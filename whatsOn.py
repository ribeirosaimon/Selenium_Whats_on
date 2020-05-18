from selenium import webdriver
import time
from datetime import datetime


url = 'https://web.whatsapp.com/'
choiceThePeople = input('Digite o Nome exatamente igual ao whatsapp: ')


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


def validation(check):
    if check == []:
        check = 'Offline'
    elif check != 'online':
        check = 'offline'
    else:
        check = check[0].text
    return check


class whatsappBot:
    def __init__(self):
        self.grupos = choiceThePeople
        self.chrome = webdriver.Chrome()
        data = datetime.now()
        print(f'Seu Script começou a ser rodado às {data}Horas')


    def seeStatus(self):
        self.chrome.get(url)
        time.sleep(20)
        grupo = self.chrome.find_element_by_xpath(f"//span[@title='{choiceThePeople}']")
        grupo.click()
        time.sleep(5)
        timeOn=0
        timeOf=0


        while True:
            lastTime = 0
            check = self.chrome.find_elements_by_xpath("//span[contains(@class, 'O90ur _3FXB1')]")
            validation(check)
            while check == 'online':
                time.sleep(1)
                check_if_online = self.chrome.find_elements_by_xpath("//span[contains(@class, 'O90ur _3FXB1')]")
                check = validation(check_if_online)
                timeOn += 1
                lastTime += 1
                if check != 'online':
                    calcTime(timeOn, 'OnLine')
                    calcTime(lastTime, 'OnLine', True)
                    break
            while check != 'online':
                time.sleep(1)
                check_if_offline = self.chrome.find_elements_by_xpath("//span[contains(@class, 'O90ur _3FXB1')]")
                check = validation(check_if_offline)
                timeOf += 1
                lastTime += 1
                if check == 'online':
                    calcTime(timeOf, 'OffLine')
                    calcTime(lastTime, 'OffLine', True)
                    break


whats = whatsappBot()
whats.seeStatus()
