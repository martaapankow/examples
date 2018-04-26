#_*_ coding: utf-8 _*_
from selenium import webdriver
import unittest

"""
Sign up at website wizzair.com

Test case 01:
I Sign up (registration as a new user) using invalid email

Steps:
"1. Go to https://wizzair.com/pl-pl/main-page#/
2. Click ZALOGUJ SIĘ in the upper right corner 
3. Select REJESTRACJA
4. Enter name - Imię
5. Enter surname - Nazwisko
6. Select gender
7. Enter phone number
8. Enter invalid email (no @)
9. Enter password
10. Select country
11. Accept the privacy policy
12. Click button ZAREJESTRUJ SIĘ

The expected result:
The button ZAREJESTRUJ SIĘ is inactive
User receives message  NIEPRAWIDŁOWY ADRES EMAIL
"""

valid_name = "Jacek"
valid_surname = "Nowak"
telephone = "517707225"
invalid_email = "jaceknowak.gmail"
valid_password = "Marta777"

class wizzairRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#/")

    def test_invalid_email(self):
        driver = self.driver
        login_btn = driver.find_element_by_css_selector("#app > header > div.header__inner > div > nav > ul > li:nth-child(7) > button")
        login_btn.click()
        
        reg_btn = driver.find_element_by_xpath('//button[contains(text(), "Rejestracja")]')
        reg_btn.click()

        name = driver.find_element_by_xpath("//input[@placeholder='Imię']")
        name.send_keys(valid_name)

        surname = driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
        surname.send_keys(valid_surname)

        male = driver.find_element_by_id('register-gender-male')
        male.click()

        tel_n = driver.find_element_by_css_selector("input[type=tel]")
        tel_n.send_keys(telephone)

        
        mail = driver.find_element_by_css_selector('input[data-test=booking-register-email]')
        mail.send_keys(invalid_email)

        password = driver.find_element_by_css_selector('input[data-test=booking-register-password]')
        password.send_keys(valid_password)

        nationality1 = driver.find_element_by_css_selector('input[data-test=booking-register-country]')
        nationality1.click()

        nationality2 = driver.find_element_by_xpath('//*[@class="register-form__country-container__locations"]/Label[164]')
        nationality2.location_once_scrolled_into_view
        nationality2.click()
        

        acp_prv_policy = driver.find_element_by_xpath('//*[@id="registration-modal"]/form/div[2]/div[10]/span/label[1]')
        acp_prv_policy.click()

        error_notice = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[2]/span')
        print(error_notice.text)
        assert error_notice.is_displayed()
        self.assertEqual(error_notice.text, u"Nieprawidłowy adres e-mail")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
