from selenium import webdriver
import time

url = 'https://web.whatsapp.com/'



class whatsappBot:
    def __init__(self):
        self.grupos = ['Amor',]
        self.chrome = webdriver.Chrome()


    def seeStatus(self):
        self.chrome.get(url)
        time.sleep(10)
        for grupo in self.grupos:
            grupo = self.chrome.find_element_by_xpath(f"//span[@title='{grupo}']")
            grupo.click()
            time.sleep(5)
            secOn = 0
            minOn = 0
            hrOn = 0
            secOff = 0
            minOff = 0
            hrOff = 0

            while True:
                resultado = self.chrome.find_elements_by_xpath("//span[contains(@class, 'O90ur _3FXB1')]")[0].text
                if resultado == 'online':
                    time.sleep(1)
                    secOn += 1
                    if secOn == 60:
                        minOn +=1
                        secOn = 0
                        if minOn == 60:
                            hrOn +=1
                            minOn=0
                    print(f'{hrOn}h:{minOn}m:{secOn}s Online')
                else:
                    time.sleep(1)
                    secOff += 1
                    if secOff == 60:
                        minOff +=1
                        secOff=0
                        if minOff == 60:
                            hrOff +=1
                            minOff=0
                    print(f'{hrOff}h:{minOff}m:{secOff}s Offline')
whats = whatsappBot()
whats.seeStatus()
