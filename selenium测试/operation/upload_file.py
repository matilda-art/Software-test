from selenium import webdriver
import time
import os

# 上传文件操作
driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("E:\\课件\\测试工具等\\selenium2html\\upload.html")
driver.get(file_path)
time.sleep(3)

# 定位上传文件按钮

driver.find_element_by_tag_name("file").send_keys("E:\\课件\\测试工具等\\selenium2html\\upload.html")
time.sleep(3)

driver.quit()