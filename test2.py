import sys,os,webbrowser,difflib,threading,time,calendar,datetime

"""
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
"""

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

