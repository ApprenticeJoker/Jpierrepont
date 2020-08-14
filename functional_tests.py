from selenium import webdriver
import unittest

class GraduateEmployerTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/Users/Jake/Desktop/Jpierrepont/chromedriver.exe')
        
    def tearDown(self):
        self.browser.quit()

    def test_can_open_and_view_cv(self):
        #A potential employer is looking for information about me and finds my website    
        self.browser.get('http://jpierrepont.pythonanywhere.com/')

        #They fist see the main page of my site, the page is Titled "Jake's blog"
        self.assertIn('blog', self.browser.title)  
        self.fail('Finish the test!')

        #They are then able to navigate to the page on my site which holds my cv

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  