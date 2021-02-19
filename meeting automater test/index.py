from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver import ActionChains


ti = datetime.datetime.now()
ki = list(str(ti))
time_now = int("".join(ki[11:13]+ki[14:16]))
print(time_now)

def final(username='',password='',meeting_time=''):
    while True:
        if((time_now)-2==meeting_time):
            driver = webdriver.Chrome('F:\\chromedriver')
            driver.get("https://www.microsoft.com//en-in/microsoft-365//microsoft-teams//group-chat-software")
            print(driver.title)
            driver.maximize_window()
            time.sleep(5)
            a = driver.find_element_by_xpath('//a[@class="c-button f-secondary xs-ow-mt-10 m-ow-mt-30 ow-bvr-signin"]')
            a.click()
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(10)
            b = driver.switch_to_active_element()
            b.send_keys(username)
            b.send_keys(Keys.ENTER)
            time.sleep(10)
            c = driver.switch_to_active_element()
            c.send_keys(password)
            c.send_keys(Keys.ENTER)
            try:
                d = driver.find_element_by_xpath('//input[@id="idSIButton9"]')
                d.send_keys(Keys.ENTER)
            except:
                pass
            driver.implicitly_wait(30)
            action_chains.ActionChains.move_to_element_with_offset
            e = driver.find_element_by_xpath('//button[@aria-label="Calendar Toolbar"]')
            e.click()
            time.sleep(10)
            f = driver.find_element_by_xpath('//button[@aria-label="Join meeting"]').click()
            time.sleep(10)
            try:
                g = driver.find_element_by_xpath('//button[@class="ts-btn ts-btn-fluent ts-btn-fluent-secondary-alternate"]')
                g.click()
            except:
                pass
if __name__ == "__main__": 
    final() 
