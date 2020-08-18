import unittest
from test import Baidu01

# 使用 TestLoader 将一个测试类中的所有测试文件都放入测试套件中
# 和 makeSuite() 不同的是, 每次使用一次 TestLoader(), 都会产生一个测试套件. 最终需要将这些测试套件全部集中到一个测试套件中
# suite = unittest.TestLoader.loadTestsFromTestCase(文件名.类名)

def createsuite():

    suite1 = unittest.TestLoader.loadTestsFromTestCase(Baidu01.Baidu1)
    suite2 = unittest.TestLoader.loadTestsFromTestCase(Baidu01.Baidu1)
    suite = unittest.TestSuite([suite1, suite2])
    return suite

if __name__ == "__main__":
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)