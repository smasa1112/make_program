"""
坂上のlfpデータ解析描画プログラム
事前準備として、tath,cosnail,gliaのインストールが必要
"""
#ライブラリの格納
import tath
import cosnail
import glia
import matplotlib.pyplot as plt
import numpy as np 
import os
import csv
import re
import json
import OpenEphys
import scipy
from scipy import signal
import gc
import pandas as pd
import pickle

print(os.getcwd())
if not(os.path.exists("./waveform")):
    os.mkdir("./waveform")

#jsonファイルとplxファイルをそれぞれ対応させるjsonファイルを作成する
dir_path="./plx"
files=os.listdir(dir_path)
dir_names=[f for f in files if os.path.isdir(os.path.join(dir_path,f))]
result_path="./json"
files=os.listdir(result_path)
result_names=[f for f in files if "result" in f]

matching=dict(zip(dir_names,result_names))
print(matching)

#jsonファイルに辞書を成型して出力
#ensure...日本語出力可能
with open('matching.json', 'w') as f:
    json.dump(matching, f, ensure_ascii=False)

def lowpass(x, samplerate, fp, fs, gpass, gstop):
    fn = samplerate / 2                           #ナイキスト周波数
    wp = fp / fn                                  #ナイキスト周波数で通過域端周波数を正規化
    ws = fs / fn                                  #ナイキスト周波数で阻止域端周波数を正規化
    N, Wn = signal.buttord(wp, ws, gpass, gstop)  #オーダーとバターワースの正規化周波数を計算
    b, a = signal.butter(N, Wn, "low")           #フィルタ伝達関数の分子と分母を計算
    y = signal.filtfilt(b, a, x)                  #信号に対してフィルタをかける
    return y

with open("matching.json",encoding = "utf-8") as json_fp:
    rec_stim_matching = json.load(json_fp)
reload = False
#rec_stim_matching={dir_name:result.json}
print(rec_stim_matching)

for dirname in rec_stim_matching.keys():
    jsonfile=rec_stim_matching[dirname]
    pathname=f"./plx/{dirname}"
    #Ephys形式で記録されたチャネルマップ配置
    channel_map = [9,8,10,7,13,4,12,5,15,2,16,1,14,3,11,6]


    #刺激方法の設定をSetting.jsonのファイルから読み込む
    #jsonファイルは日程-時間で記録されているため、result.jsonに記載された日程を参照する
    with open(f"./json/{jsonfile[:14]}Settings.json",encoding="UTF-8") as json_fp:
        stim_setting=json.load(json_fp)

    if not(os.path.exists(f"./waveform/{dirname}")):
        os.mkdir(f"./waveform/{dirname}")
    num=1
    for i in channel_map:
        #OpenEphys.pyを使用してcontinuousファイルの読み込み
        tmp=OpenEphys.loadContinuous(f"./plx/{dirname}/101_CH{str(i)}.continuous")
        #lowpassフィルタがかけられた波形を抽出
        waveform=glia.nucleus.Waveform(lowpass(tmp["data"],30000,450,600,10,30),rate=glia.Frequency(30000))
        #tmp(['header', 'timestamps', 'data', 'recordingNumber'])が記載されている
        #timestampsはサンプリングレートで記録された記録点
        timestamps=tmp["timestamps"][0]
        if num<10:
            glia.save(f"./waveform/{dirname}/0{num}.lfp",waveform)
        else:
            glia.save(f"./waveform/{dirname}/{num}.lfp",waveform)
        del tmp,waveform
        gc.collect()
        num+=1

    events = OpenEphys.loadEvents(pathname+"/all_channels.events")
    #eventsにはトリガーの始点・終点が入っているので、始点だけ取り出す
    e_tmp=(events["timestamps"]-timestamps)[0::2]
    trigger=[]
    #millisecondのスケールでトリガー情報をtriggerに格納
    for i in (e_tmp/30):
        trigger.append(glia.millisecond(i))
    #numpy配列に変換
    trigger=np.array(trigger)
    glia.save(f"./waveform/{dirname}/{dirname}.trigger",trigger)        
    print((events["timestamps"]-timestamps)[0::2])

    #この状態で.lfpファイルにはそれぞれのチャネルからの計測電圧が入る
    #.triggerファイルではトリガーファイルが入る

    #刺激パターンをjsonファイルから読み込んで、.stimorderファイルに格納
    with open("json/"+jsonfile,encoding="utf-8") as json_fp:
        stim_pattern = json.load(json_fp)
    #刺激種類を記録したjsonファイルのdictをpandasの形に変換
    table = pd.DataFrame(stim_pattern)
    glia.save(f"./waveform/{dirname}/{dirname}.stimorder",table)
    
    lfp_file_path=f"./waveform/{dirname}/"
    #該当パスからlfpファイルの抽出
    lfp_file_list=list(tath.ext(".lfp",tath.listup(lfp_file_path)))
    #stim_order_file・triggerファイルの読み込み
    stim_pattern=glia.load(f"./waveform/{dirname}/{dirname}.stimorder")
    trigger=glia.load(f"./waveform/{dirname}/{dirname}.trigger")

    offset=glia.milliseconds(50)
    duration=glia.milliseconds(400)
    result={}
    #それぞれの刺激ラベルにおいて空リストの作成
    for i in range(len(stim_pattern["name"].values)):
        result[stim_pattern["name"].values[i]]=[]
    #lfpファイルを読み込みそれぞれの刺激ラベルに対してリストを追加していく
    for filename in lfp_file_list:
        wave=glia.load(filename)
        if stim_setting["Mode"]=="ABR Mode(TDT)":
            for i in range(len(stim_pattern["name"].values)):
                timing=trigger[(i*350+i*2):(i*350+i*2+350)]
                rec=glia.average(glia.extract(wave,timing-offset,duration))
                result[stim_pattern["name"].values[i]].append(rec)
        else:
            for key, blob in table.groupby("name"):
                    timing = trigger[blob.index]
                    rec=glia.average(glia.extract(wave,timing-offset,duration))
                    result[key].append(rec)
    print(result.keys())
    glia.save(f"./waveform/{dirname}.lfps",result)

    #作成した波形lfpsファイルから波形を描画してみる
    #画像フォルダの作成
    if not(os.path.exists("./waveform/wave_figure")):
        os.mkdir("./waveform/wave_figure")
    lfp_data=glia.load(f"./waveform/{dirname}.lfps")
    depth=50
    for key in lfp_data.keys():
        fig=plt.figure()
        ax=fig.add_subplot(111)
        for i,x in enumerate(lfp_data[key]):
            ax.plot(x-i*depth,color="k")
        ax.set_xlabel("time[ms]")
        ax.set_xticks(np.arange(0,13500,1500))
        ax.set_xticklabels(np.arange(-50,400,50))
        ax.set_ylabel("depth[um]")
        ax.set_yticks(np.arange(0,-900,-100))
        ax.set_yticklabels(np.arange(0,900,100))
        plt.savefig(f"./waveform/wave_figure/{key}.png")
    """
    for key in lfp_data.keys():
        fig=plt.figure()
        ax=fig.add_subplot(111)
        for i,x in enumerate(lfp_data[key]):
            ax1.plot(x-i*depth)
        fig.savefig()
    """