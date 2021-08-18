from selenium.common.exceptions import NoSuchElementException
import smtplib, ssl
from email.mime.text import MIMEText

def acceptConsent(driver):
    def expand_shadow_element(element):
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root
    try:
        outer = expand_shadow_element(driver.find_element_by_css_selector("div#usercentrics-root"))
        inner = outer.find_element_by_css_selector("button[data-testid='uc-accept-all-button']")
        inner.click()
    except NoSuchElementException:
        pass

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