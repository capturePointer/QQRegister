# -*- coding: UTF-8 -*-
'''
Created on 2014/4/22

@author: dada
'''
import hashlib, urllib2
import Util

def login(user, pwd):
    m = hashlib.md5(pwd)
    m.digest()
    md5Pwd = m.hexdigest()
    postValues = "VER=1.1&CMD=Login&SEQ=" + str(Util.getTime()) \
                + "&UIN=" + user + "&PS=" + md5Pwd + " &M5=1&LC=9326B87B234E7235"
    data = {'VER':'1.1', 'CMD':'Login', 'SEQ':str(Util.getTime()), 'UIN':user, 'PS':md5Pwd, 'M5':'1', 'LC':'9326B87B234E7235'}  
    url = "http://tqq.tencent.com:8000"       
    res = Util.loginPost(url, data)   
    print(res.info()) 
    print(res.read())

if __name__ == "__main__":
    handler = urllib2.HTTPHandler(debuglevel = 1)
    opener = urllib2.build_opener(handler, urllib2.HTTPCookieProcessor(Util.cj));
    #opener = urllib2.build_opener(RedirctHandler, urllib2.HTTPCookieProcessor(UtilNoVC.cj));
    #opener = urllib2.build_opener(urllib2.ProxyHandler({"http" : '112.241.179.161:29385'}), urllib2.HTTPCookieProcessor(UtilNoVC.cj))
    urllib2.install_opener(opener);
    login("2746790541", "xiaoxie1")