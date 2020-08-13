from selenium import webdriver
import time
import os

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath("E:/课件/测试工具等/selenium2html/checkbox.html")
driver.get(file_path)

driver.maximize_window()
time.sleep(3)

# 多层框架的定位
# switch_to.fream : 跳转到指定的 ifream
# switch_to.default_content() 跳转到默认页面

# 在进行跳转的时候, 不能跨越层级关系进行跳转, 只能一层一层的进行跳转
# driver.switch_to.frame("f2")
# driver.find_element_by_id("kw").send_keys(u"长白山")
# driver.find_element_by_id("su").click()

# 从默认的页面跳转到 id=f2的页面
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys(u"长白山")
driver.find_element_by_id("su").submit()
time.sleep(3)

# 跳转到默认页面
# 如果想从最里面的界面到外面一层的界面是无法做到的, 只能先回到默认界面中, 然后再进行界面的跳转
driver.switch_to.default_content()
driver.switch_to.frame("f1")
driver.find_element_by_link_text("click").click()
time.sleep(3)

driver.quit()