from selenium import webdriver
import unittest
import time

class GraduateEmployerTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/Users/Jake/Desktop/Jpierrepont/chromedriver.exe')
        
    def tearDown(self):
        self.browser.quit()

    def test_can_open_and_view_cv(self):
        #A potential employer is looking for information about me and finds my website    
        self.browser.get('http://jpierrepont.pythonanywhere.com/')
        time.sleep(3)

        #They fist see the home page of my site, the page is Titled "Home", and the header welcomes them to the site
        self.assertIn('Home', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome to my Site!', header_text)

        #They are then able to navigate to the page on my site which holds my cv
        hyperlink = self.browser.find_element_by_id('cv_link')
        self.assertEqual(
            hyperlink.get_attribute('href'),
            'http://jpierrepont.pythonanywhere.com/cv'
        )
        self.browser.get('http://jpierrepont.pythonanywhere.com/cv')
        time.sleep(3)
        self.assertIn('CV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('CV', header_text)

        #There they find my email and my career info
        secondary_header = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Background', secondary_header)

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  