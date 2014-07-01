# -*- coding: UTF-8 -*-
'''
# Created on 2014/4/10

@author: zhangda
'''
import threading
import datetime, sys
import RegOneThread
import RegTest4

class ThreadClass(threading.Thread):
    def run(self):
        now = datetime.datetime.now()
        print "%s says Hello World at time: %s" % (self.getName(), now)


def getProxy():
    proxys = []
    for line in open("proxy.txt"):
        #index = line.find(':')
        '''if index != -1:
            ip = line[:index]
            port = line[index + 1:len(line) - 1]
            print ip, port'''
        proxys.append(line[:len(line) - 1])
    
    return proxys

def writeToFile(content):
    myfile = open('ret.txt', 'a')            # open for output (creates)
    myfile.write(content)        # write a line of text
    myfile.close()

if __name__ == "__main__":
    proxys = getProxy()
    for proxy in proxys:
        print("---------------------------")
        print("Use proxy : " + proxy)
        print("---------------------------")
        try:
            ret = RegTest4.registerOne(proxy)
            writeToFile(ret + '\n')
        except :
            print "Unexpected error:", sys.exc_info()[0]
            
        
    '''for i in range(2):
        t = RegOneThread.RegOneThread()
        t.start()'''

