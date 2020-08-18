import unittest
from test import Baidu01

# 使用 makeSuite() 将测试方法加到测试套件中
# makeSuite() 可以把 一个测试类中的所有测试方法 都 加入到测试套件中
# suite. addTest(unittest.makeSuite(文件名.类名))

def createsuite():

    suite = unittest.TestSuite()

    # 使用 makeSuit() 将 一个类中的所有测试用例加入到测试套件 suit 中
    suite.addTest(unittest.makeSuite(Baidu01.Baidu1))
    suite.addTest(unittest.makeSuite(Baidu01.Baidu1))
    return suite

if __name__ == "__main__":
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)