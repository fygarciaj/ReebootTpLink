#!/usr/bin/env python
# coding: utf-8

import socket

from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        print("socket ERROR")
        pass
    return False



if (not is_connected()):
    print(config('ROUTER_USERNAME'))
    s = Service('webdriver//chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get(config('ROUTER_URL'))
    driver.find_element('xpath', '//*[@id="userName"]').send_keys(config('ROUTER_USERNAME'))
    driver.find_element('xpath', '//*[@id="pcPassword"]').send_keys(config('ROUTER_PASSWORD'))
    driver.find_element('xpath', '//*[@id="loginBtn"]').click()
    j = driver.execute_script("return window.top.location.href.toString()")
    print(j)
    xsplit = j.split("/")
    print(xsplit)
    xtpath = xsplit[3]
    print(xtpath)
    driver.execute_script('document.getElementById("mainFrame").src = "'+config('ROUTER_URL')+'/'+xtpath+'/userRpm/SysRebootRpm.htm";')
    driver.switch_to.frame('mainFrame')
    driver.find_element(By.ID, 'reboot').click()
    ## Alert(driver).accept()
    print("Fin de ejecucion")
