from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()

options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('disable-infobars')
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"')

browser = webdriver.Chrome(chrome_options=options)
url = "https://www.amazon.cn/"
browser.get(url)

sleep(3)
browser.find_element_by_link_text('免费注册').click()
sleep(5)
browser.find_element_by_id('ap_customer_name').send_keys('dasjkdhaiwdsjhd')
sleep(1)
browser.find_element_by_id('ap_phone_number').send_keys('18000000000')
sleep(1)
browser.find_element_by_id('ap_email').send_keys('1234567@qq.com')
sleep(1)
browser.find_element_by_id('ap_password').send_keys('123456')
sleep(1)
browser.find_element_by_name('legalAgreementCheckBox').click()
sleep(1)







