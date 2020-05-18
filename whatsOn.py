from selenium import webdriver
import time
from datetime import datetime

url = 'https://web.whatsapp.com/'
choiceThePeople = ['Amor',]

def calcTime(total_segs, printScreen, calcTime=False):
    horas = total_segs // 3600
    dias = horas//86400
    segs_restantes = total_segs % 3600
    minutos = segs_restantes // 60
    segs_restantes_final = segs_restantes % 60
    if calcTime == True:
        print(f'Tempo de operação "{printScreen}" no whatsapp: {horas}hrs, {minutos}min, {segs_restantes_final}seg')
    else:
        print(f'Tempo "{printScreen}"   -   {horas}Horas  {minutos}Minutos {segs_restantes_final}Segundos')

class whatsappBot:
    def __init__(self):
        self.grupos = choiceThePeople
        self.chrome = webdriver.Chrome()
        data = datetime.now()
        print(f'Seu Script começou a ser rodado às {data}Horas')


    def seeStatus(self):
        self.chrome.get(url)
        time.sleep(20)
        for grupo in self.grupos:
            grupo = self.chrome.find_element_by_xpath(f"//span[@title='{grupo}']")
            grupo.click()
        timeOn=0
        timeOf=0


        while True:
            lastTime = 0
            check = self.chrome.find_elements_by_xpath("//span[contains(@class, 'O90ur _3FXB1')]")[0].text
            while check == 'online':
                check_if_online = self.chrome.find_elements_by_xpath("//span[contains(@class, 'O90ur _3FXB1')]")[0].text
                time.sleep(1)
                timeOn += 1
                lastTime += 1
                if check_if_online != 'online':
                    calcTime(timeOn, 'OnLine')
                    calcTime(lastTime, 'OnLine', True)
                    break

            while check != 'online':
                check_if_offline = self.chrome.find_elements_by_xpath("//span[contains(@class, 'O90ur _3FXB1')]")[0].text
                time.sleep(1)
                timeOf += 1
                lastTime += 1
                if check_if_offline == 'online':
                    calcTime(timeOf, 'OffLine')
                    calcTime(lastTime, 'OffLine', True)
                    break





whats = whatsappBot()
whats.seeStatus()
