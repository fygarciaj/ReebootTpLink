#!/usr/bin/env python
# coding: utf-8

import socket
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.0", 53))
        return True
    except OSError:
        print("Error de socket")
        pass
    return False



if (not is_connected()):
    s = Service('webdriver//chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get('http://192.168.1.10:8181')
    driver.find_element('xpath', '//*[@id="userName"]').send_keys('admin')
    driver.find_element('xpath', '//*[@id="pcPassword"]').send_keys('villaros@')
    driver.find_element('xpath', '//*[@id="loginBtn"]').click()
    j = driver.execute_script("return document.title")
    print(j)
    j = driver.execute_script("return window.top.location.href.toString()")
    print(j)
    xsplit = j.split("/")
    print(xsplit)
    xtpath = xsplit[3]
    print(xtpath)
    driver.execute_script('document.getElementById("mainFrame").src = "http://192.168.1.10:8181/'+xtpath+'/userRpm/SysRebootRpm.htm";')
    driver.switch_to.frame('mainFrame')
    driver.find_element(By.ID, 'reboot').click()
    Alert(driver).accept()
    
    #driver.get('http://192.168.1.10:8181/'+xtpath+'/userRpm/SysRebootRpm.htm')
print("Fin de ejecucion")
