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


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

    #1.Otworz pasek powiadomien
    def test_notifications(self):
        self.driver.open_notifications()

    #2. Lokalizowanie elementow i porownanie
        els = self.driver.find_elements_by_class_name('android.widget.TextView')

        title = False
        body = False

        for el in els:
            print el
            text = el.text
            if text == 'USB debugging connected':
                title = True
            elif text == 'Tap to disable USB debugging.':
                body = True
    #3. Sprawdzanie asercji
        self.assertTrue(title)
        self.assertTrue(body)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_android)
    unittest.TextTestRunner(verbosity=2).run(suite)