# -*- coding: UTF-8 -*-
'''
Created on 2014/4/2

@author: zhangda
'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver  = webdriver.Firefox()


#browser.quit()

def inputSlowly(id, content):
    elm = driver.find_element_by_id(id)
    for c in content:
        elm.send_keys(c)
        time.sleep(0.01)
        
def clearCookie():
    driver.get('http://reg.qq.com')
    driver.get('http://zc.qq.com/chs/index.html')
    driver.delete_all_cookies()
    # 获得cookie信息
    cookie= driver.get_cookies()
    #将获得cookie的信息打印
    print cookie
def run():
    

    driver.get('http://reg.qq.com')
    driver.get('http://zc.qq.com/chs/index.html')
    driver.find_element_by_id("nav_1").click()
    inputSlowly("nick","xiaoxie1")
    inputSlowly("password","xiaoxie1")
    inputSlowly("password_again","xiaoxie1")
    
    driver.find_element_by_id("sex_2").click()
    time.sleep(0.01)
    driver.find_element_by_id("birthday_type_value").send_keys(Keys.TAB)
    time.sleep(0.01)
    driver.find_element_by_id("year_value").send_keys(Keys.TAB)
    time.sleep(0.01)
    driver.find_element_by_id("month_value").send_keys(Keys.TAB)
    time.sleep(0.01)
    driver.find_element_by_id("day_value").send_keys(Keys.TAB)
    time.sleep(0.01)
    driver.find_element_by_id("country_value").send_keys(Keys.TAB)
    time.sleep(0.01)
    driver.find_element_by_id("province_value").send_keys(Keys.TAB)
    time.sleep(0.01)
    driver.find_element_by_id("city_value").send_keys(Keys.TAB)
    
    
    #driver.quit()

if __name__ == "__main__":
    clearCookie()
    run()