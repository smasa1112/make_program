import tkinter as tk 

#二項演算モデルの作成
current_number=0
first_term=0 #第一項
second_term=0 #第２項
operator=""

result=0

def do_operator(input_operator):
    #演算子キーが押された場合の計算動作
    global current_number
    global first_term
    global operator
    first_term=current_number
    current_number=0
    operator=input_operator

def do_eq():
    global second_term
    global result
    global current_number
    second_term=current_number
    #演算部分・記号によって入れ替え
    if operator=="+":
        result=first_term+second_term
    elif operator=="-":
        result=first_term-second_term
    elif operator=="×":
        result=first_term*second_term
    elif operator=="÷":
        if second_term==0:
            result=0
        else:
            result=first_term//second_term
    current_number=0

def key1():
    key(1)
def key2():
    key(2)
def key3():
    key(3) 
def key4():
    key(4) 
def key5():
    key(5)       
def key6():
    key(6)       
def key7():
    key(7)       
def key8():
    key(8) 
def key9():
    key(9) 
def key0():
    key(0) 

# 数字キーを一括処理する関数
def key(n):
 global current_number
 current_number = current_number * 10 + n
 show_number(current_number)

def clear():
    global current_number
    current_number=0
    show_number(current_number)       

def plus():
    do_operator("+")
    show_number(current_number)

def minus():
    do_operator("-")
    show_number(current_number)

def multi():
    do_operator("×")
    show_number(current_number)

def devide():
    do_operator("÷")
    show_number(current_number)


def eq():
    do_eq()
    show_number(result)

def show_number(num):
    e.delete(0,tk.END)
    e.insert(0,str(num))



# tkinter での画面の構成
root = tk.Tk()
f = tk.Frame(root,bg="#ffffc0")
f.grid()
# ウィジェットの作成
b1 = tk.Button(f,text='1', command=key1,font=('Helvetica', 14),bg="#ffffff",width=2)
b2 = tk.Button(f,text='2', command=key2,font=('Helvetica', 14),bg="#ffffff",width=2)
b3 = tk.Button(f,text='3', command=key3,font=('Helvetica', 14),bg="#ffffff",width=2)
b4 = tk.Button(f,text='4', command=key4,font=('Helvetica', 14),bg="#ffffff",width=2)
b5 = tk.Button(f,text='5', command=key5,font=('Helvetica', 14),bg="#ffffff",width=2)
b6 = tk.Button(f,text='6', command=key6,font=('Helvetica', 14),bg="#ffffff",width=2)
b7 = tk.Button(f,text='7', command=key7,font=('Helvetica', 14),bg="#ffffff",width=2)
b8 = tk.Button(f,text='8', command=key8,font=('Helvetica', 14),bg="#ffffff",width=2)
b9 = tk.Button(f,text='9', command=key9,font=('Helvetica', 14),bg="#ffffff",width=2)
b0 = tk.Button(f,text='0', command=key0,font=('Helvetica', 14),bg="#ffffff",width=2)
bc = tk.Button(f,text='C', command=clear,font=('Helvetica', 14),bg="#ff0000",width=2)
bp = tk.Button(f,text='+', command=plus,font=('Helvetica', 14),bg="#00FF00",width=2)
bm = tk.Button(f,text='-', command=minus,font=('Helvetica', 14),bg="#00FF00",width=2)
bmul = tk.Button(f,text='×', command=multi,font=('Helvetica', 14),bg="#00FF00",width=2)
bd = tk.Button(f,text='÷', command=devide,font=('Helvetica', 14),bg="#00FF00",width=2)
be = tk.Button(f,text="=", command= eq,font=('Helvetica', 14),width=2)

# Grid 型ジオメトリマネージャによるウィジェットの割付
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=0)
bc.grid(row=1,column=4)
be.grid(row=4,column=4)
bp.grid(row=1,column=3)
bm.grid(row=2,column=3)
bmul.grid(row=3,column=3)
bd.grid(row=4,column=3)

# 数値を表示するウィジェット
e = tk.Entry(f,font=('Helvetica',14))
e.grid(row=0,column=0,columnspan=5)
clear()
# ここから GUI がスタート
root.mainloop()