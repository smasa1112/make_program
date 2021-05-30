# ユーザーの作成プログラム一覧

### [discord_comment_reading_bot]("https://github.com/smasa1112/make_program/tree/master/discord_comment_reading_bot")
Discord内でコメントを読み上げるようにしたプログラム  
read_bot.pyを自身で作成し、他プログラムはhts_engine及びopen_jtalk配布サイトから拝借  
コマンドプロンプトから使用可能  
このような使い方が適切かはわからないが、すべてのファイルが入っているためダウンロードし、read_bot.pyの部分のサーバーキーを書き換えることで、他サーバーでも使用可能である  

###  [Culcjava]("https://github.com/smasa1112/make_program/tree/master/Culcjava")
Android studioで作成した電卓アプリ  
言語はjavaによって作成した  
Android端末及び、仮想端末で使用可能  
https://anharu.keiji.io/  
上記サイトを参考に細かい位置等を調整  
また最新verのAndroid studioに合わせた設計にした  

### Analysis_python  
研究室内で作成したpython解析プログラムの一部  
それぞれのプログラムに関して以下解説  

#### analysis_abr_with_lfp.py  
電極で計測されたマウスの神経活動を描画するプログラム  
個別に取得した神経中枢応答(LFP)及び神経末梢応答(ABR)を描画する  
研究室内で作成したライブラリ(glia,tath,piag,cosnail)が必要  

#### abr_with_some_module.py
末梢神経応答(ABR)をcsvファイルから取得・描画するためのプログラム  
/abr_plotdata/ というディレクトリを作成し、そこに画像を保存する  

#### lfp_plot.py
上記analysis_abr_with_lfp.pyを改良して広範に対応できるようにしたプログラム  
２つのディレクトリからそれぞれファイルを一つずつ対応づけし、神経活動電位を加算平均した電圧値列をバイナリファイル(.lfpsファイル)に変換する  
その後lfpsファイルを用いて、それぞれの波形を描画する。lfpsファイルにすることで通常数十GB単位の容量があるデータを数KBにして持ち運びを行いやすくする。

### python_practice  
自身で勉強して作成したpythonプログラム   
ipynb形式or pyファイルとして残してある  

#### python_scikit-learn_practice.ipynb
scikit-learnを使用して単回帰分析によるボストンの地価予測を行った  
全データを7:3にわけ、訓練データをもとにテストデータの地価予測を行う  

#### tk_calc_model.py
tkinterをGUIアプリケーションとして電卓アプリを作成した  
出力はすべて整数のみで、除算に関しても整数値の最大値が出力される  
