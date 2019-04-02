from appium import webdriver

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='4.4.2'
desired_caps['deviceName']='hwPE'
desired_caps['appPackage']='com.tal.kaoyan'
desired_caps['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'
desired_caps['noReset']='true'

# desired_caps['app']=r'F:\apk\kaoyan3.1.0.apk'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

# # 等待启动
driver.implicitly_wait(5)
# # 点击取消

try:
    assert driver.find_element_by_id('android:id/button2').click()
    assert driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
except:
    print('按钮不存在')


#  用户名
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext ').send_keys('')
#  密码
driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext ').send_keys('')






