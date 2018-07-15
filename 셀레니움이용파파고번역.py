from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver')
driver.get('https://papago.naver.com/')
f = open('titleList.txt','r')
lines = f.readlines()
for line in lines:
    inputArea = driver.find_element_by_xpath('//*[@id="txtSource"]')
    inputArea.click()
    inputArea.clear()
    inputArea.send_keys(line.strip())
    driver.find_element_by_xpath('//*[@id="btnTranslate"]').click()
    time.sleep(3)
    print(driver.find_element_by_xpath('//*[@id="txtTarget"]').text)