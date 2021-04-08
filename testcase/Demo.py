import unittest
from selenium import webdriver

class demo(unittest.TestCase):

    def  testLogin(self):
        self.driver.find_element_by_css_selector().click()
    def testreg(self):
        print("'")
    def goiu(self):
        print()
    def tearDown(self):
        self.driver.close()

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("")
if __name__ == '__main__':
    unittest.main()