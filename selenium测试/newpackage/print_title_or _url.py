from selenium import webdriver
import time

driver = webdriver.Firefox()    # 获得驱动，打开浏览器
driver.get("https://www.baidu.com/")    # 打开百度网址

# 最大化浏览器
driver.maximize_window()

driver.find_element_by_id("kw").send_keys("朱一龙")
driver.find_element_by_id("su").submit()
time.sleep(5)

# 打印 title
title = driver.title;
print("title ="+title)
# 打印当前 URL
url = driver.current_url
print("url ="+url) 
time.sleep(6)

driver.quit()