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
