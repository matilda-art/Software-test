from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath("E:/课件/测试工具等/selenium2html/alert.html")
driver.get(file_path)

driver.maximize_window()
time.sleep(3)

driver.find_element_by_id("tooltip").click()
time.sleep()
# 得到操作 alter 框的句柄
alter = driver.switch_to.alert
# 关闭 alter 框
alter.accept()
time.sleep(3)
driver.quit()