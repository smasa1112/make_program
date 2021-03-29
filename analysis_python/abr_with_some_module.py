# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:33:02 2020

@author: sakagami masaaki
purpose: plot abr with glia,tath
guide:
    1.gliaのwaveform系列でcsvファイルの刺激波形を取得
    2.同ファイルの刺激の種類を表記
    (3．刺激番号と刺激波形を対応させたjsonファイルを作成し、刺激番号の音圧等をふる)
    4.横軸を時間・縦軸を電圧とした波形の描画を行う
    5.描画した波形を.png形式で保存する
    ___
    Ex1.continuasファイルのもとを描画する隙間を作る
"""
import tath
import cosnail
import glia
import matplotlib.pyplot as plt
import numpy as np
import os


filelist = list(tath.selectively('.+\\.csv',tath.listup("C:/Users/student/programming/2020_03_23_USStim/abr")))
datas={}
#csvファイルに記載されたデータをwaveform型のデータとして取得
for filename in filelist:
    datas[tath.Path(filename).body]=cosnail.read_abrcsv(filename,add_dict_key_ID=False)
#各csvファイル内に存在する刺激の種類を配列として取得
wave_status={}
stim_label=["c","us","usm"]
for filename in filelist:
    wave_status_key=tath.Path(filename).body
    wave_status[wave_status_key]=[]
    for stim_name in stim_label:
        for i in range(0,100):
            for j in range(0,100):
                 if stim_name+str(i)+"-"+str(j) in filename and i<j:
                    for k in range(i,j+1):
                        wave_status[wave_status_key].append(stim_name+str(k))
                 elif stim_name+str(i)+".csv" in filename:
                    wave_status[wave_status_key].append(stim_name+str(i))
                    break
#計測データと刺激の種類を組み合わせてdict型にする{filename:[{stim_name:stim_data},...],filename:...}の形にする
wave_dict={}
for wave_dictname in wave_status.keys():
    #対応するwave_statusのものとdictを作成        
    data_dict=dict(zip(wave_status[wave_dictname],datas[wave_dictname].values()))
    wave_dict[wave_dictname]=data_dict

#作成した各波形ごとにグラフを描画できるようにする
for wave_dictname in wave_dict.keys():
    #描画グラフを保存するディレクトリの作成
    if not(os.path.exists("abr_plotdata")):
        os.mkdir("abr_plotdata")
    dir_path="./abr_plotdata/"+wave_dictname
    if not(os.path.exists(dir_path)):
        os.mkdir(dir_path)
    for stim_wavename,stim_wavedata in wave_dict[wave_dictname].items():
        fig=plt.figure()
        ax=fig.add_subplot(111)
        #units:Hz
        sampling_rate=25000
        timespan=1000
        print(wave_dict[wave_dictname][stim_wavename])
        x=[xl/(sampling_rate/timespan) for xl in range(len(stim_wavedata))]
        y=stim_wavedata
        ax.plot(x,y)
        ax.set_title(stim_wavename)
        ax.set_xlim(0,20)
        ax.set_ylim(-1500,1500)
        fig.savefig(os.path.join(dir_path,wave_dictname+"_stimname-"+stim_wavename+".png"))
        plt.close()

        