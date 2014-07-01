# -*- coding: UTF-8 -*-
'''
# Created on 2014/4/10

@author: zhangda
'''
import threading, cookielib, time
import datetime, sys
import RegOneThread
import RegTestWithVC, Util
from Queue import Queue
from Tkinter import *
from PIL import ImageTk, Image



class RegThread(threading.Thread):
    def run(self):
        Util.code = self.getName()
        while True:
            print(Util.code)
            time.sleep(2)


    

if __name__ == "__main__":

    threadNum = 2
    
    for i in range(threadNum):
        t = RegThread()
        t.start()
    path = '../../pic/1.jpg'

