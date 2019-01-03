                                        #import required modules
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
waittime=0.5
float(waittime)
def check_exists_by_xpath(xpath):
                                        #function to check if web element has loaded 
    
    try:
        driver.find_element_by_xpath(xpath)
        
    except NoSuchElementException:
        print('Tooo slow, waiting for website....')
        global waittime
        print('total time spent waiting:{wait} seconds'.format(wait=waittime))
        waittime=waittime+0.5
        return False
    
    return True
def waitloop(xp):
                                        #function to wait while web element loads(max 5 second, then program stops)
    if not check_exists_by_xpath(xp):
            time.sleep(0.5)
    if not check_exists_by_xpath(xp):
            time.sleep(0.5)
    if not check_exists_by_xpath(xp):
            time.sleep(0.5)
    if not check_exists_by_xpath(xp):
            time.sleep(0.5)
    if not check_exists_by_xpath(xp):
            time.sleep(0.5)
    if not check_exists_by_xpath(xp):
            time.sleep(0.5)
    if not check_exists_by_xpath(xp):
            time.sleep(0.5)
    if not check_exists_by_xpath(xp):
            time.sleep(0.5)
    if not check_exists_by_xpath(xp):
            time.sleep(0.5)
    if not check_exists_by_xpath(xp):
            time.sleep(0.5)






names = []
emails = []
 
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    
 
    rowNr = 0
    for row in reader:
        if rowNr >= 0:
            names.append(row[0])
            emails.append(row[1])
 
        rowNr = rowNr + 1
 
print(names)
print(emails)
with open('data.csv',"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)

print('no if rows={rows}'.format(rows=row_count))






id1='email@address'           #enter your email id here
passwd='password'                  #enter your password here
driver = webdriver.Chrome()
driver.get('https://www.gmail.com')
xp1=('//*[@id="identifierId"]')
waitloop(xp1)
id_field=driver.find_element_by_xpath('//*[@id="identifierId"]')
id_field.click()
id_field.send_keys(id1)
xp2=('//*[@id="identifierNext"]/content')
waitloop(xp2)
next_button1=driver.find_element_by_xpath('//*[@id="identifierNext"]/content')
next_button1.click()
xp3=('//*[@id="password"]/div[1]/div/div[1]/input')
waitloop(xp3)
pass_field=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
pass_field.click()
pass_field.send_keys(passwd)
next_button2=driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
next_button2.click()

#uncomment the following double hashed lines if program stops and  gmail opens account recovery page before inbox

##xp4=('//*[@id="yDmH0d"]/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div/content/span')
##waitloop(xp4)
##done_button=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div/content/span')
##done_button.click()
x=0
while x<=row_count:
    
    idd=emails[x]
    #idd=id1
    subj='Job Application'
    naaam=names[x]
    print(emails[x],names[x])

    application=("""
    Dear {naam},
    ###enter your message here###""".format(naam=naaam))

    
    xp5=('//*[@id=":k9"]/div/div')
    waitloop(xp5)
    compose_button=driver.find_element_by_xpath('//*[@id=":k9"]/div/div')
    compose_button.click()

    xp6=('//*[@aria-label="To"]')
    waitloop(xp6)
    to_field=driver.find_element_by_xpath('//*[@aria-label="To"]')
    to_field.click()
    to_field.send_keys(idd)
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    subject_field=driver.find_element_by_xpath('//*[@aria-label="Subject"]')
    subject_field.click()
    subject_field.send_keys(subj)
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    msgbody_field=driver.find_elements_by_xpath('//*[@aria-label="Message Body"]')
    msgbody_field[1].click()
    msgbody_field[1].send_keys(application)
    time.sleep(5)

    ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.ENTER).key_up(Keys.CONTROL).key_up(Keys.ENTER).perform()
    x=x+1
