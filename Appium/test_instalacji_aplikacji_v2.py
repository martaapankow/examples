import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class test_android(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('C:\APPTEST\ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        #appium server
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_if_app_installed(self):
        self.assertTrue(self.driver.is_app_installed('io.appium.android.apis'))

if __name__ == '__main__':
    suite = unittest.TestLoader().0loadTestsFromTestCase(test_android)
    unittest.TextTestRunner(verbosity=2).run(suite)