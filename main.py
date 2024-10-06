from scraper import CWScraper
from twilio_api import SendMessage
# create a CWS_scraper object.
scraper = CWScraper()

# scrape a product data.
product_data = scraper.product_data(product_url="https://www.chemistwarehouse.com.au/buy/75082/rose-hip-vital-canine-500g")
print(product_data)
scraper.quit()

# Send message to user.
message = SendMessage()
message.send_product_offer(product_data=product_data, to_number="+61449932325")


