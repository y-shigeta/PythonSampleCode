import sys,os,webbrowser,difflib,threading,time,calendar,datetime

import pyautogui as pag
import sys
import pyperclip
import time

# 画像座標の取得関数
def get_coord(png):
    # 画像ファイルのパス
    file_path = png+".png"
    if "radio_" == png[:6]:
    # ラジオボタンは左上から10ほど右下
        x,y,w,h = pag.locateOnScreen(file_path)
        temp_coord = (x+10,y+10)
    else:
    # ラジオボタン以外は真ん中
        temp_coord = pag.locateCenterOnScreen(file_path)
    # Noneチェック
    if temp_coord is None:
        print(file_path+"の座標が見つかりませんでした")
        sys.exit()
    return temp_coord

# 画像リスト
png_list=["csv", "system", "text_name", "text_price", "radio_single", "radio_set", "text_comment", "button_next"]
# 画像座標
coord = {}
for png in png_list:
    x,y = get_coord(png)
    coord.update({png:{"x":x, "y":y}})
# 余白座標(次へボタンの少し下の余白部分とする)
x,y = (coord["button_next"]["x"], coord["button_next"]["y"]+20)
coord.update({"margin":{"x":x, "y":y}})
print(coord)

"""
# システムに入力する行数
rows = 5
pag.PAUSE = 1.0
# CSVファイルをアクティブに
pag.click(x=coord["csv"]["x"], y=coord["csv"]["y"])
# 指定行数分ループ
for row in range(0, rows):
    # 商品名
    pag.hotkey('ctrl', 'c')
    pag.click(x=coord["system"]["x"], y=coord["system"]["y"])
    pag.click(x=coord["text_name"]["x"], y=coord["text_name"]["y"])
    pag.hotkey('ctrl', 'v')
    # 値段
    pag.click(x=coord["csv"]["x"], y=coord["csv"]["y"])
    pag.press('tab')
    pag.hotkey('ctrl', 'c')
    pag.click(x=coord["system"]["x"], y=coord["system"]["y"])
    pag.click(x=coord["text_price"]["x"], y=coord["text_price"]["y"])
    pag.hotkey('ctrl', 'v')
    # 単品/セット
    pag.click(x=coord["csv"]["x"], y=coord["csv"]["y"])
    pag.press('tab')
    pag.hotkey('ctrl', 'c')
    pag.click(x=coord["system"]["x"], y=coord["system"]["y"])
    num = str(pyperclip.paste()).strip()
    if num == "単品":
        pag.click(x=coord["radio_single"]["x"], y=coord["radio_single"]["y"])
    elif num == "セット":
        pag.click(x=coord["radio_set"]["x"], y=coord["radio_set"]["y"])
    # 説明
    pag.click(x=coord["csv"]["x"], y=coord["csv"]["y"])
    pag.press('tab')
    pag.hotkey('ctrl', 'c')
    pag.click(x=coord["system"]["x"], y=coord["system"]["y"])
    pag.click(x=coord["text_comment"]["x"], y=coord["text_comment"]["y"])
    pag.hotkey('ctrl', 'v')
    # 次へボタン
    pag.click(x=coord["button_next"]["x"], y=coord["button_next"]["y"])
    pag.click(x=coord["margin"]["x"], y=coord["margin"]["y"])
    # CSVファイルの次の行へ
    pag.click(x=coord["csv"]["x"], y=coord["csv"]["y"])
    pag.press(['enter', 'enter'])
"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
browser.get('https://www.google.com')
time.sleep(3)

search_box = browser.find_element_by_name("q")
search_box.send_keys('練馬　美味しい店')
search_box.submit()
time.sleep(3)

for g_h3 in browser.find_elements_by_css_selector(".g h3"):
    print(g_h3.text)
time.sleep(1)


stats = browser.find_element_by_id("resultStats").text
print(stats)
for i, g in enumerate(browser.find_elements(By.CLASS_NAME, "g")):
    print("------ " + str(i+1) + " ------")
    r = g.find_element(By.CLASS_NAME, "r")
    print(r.find_element(By.TAG_NAME, "h3").text)
    print("\t" + r.find_element(By.TAG_NAME, "a").get_attribute("href"))
    r.click()
    s = g.find_element(By.CLASS_NAME, "s")
    print("\t" + s.find_element(By.CLASS_NAME, "st").text)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Gmailのリンクをクリック
element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Gmail"))
)

# Macの場合、COMMANDキーを押しながらGmailリンクをクリック
actions = ActionChains(browser)
actions.key_down(Keys.COMMAND)

# Windowsの場合はCTRLキー
# actions.key_down(Keys.CONTROL)

actions.click(element)
actions.perform()

browser.back()
browser.forward()
browser.refresh()
browser.quit()


class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass

if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                 "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()
        my_car.say_state()

import tkinter as tk
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


import sys,os,webbrowser,difflib,threading,time,calendar,datetime

#OS/sys test
print(sys.platform)
print(sys.path)
try:
    print(sys.exc_info())
    sys.exit()
except:
    print(sys.exc_info())

p = os.getcwd()
print(os.listdir(p))

url="https://www.google.com"
#webbrowser.open_new_tab(url)

#diff test
diff1 = "abcd"
diff2 = "abce"
diff = difflib.Differ()
res = diff.compare(diff1,diff2)
[print(d) for d in list(res)]

# thread testing
def call_th(prm1,prm2):
    for t in range(1,prm1+1):
        time.sleep(prm2)
        print ("[{0}] {1}/{2}".format(threading.current_thread().name,t,prm1))

tread_1 = threading.Thread(name="thread_1",target=call_th,args=(3,0.5))
tread_1.start()
time.sleep(0.5)

tread_2 = threading.Thread(name="thread_2",target=call_th,args=(3,0.3))
tread_2.start()
time.sleep(0.5)

tread_3 = threading.Thread(name="thread_3",target=call_th,args=(3,0.1))
tread_3.start()
time.sleep(0.5)

#calendar
year=datetime.date.today().year
month=datetime.date.today().month
print ("{0}Year {1} Month".format(year,month))
print(calendar.month(year,month))
print (calendar.calendar(year))
"""

"""
import inspect
print(inspect.getdoc(os))
print(inspect.getfile(os))
print(inspect.getmembers(os)[:3])

import csv
header = ["A","B","C"]
data = [[1,2,3],[4,2,3],[5,2,3]]
with open("test.csv", mode="w") as fp:
    writer = csv.writer(fp,lineterminator="\n")
    writer.writerow(header)
    writer.writerow(data)

import getpass
uid = input("ID: ")
password = getpass.getpass("Password: ")
print ("uid")

import logging
logging.basicConfig(level=logging.DEBUG,filename="test.log",format="%(asctime)s:%(lineno)s:%(levelname)s:%(message)s")
logging.debug("debug")
logging.info("info")
logging.warning("warn")
logging.error("error")
logging.critical("critical")

obj = {'hoge': 1, 'fuga': 1, 'foo': 2}
del obj['hoge']
print(obj)

s = set()
s.add(1)
s.add(2)
s.add(1)
print(s)

i = 0
while True:
    if i > 100:
        print ("LOOP IS END")
        break
    i += 1


list = ['hoge','fuga',10,1,2,5,True]
for i in list:
    print(i)

l = [i for i in range(100) if i % 3 == 0 and i % 5 == 0]
print(l)

for i in range(100):
    if i % 10 == 0:
        print ("hoge")
    elif i % 5 == 0:
        print ("fuga")
    else:
        i = i + 4

class Hoge:
    def __init__(self,hoge,fuga):
        self.hoge = hoge
        self.fuga = fuga

    def getHoge(self):
        print (self.hoge)
    def getFuga(self):
        print (self.fuga)

h = Hoge("hoge","fuga")
h.getFuga()



import numpy as np
arr = np.asarray([1,2,3])
print("A",arr)
print("B",np.mean(arr))
"""

