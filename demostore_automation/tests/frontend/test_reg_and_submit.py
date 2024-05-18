from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options =   webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8888/Mysite2/')

#finding and clicking on the my account tab
my_acct = driver.find_element('css selector', '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-10 > a')
my_acct.click()

#getting the field email to type in an Email
u_name = driver.find_element('id', 'reg_email')
u_name.send_keys('Rasputin@gmail.com')

#getting the field password to type in a password
p_field = driver.find_element('id', 'reg_password')
p_field.send_keys('Mypassword1234!!') 

# selecting and clicking on the register button
reg_btn = driver.find_element('css selector', '#customer_login > div.u-column2.col-2 > form > p:nth-child(5) > button')
reg_btn.click()
