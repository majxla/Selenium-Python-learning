import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class PythonGuruTests(unittest.TestCase):
    

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_settings_values.cookies": 2,
            "profile.block_third_party_cookies": False
            })
        self.driver = webdriver.Chrome(options=chrome_options)
    
    def test_title(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/telecom/index.html")
        print(self.user_id)

        self.assertIn("Guru99 Telecom", driver.title)
    
    def test_add_customer_reset_form(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/telecom/index.html")

        add_customer_link = driver.find_element(By.LINK_TEXT, "Add Customer")
        add_customer_link.click()
        assert driver.title == 'Guru99 Telecom Add Customer'

        fname = driver.find_element(By.ID, "fname")
        fname.send_keys("name")
        lname = driver.find_element(By.ID, "lname")
        lname.send_keys("last name")
        email = driver.find_element(By.ID, "email")
        email.send_keys('fname_lname@example.com')

        assert email.get_attribute("value") != fname.get_attribute("value") != lname.get_attribute("value") != ''

        reset = driver.find_element(By.XPATH, "//input[@value='Reset']")
        driver.execute_script("arguments[0].click();", reset)

        assert email.get_attribute("value") == fname.get_attribute("value") == lname.get_attribute("value") == ''
    
    def test_add_customer_submit_empty_form(self):
        
        driver = self.driver
        driver.get("https://demo.guru99.com/telecom/index.html")

        add_customer_link = driver.find_element(By.LINK_TEXT, "Add Customer")
        add_customer_link.click()
        assert driver.title == 'Guru99 Telecom Add Customer'

        submit = driver.find_element(By.XPATH, "//input[@name='submit']")
        driver.execute_script("arguments[0].click();", submit)

        alert = driver.switch_to.alert
        assert alert.text == "please fill all fields"
        alert.accept()
    
    def test_add_customer_enter_invalid_email(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/telecom/index.html")

        add_customer_link = driver.find_element(By.LINK_TEXT, "Add Customer")
        add_customer_link.click()
        assert driver.title == 'Guru99 Telecom Add Customer'

        email = driver.find_element(By.ID, "email")
        email.send_keys('email')

        warning_message = driver.find_element(By.ID, "message9")
        assert warning_message.text == "Email-ID is not valid"


    def test_add_customer_enter_invalid_mobile(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/telecom/index.html")

        add_customer_link = driver.find_element(By.LINK_TEXT, "Add Customer")
        add_customer_link.click()
        assert driver.title == 'Guru99 Telecom Add Customer'

        mobile = driver.find_element(By.ID, "telephoneno")
        mobile.send_keys("abcdefgh")

        warning_message = driver.find_element(By.ID, "message7")
        assert warning_message.text == "Characters are not allowed"


    def test_add_customer_success(self):
        # Test Add Customer
        driver = self.driver
        driver.get("https://demo.guru99.com/telecom/index.html")

        add_customer_link = driver.find_element(By.LINK_TEXT, "Add Customer")
        add_customer_link.click()
        assert driver.title == 'Guru99 Telecom Add Customer'

        bg_done = driver.find_element(By.XPATH, "//input[@id='done']")
        driver.execute_script("arguments[0].checked = true;", bg_done)
        fname = driver.find_element(By.ID, "fname")
        fname.send_keys("name")
        lname = driver.find_element(By.ID, "lname")
        lname.send_keys("last name")
        email = driver.find_element(By.ID, "email")
        email.send_keys('fname_lname@example.com')
        address = driver.find_element(By.TAG_NAME, "textarea")
        address.send_keys("address line 1")
        mobile = driver.find_element(By.ID, "telephoneno")
        mobile.send_keys("123456789")

        submit = driver.find_element(By.XPATH, "//input[@name='submit']")
        driver.execute_script("arguments[0].click();", submit)

        access_id = driver.find_element(By.TAG_NAME, "h3")
        assert access_id.text != None


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

    