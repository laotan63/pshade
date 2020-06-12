import unittest
from selenium import webdriver
from time import sleep
class Amjs(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        res = driver.get('http://masands_h5_test.fftechs.com:2086')


    def tearDown(self):

