from selenium import webdriver
import time

driver = webdriver.Firefox()    # 获得驱动，打开浏览器
driver.get("https://www.baidu.com/")    # 打开百度网址

# 最大化浏览器
driver.maximize_window()
time.sleep(6)

# 用 id 来进行定位（只有 id 是唯一的
# driver.find_element_by_id("kw").send_keys("卡布叻船长")
# driver.find_element_by_id("su").click()

# 用 name 来定位,不是所有的元素都是有 name 属性的
# driver.find_element_by_name("wd").send_keys("盗墓笔记")
# driver.find_element_by_id("su").click()

# 用 class name 来定位, 定位失败, 因为 class name 中的内容有多个, 所以无法定位
# driver.find_element_by_class_name("s_ipt nobg_s_fm_hover").send_keys("朱一龙")
# driver.find_element_by_class_name("btn self-btn bg s_btn btn_h btnhover").click()

# 用 tag name 来定位, 定位失败, 因为使用 tag name 定位到的东西太多了, 无法区分是哪一个
# 只有想定位的属性是唯一的，才可以用 tag name 定位到
# driver.find_element_by_tag_name("input").send_keys("朱一龙")
# driver.find_element_by_id("su").click()


# 使用 链接/部分链接 进行定位的时候, 链接名一定要是唯一的

# 使用 link text 定位
# driver.find_element_by_link_text("视频").click()

# 使用 partial link text 定位： 通过链接的一部分进行查找
# driver.find_element_by_partial_link_text("频").click()

# 使用 xpath 定位：xpath 是一定可以定位到的
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("铁三角")
# driver.find_element_by_xpath("//*[@id='su']").click()

# 使用 css selecter 定位
# driver.find_element_by_css_selector("#kw").send_keys("瓶邪")
# driver.find_element_by_css_selector("#su").click()

# time.sleep(6)


# driver.find_element_by_name("wd").clear()
# time.sleep(3)
# driver.find_element_by_name("wd").send_keys("徐文组")

# 清除搜索内容“瓶邪”(clear)
# driver.find_element_by_name("wd").clear()
# time.sleep(3)

# 重新搜索“徐文组”
# driver.find_element_by_name("wd").send_keys(u"徐文组")

# 提交查询内容(submit)
# driver.find_element_by_id("su").submit()
# time.sleep(6)

# 输出定位元素的内容(test)
# test = driver.find_element_by_id("s-bottom-layer-right").text
# print("test = "+test)
# time.sleep(3)

driver.find_element_by_id("kw").send_keys("周深")
driver.find_element_by_id("su").submit()

# 智能等待(如果事件在给定时间内就完成了, 则可以马上执行下一步)
driver.implicitly_wait(10)
driver.find_element_by_link_text("周深_百度百科").click()
time.sleep()

driver.quit()