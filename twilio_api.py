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

    def send_product_offer(self, product_data:str, to_number:str) -> dict :
        """
        This function take product data and send a whatsapp message to the user.
        :param product_data: data of product.
        :param to_number: customer whatsapp number
        :return: success or not in dictionary.
        """
        to_number = f"whatsapp:{to_number}"
        try:
            self.client.messages.create(
                body= product_data,
                from_=self.whatsapp_number,
                to= to_number
            )
            return {"success":True, "response":"message queued."}
        except:
            return {"success": False, "response": "error while sending message."}
