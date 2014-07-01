# -*- coding: UTF-8 -*-
'''
Created on 2014/3/30
Reg qq without verification code
@author: dada
'''

import UtilNoVC, cookielib, SecCode, httplib
import urllib, urllib2, time


def register():
    response = UtilNoVC.sendPostWithHeader("http://zc.qq.com/cgi-bin/chs/numreg/get_acc?r=" + "0.42129214744869004", UtilNoVC.postdata, UtilNoVC.headers)
    print(response.info())
    ret = response.read()
    print(ret)
    return ret
    
        
    
def initPage(threadName):
    #some special init
    UtilNoVC.sendPtLoginGet("http://ptlogin2.qq.com/qq_signup?ptlang=2052&regkey=313D40DEBEB5C0B0083AEF80FAB95A6DD1DA8393E4BE6CB6DFEE4F918EDBBE2B&ADUIN=0&ADSESSION=0&ADTAG=CLIENT.QQ.5281_NewAccount_Btn.0&ADPUBNO=26292")
    #zc.qq.com
    UtilNoVC.sendPtLoginGet2(UtilNoVC.newurl)
    #new router
    UtilNoVC.sendPtLoginGet3(UtilNoVC.newurl)
    #index.html
    UtilNoVC.sendIndexGet(UtilNoVC.newurl)
    UtilNoVC.sendVerJSGet("http://zc.qq.com/en/ver.js?v=0.8133795140461465", UtilNoVC.newurl)
    response = UtilNoVC.sendGetWithReferHeader("http://zc.qq.com/cgi-bin/en/othmailreg/init?r=0.6421093098453319&cookieCode=undefined", UtilNoVC.newurl)
    UtilNoVC.setInitData(response, UtilNoVC.postdata)
    UtilNoVC.sendMoniKeyWithRefer("http://zc.qq.com/cgi-bin/common/attr?id=173278&r=0.6699955210210492", UtilNoVC.newurl)
    response = UtilNoVC.sendSJSGet("http://a.zc.qq.com/s.js?t=0.2977374854148608", UtilNoVC.newurl)
    secCode = SecCode.getSecCode(response)
    UtilNoVC.sendMoniKeyWithRefer("http://zc.qq.com/cgi-bin/common/attr?id=61112&timeused=0&seed=0.47954484357333593", UtilNoVC.newurl)
    UtilNoVC.sendMoniKeyWithRefer("http://zc.qq.com/cgi-bin/common/attr?id=260714&r=0.45523373243084253", UtilNoVC.newurl)
    UtilNoVC.sendMoniKeyWithRefer("http://zc.qq.com/cgi-bin/common/attr?id=278039&r=0.126593756287934", UtilNoVC.newurl)
    UtilNoVC.sendMoniKeyWithRefer("http://zc.qq.com/cgi-bin/common/attr?id=173279&r=0.6062411974921303", UtilNoVC.newurl)
    UtilNoVC.sendSecCheckGet("http://a.zc.qq.com/Cgi-bin/SecCheck?" + secCode + "&0.5301467733723995", UtilNoVC.newurl)
    UtilNoVC.sendVerJSGet("http://zc.qq.com/chs/m.js?v=0.11557472582923711", UtilNoVC.newurl)
    UtilNoVC.sendMoniKeyWithReferAQQ("http://a.zc.qq.com/Cgi-bin/MoniKey?0|4|" + str(UtilNoVC.getTime()), UtilNoVC.newurl)
    
    '''
    swith from en to chs
    '''
    UtilNoVC.sendIndexGet("http://zc.qq.com/chs/index.html")
    UtilNoVC.sendGetWithHeader("http://zc.qq.com/chs/ver.js?v=0.1699609496164347")
    UtilNoVC.sendGetWithHeader("http://zc.qq.com/cgi-bin/common/attr?id=252190&r=0.09858561242344455")
    response = UtilNoVC.sendGetWithHeader("http://zc.qq.com/cgi-bin/chs/numreg/init?r=0.26596747531327136&cookieCode=undefined")
    UtilNoVC.setInitData(response, UtilNoVC.postdata)
    UtilNoVC.sendGetWithHeader("http://zc.qq.com/cgi-bin/common/attr?id=173276&r=0.7227281477307663")
    response = UtilNoVC.sendOtherCheckGet("http://a.zc.qq.com/s.js?t=0.016436040078278036")
    secCode = SecCode.getSecCode(response)
    UtilNoVC.sendGetWithHeader("http://zc.qq.com/cgi-bin/common/attr?id=58030&timeused=0&seed=0.3017548276392469")
    UtilNoVC.sendGetWithHeader("http://zc.qq.com/cgi-bin/common/attr?id=260714&r=0.5433415712664798")
    UtilNoVC.sendGetWithHeader("http://zc.qq.com/cgi-bin/common/attr?id=278037&r=0.29890037895792143")
    UtilNoVC.sendGetWithHeader("http://zc.qq.com/cgi-bin/common/attr?id=173279&r=0.49857171260968147")
    UtilNoVC.sendOtherCheckGet("http://a.zc.qq.com/Cgi-bin/SecCheck?" + secCode + "&0.8532321740752858")
    UtilNoVC.sendGetWithHeader("http://zc.qq.com/chs/m.js?v=0.8039430183252769")
    
def inputValues():
    beginTime = UtilNoVC.getTime()
    #休眠3.5秒再发送下个请求
    time.sleep(3.5)
    
    UtilNoVC.sendGetWithHeader("http://zc.qq.com/cgi-bin/chs/common/dirty_check?nick=xiaoxie1&regType=1&r=0.4334156954487689")
    time.sleep(2.41)
    mouseTime2 = UtilNoVC.getTime()
    time.sleep(1.73)
    #password
    url = getNickLongUrl()
    time.sleep(1.1)
    UtilNoVC.sendMoniKey(url)
    time.sleep(1.2)
    
    url = getNickLongUrl()
    time.sleep(1.1)
    UtilNoVC.sendMoniKey(getPwdLongUrl1())
    time.sleep(1.3)
    
    url = getNickLongUrl()
    time.sleep(1.1)
    UtilNoVC.sendMoniKey(getPwdLongUrl2())
    time.sleep(1.4)
    
    UtilNoVC.sendMoniKey("http://a.zc.qq.com/Cgi-bin/MoniKey?9|7|" + str(UtilNoVC.getTime()))
    time.sleep(0.35)
    UtilNoVC.sendMoniKey("http://a.zc.qq.com/Cgi-bin/MoniKey?9|8|" + str(UtilNoVC.getTime()))
    time.sleep(0.35)
    UtilNoVC.sendMoniKey("http://a.zc.qq.com/Cgi-bin/MoniKey?9|9|" + str(UtilNoVC.getTime()))
    time.sleep(0.35)
    UtilNoVC.sendMoniKey("http://a.zc.qq.com/Cgi-bin/MoniKey?9|10|" + str(UtilNoVC.getTime()))
    time.sleep(0.35)
    UtilNoVC.sendMoniKey("http://a.zc.qq.com/Cgi-bin/MoniKey?9|11|" + str(UtilNoVC.getTime()))
    time.sleep(0.35)
    UtilNoVC.sendMoniKey("http://a.zc.qq.com/Cgi-bin/MoniKey?9|12|" + str(UtilNoVC.getTime()))
    time.sleep(0.35)
    UtilNoVC.sendMoniKey("http://a.zc.qq.com/Cgi-bin/MoniKey?9|13|" + str(UtilNoVC.getTime()))
    time.sleep(0.35)
    UtilNoVC.sendMoniKey("http://a.zc.qq.com/Cgi-bin/MoniKey?9|14|" + str(UtilNoVC.getTime()))
    time.sleep(0.35)
    UtilNoVC.sendMoniKey("http://a.zc.qq.com/Cgi-bin/MoniKey?0|15|" + str(UtilNoVC.getTime()))
    time.sleep(0.35)
    UtilNoVC.sendMoniKey("http://a.zc.qq.com/Cgi-bin/mouse?|0|17|" + str(beginTime) + "|1084-1083-839-775-779-792-828-820-773-637-601-599-598-598-599-604-708|42-42-135-162-160-174-157-181-215-255-283-286-401-551-551-551-564|0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0|0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0|470-470-470-470-470-470-470-470-470-470-470-470-470-470-470-470-470|1514-1514-1514-1514-1514-1514-1514-1514-1514-1514-1514-1514-1514-1514-1514-1514-1514|273-577-778-1188-7968-8281-8711-8934-9135-9338-9555-9862-10127-10366-10615-10929-11130|")
    UtilNoVC.sendOtherCheckGet("http://a.zc.qq.com/Cgi-bin/mouse?|1|1|" + str(mouseTime2) + "|775|161|1|68|470|1514|1163|")
    UtilNoVC.sendGetWithHeader("http://zc.qq.com/cgi-bin/common/attr?id=252193&r=0.7783785835026651")

def getNickLongUrl():
    #http://a.zc.qq.com/Cgi-bin/MoniKey?56|5|1396438512189&56|5|1396438512496&56|5|1396438512632&56|5|1396438512781&56|5|1396438512902&56|5|1396438513066&56|5|1396438513298&56|5|1396438513554&56|5|1396438513999
    cur = UtilNoVC.getTime()
    ret = "http://a.zc.qq.com/Cgi-bin/MoniKey?88|1|" + str(cur) +  \
        "&73|1|" + str(cur + 134) +  \
        "&65|1|" + str(cur + 132) +  \
        "&79|1|" + str(cur + 113) +  \
        "&88|1|" + str(cur + 91) +  \
        "&73|1|" + str(cur + 138) +  \
        "&69|1|" + str(cur + 167) +  \
        "&49|1|" + str(cur + 225) +  \
        "&9|1|" + str(cur + 247)
    return ret

def getPwdLongUrl1():
    #http://a.zc.qq.com/Cgi-bin/MoniKey?88|1|1396360234135&73|1|1396360234282&65|1|1396360234389&79|1|1396360234467&88|1|1396360234576&73|1|1396360234681&69|1|1396360234811&49|1|1396360235016&9|1|1396360235299
    cur = UtilNoVC.getTime()
    ret = "http://a.zc.qq.com/Cgi-bin/MoniKey?56|5|" + str(cur) + \
        "&56|5|" + str(cur + 257) +  \
        "&56|5|" + str(cur + 115) +  \
        "&56|5|" + str(cur + 129) +  \
        "&56|5|" + str(cur + 124) +  \
        "&56|5|" + str(cur + 104) +  \
        "&56|5|" + str(cur + 237) +  \
        "&56|5|" + str(cur + 253) +  \
        "&56|5|" + str(cur + 199)
    return ret

def getPwdLongUrl2():
    #http://a.zc.qq.com/Cgi-bin/MoniKey?88|1|1396360234135&73|1|1396360234282&65|1|1396360234389&79|1|1396360234467&88|1|1396360234576&73|1|1396360234681&69|1|1396360234811&49|1|1396360235016&9|1|1396360235299
    cur = UtilNoVC.getTime()
    ret = "http://a.zc.qq.com/Cgi-bin/MoniKey?56|6|" + str(cur) +  \
        "&56|6|" + str(cur + 226) +  \
        "&56|6|" + str(cur + 94) +  \
        "&56|6|" + str(cur + 133) +  \
        "&56|6|" + str(cur + 95) +  \
        "&56|6|" + str(cur + 112) +  \
        "&56|6|" + str(cur + 188) +  \
        "&56|6|" + str(cur + 254) +  \
        "&56|6|" + str(cur + 205)
    return ret

def getLastLongUrl2():
    #http://a.zc.qq.com/Cgi-bin/MoniKey?88|1|1396360234135&73|1|1396360234282&65|1|1396360234389&79|1|1396360234467&88|1|1396360234576&73|1|1396360234681&69|1|1396360234811&49|1|1396360235016&9|1|1396360235299
    cur = UtilNoVC.getTime()
    ret = "http://a.zc.qq.com/Cgi-bin/MoniKey?69|16|" + str(cur) +  \
        "&84|16|" + str(cur + 422) +  \
        "&16|16|" + str(cur + 428) +  \
        "&90|16|" + str(cur + 214) + \
        "&75|16|" + str(cur + 360)
    return ret

def registerOneOld(threadName):
    UtilNoVC.cj.load("cookie.txt")
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(UtilNoVC.cj));
    #opener = urllib2.build_opener(urllib2.ProxyHandler({"http" : '112.241.179.161:29385'}), urllib2.HTTPCookieProcessor(UtilNoVC.cj))
    urllib2.install_opener(opener);
    initPage()
    inputValues()
    UtilNoVC.lock.acquire()
    #for index, cookie in enumerate(UtilNoVC.cj):
    #    print '[',index, ']',cookie;
    #UtilNoVC.cj.save("c.txt")
    code = raw_input("Input verification code:")
    UtilNoVC.postdata["verifycode"] = code
    print(UtilNoVC.postdata)
    register()
    UtilNoVC.lock.release()
    


class RedirctHandler(urllib2.HTTPRedirectHandler):
    """docstring for RedirctHandler"""
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        if 'location' in headers:
            UtilNoVC.newurl = headers.getheaders('location')[0]
        elif 'uri' in headers:
            UtilNoVC.newurl = headers.getheaders('uri')[0]
        print("Newurl In Redirect Handler:" + UtilNoVC.newurl)
        pass
    

'''
register one, proxy is string like 36.248.36.255:11850
'''
def registerOne(proxy):
    #empty cookie
    UtilNoVC.cj = cookielib.MozillaCookieJar()
    UtilNoVC.cj.load("CookieNoVC.txt")
    #open debug
    handler=urllib2.HTTPHandler()
    #opener = urllib2.build_opener(handler, RedirctHandler, urllib2.HTTPCookieProcessor(UtilNoVC.cj));
    opener = urllib2.build_opener(handler, RedirctHandler, urllib2.HTTPCookieProcessor(UtilNoVC.cj), \
                                  urllib2.ProxyHandler({"http" : proxy}))
    urllib2.install_opener(opener);
    initPage("thread-1")
    inputValues()
    
    UtilNoVC.postdata["verifycode"] = ""
    print(UtilNoVC.postdata)
    for index, cookie in enumerate(UtilNoVC.cj):
        print '[',index, ']',cookie;
    ret = register()
    time.sleep(8)
    print("hello")
    return ret

'''
注意每次发送之前更新下POST DATA的最后一个参数
因为实在没看出他是从哪里把这个参数加上的......
'''
if __name__ == "__main__":
    UtilNoVC.cj.load("CookieNoVC.txt")
    #open debug
    handler=urllib2.HTTPHandler()
    opener = urllib2.build_opener(handler, RedirctHandler, urllib2.HTTPCookieProcessor(UtilNoVC.cj));
    #opener = urllib2.build_opener(RedirctHandler, urllib2.HTTPCookieProcessor(UtilNoVC.cj));
    #opener = urllib2.build_opener(urllib2.ProxyHandler({"http" : '112.241.179.161:29385'}), urllib2.HTTPCookieProcessor(UtilNoVC.cj))
    urllib2.install_opener(opener);
    initPage("thread-1")
    inputValues()
    
    UtilNoVC.postdata["verifycode"] = ""
    print(UtilNoVC.postdata)
    for index, cookie in enumerate(UtilNoVC.cj):
        print '[',index, ']',cookie;
    register()
    time.sleep(8)
    #print(getLastLongUrl2())'''
    #httplib.HTTPConnection.debuglevel = 1
    #res = UtilNoVC.sendPtLoginGet("http://ptlogin2.qq.com/qq_signup?ptlang=2052&regkey=A5E5F9F078C4376828E45B0244C0E0011D859E0D49E2623C1DC8D147301F3BF6&ADUIN=0&ADSESSION=0&ADTAG=CLIENT.QQ.5281_NewAccount_Btn.0&ADPUBNO=26292")
    #print(res.getcode())
    print("hello")
   