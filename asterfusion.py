#!/bin/python
import threading
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 

class Asterfusion:
    def __init__(self):
        self.webnet = ''
        self.chrome = webdriver.Chrome()
        #self.search_button_rule = '[data-ved="0ahUKEwjI9_rd64XrAhXwyosBHUNYCeoQ4dUDCAs"]'
        self.search_button_rule = '.FPdoLc.tfB0Bf  center .gNO89b'
    
    def start(self):
        self.chrome.get("https://www.google.com/")
        self.chrome.find_element_by_css_selector(".gLFyf.gsfi").send_keys("星融元数据技术有限公司")
        search_button = self.chrome.find_element_by_css_selector(self.search_button_rule)
        search_button.click()

    def SpiderIndex(self):
        


asterfusion = Asterfusion()
asterfusion.start()
