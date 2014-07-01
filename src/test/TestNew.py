# -*- coding: UTF-8 -*-
'''
Created on 2014/3/30

@author: dada
'''

import Util, cookielib
import urllib, urllib2
import time,datetime 
import random

def register():
    
    response = Util.sendPostWithHeader("http://zc.qq.com/cgi-bin/chs/numreg/get_acc?r=0.7807113883514445", Util.postdata, Util.headers)
    print(response.info())
    print(response.read())
    
    pass

def getInentifier():
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(Util.cj));
    urllib2.install_opener(opener);
    resp = urllib2.urlopen("http://zc.qq.com:443/cgi-bin/common/new_router"); 
    print(resp.info()) 
    for index, cookie in enumerate(Util.cj):
        print '[',index, ']',cookie;
        
def getMachineCookie():
    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(Util.cj));
    #urllib2.install_opener(opener);
    resp = urllib2.urlopen("http://zc.qq.com/cgi-bin/chs/numreg/init?r=0.721300816430285&cookieCode=undefined"); 
    print(resp.info()) 
    for index, cookie in enumerate(Util.cj):
        print '[',index, ']',cookie;
    
def getCodePic():
    Util.saveFile("http://captcha.qq.com/getimage?aid=1007901&r=0.8374034030256831", "1.jpg")
    
def simulatorAllProcess():
    pass


if __name__ == "__main__":
    Atime=time.time() ##获取本地时间戳 
    random.seed(0.029119366533932545)
    print(random.random())
    print random.random()
    print random.random()
    print random.random()
    print Util.getTime()
    a = 0.029119366533932545
    print(a)
    '''Util.cj.load("cookie.txt")
    getInentifier()
    getMachineCookie()
    getCodePic()
    
    for index, cookie in enumerate(Util.cj):
        print '[',index, ']',cookie;
    #Util.cj.save("c.txt")
    code = raw_input("Input verification code:")
    Util.postdata["verifycode"] = code
    print(Util.postdata)
    register()
    print("hello")
    for index, cookie in enumerate(Util.cj):
        print '[',index, ']',cookie;'''