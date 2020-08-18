from selenium import webdriver
import time
import os


# div 模块定位
# 如果页面有多个div，需要定位的元素在某一个div里，可以优先定位这个div，在此基础上再定位该元素
driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("E:\\课件\\测试工具等\\selenium2html\\modal.html")
driver.get(file_path)
driver.maximize_window()
time.sleep(3)

# 点击主页的 click
driver.find_element_by_id("show_modal").click()
time.sleep(3)

# 点击 click me
div1 = driver.find_element_by_class_name("modal-body")
div1.find_element_by_link_text("click me").click()
time.sleep(3)

# 定位 close
div2 = driver.find_element_by_class_name("modal-footer")
buttons = div2.find_element_by_tag_name("button")
time.sleep(3)
buttons[0].click()
time.sleep(3)

driver.quit()