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
        desired_caps['app'] = PATH('C:\APPTEST\ContactManager.apk')
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'



        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

    # 1.Otworz Contact Manager
    def test_form(self):
        el = self.driver.find_element_by_class_name('android.widget.Button')
        el.click()

        text_fields = self.driver.find_elements_by_class_name('android.widget.EditText')

        text_fields[0].send_keys("Ela")
        text_fields[1].send_keys("519771067")
        text_fields[2].send_keys("ela@gamil.com")

    # 2. Asercja
        el1 = self.assertEqual("Ela", text_fields[0].text)
        el2 = self.assertEqual("519771067", text_fields[1].text)
        el3 = self.assertEqual("ela@gamil.com", text_fields[2].text)

    #3. Button save

        button = self.driver.find_element_by_id('com.example.android.contactmanager:id/contactSaveButton')
        button.click()
   

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_android)
    unittest.TextTestRunner(verbosity=2).run(suite)