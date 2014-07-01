# -*- coding: UTF-8 -*-
'''
# Created on 2014/4/10

@author: zhangda
'''

import RegTest3
import threading
import datetime

class RegOneThread(threading.Thread):
    '''
    register one number
    '''
    def run(self):
        now = datetime.datetime.now()
        RegOneThread.register(self)


    def register(self):
        print("%s says Hello World at time: %s" % (self.getName(), datetime.datetime.now()))
        RegTest3.registerOne(self.getName())
        
        