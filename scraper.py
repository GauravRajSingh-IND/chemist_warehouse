import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class CWScraper:

    def __init__(self):

        self.driver = webdriver.Chrome(options=chrome_options)
        self.product_link = None

        self.wait = WebDriverWait(self.driver, 10)

    # Helper function to retrieve element text or attribute
    def get_element_text(self, xpath, attribute=None):

        try:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return element.get_attribute(attribute) if attribute else element.text
        except Exception:
            return None  # Return None if the element is not found

    def product_data(self, product_url):

        self.product_link = product_url
        self.driver.get(url=self.product_link)

        # Define XPaths for product details
        xpaths = {
            'name': '//*[@id="Left-Content"]/div[4]/div/table/tbody/tr[3]/td[2]/div[2]/h1',
            'price_now': '//*[@id="p_lt_ctl10_pageplaceholder_p_lt_ctl00_wBR_P_D1_ctl00_ctl00_ctl00_ctl00_ctl04_lblActualPrice"]',
            'price_mrp': '//*[@id="p_lt_ctl10_pageplaceholder_p_lt_ctl00_wBR_P_D1_ctl00_ctl00_ctl00_ctl00_ctl04_lblOrignalPriceText"]',
            'save': '//*[@id="p_lt_ctl10_pageplaceholder_p_lt_ctl00_wBR_P_D1_ctl00_ctl00_ctl00_ctl00_ctl04_lblOffCategory"]',
            'image': '//*[@id="slider_pi_container"]/div/div/div[3]/div[2]/a/img',
            'product_id': '//*[@id="Left-Content"]/div[4]/div/table/tbody/tr[3]/td[2]/div[3]'
        }

        # Retrieve product details
        # Use the helper function to retrieve product details
        product_name = self.get_element_text(xpaths['name'])
        product_price_now = self.get_element_text(xpaths['price_now'])
        product_price_mrp = self.get_element_text(xpaths['price_mrp'])
        product_save = self.get_element_text(xpaths['save'])
        product_image = self.get_element_text(xpaths['image'], attribute='src')
        product_id = self.get_element_text(xpaths['product_id'])

        # Return structured data as a dictionary
        return {
            'name': product_name,
            'price_now': product_price_now,
            'price_mrp': product_price_mrp,
            'save': product_save,
            'image': product_image,
            'product_id': product_id
            }

    def quit(self):
        self.driver.quit()


scraper = CWScraper()
response = scraper.product_data(product_url="https://www.chemistwarehouse.com.au/buy/64065/qv-gentle-wash-1-25kg")
print(response)
scraper.quit()