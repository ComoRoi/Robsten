#_*_ coding:utf-8 _*_
import config
import os
import datetime as pydatetime
#import requests
import datetime
# 설정값 관리
comConSet = config.COMMON_CONFIG
exeDir = comConSet['exeDir']
file = exeDir + "/time.txt"

def currentTime():
    global nowDatetime
    nowDatetime = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S] ')
    return nowDatetime
    print(nowDatetime)

def get_now():
    """
        현재 시스템 시간을 datetime형으로 반환
    """
    return pydatetime.datetime.now()

def get_now_timestamp():
    """
        현재 시스템 시간을 POSIX timestamp float형으로 반환
    """
    return get_now().timestamp()


#실행가능한 시간값 읽어오기
def readtime():
    f = open(file, 'r')
    readTime = f.readline()
    f.close()
    return readTime

# writedata.py
def writetime():
    f = open(file, 'w')
    ts = get_now_timestamp()
    f.write(str(ts + 86700))
    print(currentTime()  + "Executed at " + str(ts))
    f.close()

rt = float(readtime())
ct = get_now_timestamp()

#print(currentTime() +"Record Time  : " + str(rt))
#print(currentTime() +"Current Time : " + str(ct))
if rt > ct :   # 실행시간이 도달하지 않음
    #print(currentTime()+ "Not executed")  
    exit()

elif rt <= ct :  # 실행가능 시간임
    os.system("/opt/homebrew/bin/python3 /Users/rsi/github/Robsten/main.py")
    writetime()

