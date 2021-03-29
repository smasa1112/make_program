# ユーザーの作成プログラム一覧

### discord_comment_reading_bot
Discord内でコメントを読み上げるようにしたプログラム  
read_bot.pyを自身で作成し、他プログラムはhts_engine及びopen_jtalk配布サイトから拝借  
コマンドプロンプトから使用可能  
このような使い方が適切かはわからないが、すべてのファイルが入っているためダウンロードし、read_bot.pyの部分のサーバーキーを書き換えることで、他サーバーでも使用可能である  

###  Culcjava
Android studioで作成した電卓アプリ  
言語はjavaによって作成した  
Android端末及び、仮想端末で使用可能  
https://anharu.keiji.io/  
上記サイトを参考に細かい位置等を調整  
また最新verのAndroid studioに合わせた設計にした  

### Analysis_python  
研究室内で作成したpython解析プログラムの一部  
それぞれのプログラムに関して以下解説  

#### analysis_with_lfp.py  
電極で計測されたマウスの神経活動を描画するプログラム
個別に取得した神経中枢応答(LFP)及び神経末梢応答(ABR)を描画する
研究室内で作成したライブラリ(glia,tath,piag,cosnail)が必要
