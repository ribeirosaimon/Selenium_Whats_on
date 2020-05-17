from selenium import webdriver
import time
from datetime import datetime

url = 'https://web.whatsapp.com/'



class whatsappBot:
    def __init__(self):
        self.grupos = ['Amor',]
        self.chrome = webdriver.Chrome()
        print('Bom dia!, seu script começou a ser rodado as {}horas')


    def seeStatus(self):
        self.chrome.get(url)
        time.sleep(20)
        for grupo in self.grupos:
            grupo = self.chrome.find_element_by_xpath(f"//span[@title='{grupo}']")
            grupo.click()
        online = False
        while True:
            check_if_online = self.chrome.find_elements_by_xpath("//span[contains(@class, 'O90ur _3FXB1')]")[0].text
            while check_if_online != 'online':
                online=True
                time.sleep(1)
                print('True')
            print('saiu do loop')
            while check_if_online != 'online':
                online=False
                time.sleep(1)
                print('False')
            print('saiu do loop')




whats = whatsappBot()
whats.seeStatus()
