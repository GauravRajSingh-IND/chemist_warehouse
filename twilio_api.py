from twilio.rest import Client
from dotenv import load_dotenv
import os

class SendMessage:

    def __init__(self):

        load_dotenv()
        self.sid = os.getenv('account_sid')
        self.token = os.getenv('account_token')
        self.whatsapp_number = os.getenv('whatsapp_number')

        self.client = Client(self.sid, self.token)

    def send_product_offer(self, product_data:dict, to_number:str) -> dict :
        """
        This function take product data and send a whatsapp message to the user.
        :param product_data: data of product.
        :param to_number: customer whatsapp number
        :return: success or not in dictionary.
        """

        body = f"""
        🌹 *Special Offer on {product_data['name']}!* 🌹
        🐾 *Product Name:* {product_data['name']}
        💲 *Current Price:* {product_data['price_now']}
        💲 *Original Price:* {product_data['price_mrp']}
        🎉 *You Save:* {product_data['save']}

        📸 Check out the product below!
        {product_data['product_link']}
        🛒 Don't miss out on this amazing deal! Grab yours now!
        """

        to_number = f"whatsapp:{to_number}"
        try:
            self.client.messages.create(
                body= body,
                from_=self.whatsapp_number,
                to= to_number,
                media_url = product_data['image']
            )
            return {"success":True, "response":"message queued."}
        except:
            return {"success": False, "response": "error while sending message."}
