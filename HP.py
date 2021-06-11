from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import smtplib, ssl
from email.mime.text import MIMEText
driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver90.exe")
URL = "https://www.fischer.cz"
URL_faq = URL+"/faq"
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 1500)

def sendEmail(msg):
    fromx = 'alertserverproblem@gmail.com'
    to = 'ooo.kadoun@gmail.com'
    msg = MIMEText(msg)
    msg['Subject'] = "SRWEB1"
    msg['From'] = fromx
    msg['To'] = to

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login("alertserverproblem@gmail.com", "")
    server.sendmail(fromx, to, msg.as_string())
    server.quit()



def test_HomePage():
    driver.get(URL)
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

test_HomePage()