import time
from pages.homepage import HomePage
from pages.product import ProductPage

def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    #browser.get('https://www.demoblaze.com/')
    homepage.click_galaxy_s6()
    #galaxy_s6 = self.browser.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]')
    #galaxy_s6.click()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')

def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    #browser.get('https://www.demoblaze.com/')
    homepage.click_monitor()
    #monitor_link = self.browser.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
    #monitor_link.click()
    time.sleep(2)
    homepage.check_products_count(2)
    #monitors = browser.find_elements(By.CSS_SELECTOR, value='.card')
    #assert len(monitors) == 2





