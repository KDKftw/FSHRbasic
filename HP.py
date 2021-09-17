from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import smtplib, ssl
from email.mime.text import MIMEText
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from import_this import acceptConsent, sendEmail
##driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver92.exe")
from threading import Thread


from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
URL = "https://www.eximtours.cz"
URL_faq = URL+"/faq"
from selenium.webdriver.support import expected_conditions as EC
from to_import_secret import sendEmail, comandExecutor

caps=[{
      'os_version': 'Mavericks',
      'os': 'OS X',
      'browser': 'safari',
      'browser_version': '7.1',
      'name': 'Parallel Test1', # test name
      'build': 'browserstack-build-1' # Your tests will be organized within this build
      },
      {
      'os_version': '10',
      'os': 'Windows',
      'browser': 'ie',
      'browser_version': '11.0',
      'name': 'Parallel Test2',
      'build': 'browserstack-build-1'
      },
      {
      'os_version': 'Big Sur',
      'os': 'OS X',
      'browser': 'safari',
      'browser_version': 'latest',
      'name': 'Parallel Test3',
      'build': 'browserstack-build-1'
}]

def HomePage(desired_cap):
    driver = webdriver.Remote(
        command_executor=comandExecutor,
        desired_capabilities=desired_cap)
    wait = WebDriverWait(driver, 1500)
    driver.get(URL)
    time.sleep(2.5)
    acceptConsent(driver)
    try:
        bannerSingle = driver.find_element_by_xpath("//*[@class='f_teaser-item']")
        bannerAll = driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
        wait.until(EC.visibility_of(bannerSingle))
        if bannerSingle.is_displayed():
            for WebElement in bannerAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass
                else:
                    url = driver.current_url
                    msg = "Problem na HP s bannery " + url
                    sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem na HP s bannery " + url
        sendEmail(msg)

    time.sleep(1.5)

    try:
        nejnabidkyLMsingle = driver.find_element_by_xpath("//*[@class='fshr-lm-table-item-content']")
        nejnabidkyLMall = driver.find_elements_by_xpath("//*[@class='fshr-lm-table-item-content']")
        wait.until(EC.visibility_of(nejnabidkyLMsingle))
        if nejnabidkyLMsingle.is_displayed():
            for WebElement in nejnabidkyLMall:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass

                else:
                    url = driver.current_url
                    msg = "Problem na HP s nej. nabidky LM " + url
                    sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem na HP s nej. nabidky LM " + url
        sendEmail(msg)

    driver.get(URL_faq)

    try:
        faqSingle = driver.find_element_by_xpath("//*[@class='f_faq-item']")
        faqAll = driver.find_elements_by_xpath("//*[@class='f_faq-item']")
        if faqSingle.is_displayed():
            for WebElement in faqAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass
        else:
            url = driver.current_url
            msg = "Problem FAQ " + url
            sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem FAQ " + url
        sendEmail(msg)



    driver.quit()

for cap in caps:
        Thread(target=HomePage, args=(cap,)).start()