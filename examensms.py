from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_argument("start-maximized");
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(r"votrecheminc\chromedriver.exe",chrome_options=options)
driver.get("https://cas.umontpellier.fr/cas/login")
    

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
execution = driver.find_element_by_name("execution")
geolocation = driver.find_element_by_name("geolocation")
_eventId = driver.find_element_by_name("_eventId")
submit = driver.find_element_by_name("submit")


username.send_keys("adressemail")
password.send_keys("motdepasseent")


time.sleep(7)#7 before

submit.click()


driver.get("https://app.umontpellier.fr/mdw/#!notesView")

time.sleep(5)#5b4

reee= driver.find_elements_by_xpath('//span[text()="Notes & résultats"]')
print(reee)
reee[0].click()
time.sleep(5)#10b4




eeeeeeeeeeee= driver.find_elements_by_xpath('//span[text()="M1 Physique Numérique"]')



driver.execute_script("arguments[0].click();", eeeeeeeeeeee[0]) 
time.sleep(5)#5b4

dddddd= driver.find_elements_by_xpath('//span[text()="Fermer"]')

driver.execute_script("arguments[0].click();", dddddd[0]) 

time.sleep(5)#5b4

from bs4 import BeautifulSoup

soup = BeautifulSoup(driver.page_source,features="lxml")

result = soup.find_all("div", {"class":"v-label v-widget v-has-width"})
apartirdela=0
thesms=""
for res in result:
    if res.text=="S1 Physique Numérique":
        apartirdela=1
    if apartirdela==1 and ("/" in res.text):
        print(res.text)
        thesms+=res.text
        thesms+=" | "
    



from twilio.rest import Client


try:
    f = open(r"votrecheminc\marks.txt", "r")
    a=f.read()
    if a==thesms:
        print("do nada")
        f.close()
    else:
        print("do something")
        f.close()
        f = open(r"votrecheminc\marks.txt", "w")
        f.write(thesms)
        f.close()

        account_sid = 'sidtwilio'
        auth_token = 'tokentwilio'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                 body=thesms,
                 from_='+numerotwilio',
                 to='+votrenumero'
             )

except:

    f = open(r"votrecheminc\marks.txt", "w")
    f.write(thesms)
    f.close()

    account_sid = 'sidtwilio'
    auth_token = 'tokentwilio'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body=thesms,
             from_='+numerotwilio',
             to='+votrenumero'
         )



time.sleep(12)
driver.quit()
