from selenium import webdriver
from time import sleep
import unittest,requests

class Masands(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://masands_h5_test.fftechs.com:2086/#/lo/login")
    def tearDown(self):
        sleep(3)
        self.driver.quit()
    def test_login(self):
        a = self.driver.find_elements_by_class_name('van-field__control')[0].send_keys('hhs001')
        b = self.driver.find_elements_by_class_name('van-field__control')[1].send_keys('123456')
        self.driver.find_element_by_class_name('loginn').click()
        self.assertEqual("登录成功","登录成功",msg="failure")
        self.driver.save_screenshot('a.png')

if __name__ == '__main__':
    unittest.main()

        # data = {'username':'hhs001','password':'123456','type':'2'}
        # headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Mobile Safari/537.36'}
        # res = requests.post('http://masands_h5_test.fftechs.com:2086',data=data,headers = headers)