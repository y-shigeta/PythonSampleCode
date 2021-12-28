## tkinter sample code
import tkinter as tk
from tkinter import messagebox as mbox

win = tk.Tk()
win.title("Hello")
win.geometry("400x300")

label = tk.Label(win,text = "title?")
label.pack()

# テキストボックスを作成
text = tk.Entry(win)
text.pack()
text.insert(tk.END, 'クジラ') # 初期値を指定

# OKボタンを押した時 --- (*3)
def ok_click():
    # テキストボックスの内容を得る
    s = text.get()
    # ダイアログを表示
    mbox.showinfo('挨拶', s + 'さん、こんにちは!')

# ボタンを作成 --- (*4)
okButton = tk.Button(win, text='OK', command=ok_click)
okButton.pack()

win.mainloop()
