from selenium import webdriver
import unittest
import time
from ddt import ddt, unpack, data, file_data
import sys, csv

# 数据驱动

# 1. 传入多组数据，一组数据有一个：@data
# 2. 传入多组数据，每组数据有两个以上的数据：@data  @unpack
# 3. 如何读取一个文件(txt,csv)中的数据：@data(方法)  @unpack
# 4. 如何读取一个json文件中的数据：@file_data


# 读取 txt 文件中的方法
def getCsv(file_name):
    rows=[]
    path=sys.path[1]

    with open(path+'\\data\\'+file_name, 'rt', encoding='UTF-8') as f:
        readers = csv.reader(f, delimiter=',', quotechar='|')
        next(readers, None)
        for row in readers:
            # [周迅，周迅_百度搜索]
            temprows=[]
            for i in row:
                temprows.append(i)
            rows.append(temprows)
        return rows

@ddt
class Baidu1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.driver.maximize_window()
        self.verificationErrors=[]
        self.accept_next_alert = True
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


    @file_data('test_baidu_data.json')
    # @data(*getCsv('test_baidu_data.txt'))
    # ([周迅,周迅_百度搜索],[张国荣,张国荣_百度搜索],[朱一龙,朱一龙_百度搜索])
    @unpack
    # @data("朱一龙", "罗云熙", "黄敏捷", "严屹宽")
    def test_baidu1(self, value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(3)
        # self.assertEqual(driver.title, expected_value, msg="和预期搜索结果不一致！")
        time.sleep(3)


    @unittest.skip("skipping")
    @data(["Lisa", u"Lisa_百度搜索"], [u"朱一龙", u"朱一龙_百度搜索"], ["999", u"999_百度搜索"])
    @unpack
    def test_baidu2(self, value, expected_value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear() # 清理工作，可没有
        driver.find_element_by_id("kw").send_keys(value) # 定位input输入框
        driver.find_element_by_id("su").click() # 点击百度一下
        driver.maximize_window()
        time.sleep(3)
        # 判断搜索网页的title和我们期望的是否一致
        self.assertEqual(expected_value, driver.title, msg="和预期搜索结果不一致！")
        print(expected_value)
        print(driver.title)
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()