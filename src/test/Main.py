# -*- coding: UTF-8 -*-
'''
# Created on 2014/4/10

@author: zhangda
'''
import threading, cookielib
import datetime, sys
import RegOneThread
import RegTestWithVC2, Util
from Queue import Queue
from Tkinter import *
from PIL import ImageTk, Image
import pygame



class RegThread(threading.Thread):
    def run(self):
        
        global queue, myLock, conditions
        conditions[self.getName()] = threading.Condition()
        while True:
            proxy = queue.get()
            print("---------------------------")
            print("Use proxy : " + proxy)
            print("---------------------------")
            
            try:
                reg = RegTestWithVC2.RegQQ()
                reg.prepareRegister(self.getName(), proxy, changeImg, myLock, conditions)
                myLock.acquire()
                myLock.release()
            except :
                print "Unexpected error:", sys.exc_info()


def playMusic():
    pygame.mixer.init()
    track = pygame.mixer.music.load("tkzc.wav")
    pygame.mixer.music.play()

def getProxy():
    proxys = []
    global queue
    for line in open("proxy.txt"):
        proxys.append(line[:len(line) - 1])
        queue.put(line[:len(line) - 1])
    return proxys

def writeToFile(content):
    myfile = open('ret.txt', 'a')            # open for output (creates)
    myfile.write(content)        # write a line of text
    myfile.close()


queue = Queue()
regQueue = Queue()
codes = {}

def click(event=None):
    global myLock, conditions
    Util.code = input.get()
    print(Util.code)
    conditions[Util.curName].acquire()
    conditions[Util.curName].notify()
    conditions[Util.curName].release()
    myLock.release()
    input.delete(0, END)
    

def changeImg(threadName):
    print("in")
    path = '../../pic/' + threadName + '.jpg'
    newImg = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image = newImg)
    panel.image = newImg
    

if __name__ == "__main__":
    global panel, myLock, conditions
    myLock = threading.Lock()
    conditions = {}
    proxys = getProxy()
    threadNum = 9
    
    for i in range(threadNum):
        t = RegThread()
        t.start()
    path = '../../pic/1.jpg'

    win = Tk()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(win, image = img)
    panel.pack(expand=YES, fill=BOTH)
    input = Entry(win,text='输入')
    input.pack(expand=YES, fill=BOTH)
    btn = Button(win, text='OK', command=click)
    btn.pack(expand=YES, fill=BOTH)
    win.bind('<Return>', click)
    win.mainloop()
            
