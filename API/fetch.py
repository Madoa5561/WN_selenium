from selenium import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
import urllib.request, urllib.error
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless=new")
options.add_argument('--log-level=200')
LOGGER.setLevel(logging.CRITICAL)
user_ag='MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; '+'CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
options.add_argument('user-agent=%s'%user_ag)

class weatherAPI():
    def __init__(self, url):
        self.url = url

    def url_check(self):
        try:
            f = urllib.request.urlopen(self.url)
            print ("success" + self.url )
            f.close()
        except:
            raise "NotFound URL Please enter a valid URL"

    def fetch_temperature(self):
        """温度を取得 (℃)"""
        try:
            driver = webdriver.Chrome(options=options)
            driver.get(self.url)
            driver.implicitly_wait(10)
            temperature = driver.find_element(By.XPATH, "/html/body/article[2]/article[1]/section[4]/div[2]/div/table/tbody/tr/td[1]/text()").text
            driver.quit()
            return temperature
        except:
            pass

    def fetch_humidity(self):
        """湿度を取得 (%)"""
        try:
            driver = webdriver.Chrome(options=options)
            driver.get(self.url)
            driver.implicitly_wait(10)
            humidity = driver.find_element(By.XPATH, "/html/body/article[2]/article[1]/section[4]/div[2]/div/table/tbody/tr/td[2]/text()").text
            driver.quit()
            return humidity
        except:
            pass
    
    def fetch_AtmosphericPressure(self):
        """気圧を取得 hPa"""
        try:
            driver = webdriver.Chrome(options=options)
            driver.get(self.url)
            driver.implicitly_wait(10)
            Pressure = driver.find_element(By.XPATH, "/html/body/article[2]/article[1]/section[4]/div[2]/div/table/tbody/tr/td[3]/text()").text
            driver.quit()
            return Pressure
        except:
            pass

    def fetch_wind(self):
        """風を取得
        
        return example [北東,2.8m/s]"""
        try:
            driver = webdriver.Chrome(options=options)
            driver.get(self.url)
            driver.implicitly_wait(10)
            wind_Direction = driver.find_element(By.XPATH, "/html/body/article[2]/article[1]/section[4]/div[2]/div/table/tbody/tr/td[4]/span[1]").text
            wind_Speed = driver.find_element(By.XPATH, "/html/body/article[2]/article[1]/section[4]/div[2]/div/table/tbody/tr/td[4]/text()").text
            driver.quit()
            return [wind_Direction,wind_Speed]
        except:
            pass

    def fetch_weather(self):
        """天気を取得
        
        return example [北東,2.8m/s]"""
        try:
            driver = webdriver.Chrome(options=options)
            driver.get(self.url)
            driver.implicitly_wait(10)
            weather = driver.find_element(By.XPATH, "/html/body/article[2]/article[1]/section[4]/div[2]/figure/figcaption").text
            driver.quit()
            return weather
        except:
            pass
