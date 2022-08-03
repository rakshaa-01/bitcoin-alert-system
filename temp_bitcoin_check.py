import conf_alerts, json, time, requests
from boltiot import Bolt,Sms,Email

mybolt = Bolt(conf_alerts.API_KEY, conf_alerts.DEVICE_ID)
sms = Sms(conf_alerts.SID, conf_alerts.AUTH_TOKEN, conf_alerts.TO_NUMBER, conf_alerts.FROM_NUMBER)
email = Email(conf_alerts.MAILGUN_API_KEY, conf_alerts.SANDBOX_URL, conf_alerts.SENDER_EMAIL, conf_alerts.RECIPIENT_EMAIL)

def get_bitcoin_price():
   try:
      URL = conf_alerts.URL
      response = requests.request("GET", URL)
      response = json.loads(response.text)
      current_price = response["INR"]
      return current_price
   except Exception as e:
      print("Error occured in finding the Bitcoin Price!")
      print(e)
def send_telegram_message(message):
    url = "https://api.telegram.org/" + conf_alerts.telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": conf_alerts.telegram_chat_id,
        "text": message
    }
    try:
        response = requests.request(
            "POST",
            url,
            params=data
        )
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("An error occurred in sending the alert message via Telegram")
        print(e)
        return False

while True:
   current_price = get_bitcoin_price()
   if current_price > conf_alerts.SP:
      # Alert using Buzzer
      print("Current Price = " + str(current_price) + " has exceeded the Selling Price = " + str(conf_alerts.SP) + "!")
      response1 = mybolt.digitalWrite(0,"HIGH")
      time.sleep(5)
      response1 = mybolt.digitalWrite(0,"LOW")
      # Alert using SMS
      response_sms = sms.send_sms("Current Price = " + str(current_price) + " has exceeded the Selling Price = " + str(conf_alerts.SP) + "!")
      print("Response received for SMS from server : " + str(response_sms))
      print("Status of SMS is : " + str(response_sms.status))
      # Alert using Email
      response_email = email.send_email("Alert for Bitcoin Price", "Current Price = " + str(current_price) + " has exceeded the Selling Price = " + str(conf_alerts.SP) + "!")
      response_email_text = json.loads(response_email.text)
      print("Response received for Email from server : " + str(response_email_text['message']))
      # Alert using Telegram
      telegram_message = "Current Price = " + str(current_price) + " has exceeded the Selling Price = " + str(conf_alerts.SP) + "!"
      telegram_status = send_telegram_message(telegram_message)
      print("Response recieved for 'Telegram Message' from Telegram : ", telegram_status)
   time.sleep(30)