
# Bitcoin Price Alerting System | Bolt IoT

An alert system which gives an alert message via Buzzer, SMS, Email and Telegram Bot whenever current bitcoin value has exceeded the specified threshold value.

## Components
Hardware Components:
 - Bolt Wifi Module
 - Buzzer
 - LED
 - Breadboard
 - Jumper Wires
 - Resistor (10kΩ)

 Software apps & Online Services:
 - Bolt Cloud
 - Twilio SMS Messaging API
 - Mailgun Email API
 - Telegram API
 - Ubuntu
## Purpose of Project

Bitcoin lets us exchange money in a non traditional way and falls under the category of digital currency. The price of a bitcoin varies unpredictably and thus can increase or decrease in a short period of time.

This project lets one track the ever fluctuating bitcoin prices in the currency suitable to the user. There is no need to check the website time and again for bitcoin prices, as the user will be notified whenever there is an increase or decrease in the bitcoin market price with respect to the price specified by the user.


## Setup & Code
(a) **Circuit**

- The postive pins of buzzer is connected to pin 1 of the module and LED is connected to pin 0 of the module and their negative pins are connected to GND.
- The module is powered ON connected to the hotspot using Bolt App.
[![Circuit.jpg](https://i.postimg.cc/B6ddqCT1/Circuit.jpg)](https://postimg.cc/XGk2LdDV)

*The stable blue and green LED's symbolises that the module has proper cloud access, is connected to the hotspot and has power supply.*

(b) **Code**

- In the following block of code, I have imported important files like _json_ for converting python dictionary to json strings, _time_ to return the number of seconds passed since epoch and _conf_ is the file containing private api keys and tokens.
[![import.jpg](https://i.postimg.cc/zvGRGnq8/import.jpg)](https://postimg.cc/KkCY93KH)
- Now to fetch the data from Bolt Cloud, I have created an object called 'bolt' using which we can access the data on Bolt.
- For the Bolt Cloud to identify our device, we will need to provide the API key and the Device ID when creating the mybolt object. Since the conf file holds the API key and Device ID variables, we can use them as follows:

The below code will automatically fetch one's SID, Authentication TOKEN, TO_NUM and FROM_NUM that one have initialized in conf.py file. 

[![credentials.jpg](https://i.postimg.cc/Fz61F8PV/credentials.jpg)](https://postimg.cc/gLvGNSbx)
- The inputs from the user:
[![Input.jpg](https://i.postimg.cc/Kc1MwDpD/Input.jpg)](https://postimg.cc/z31vRKry)
- Below is the function definition to check the current market value of bitcoin and return it to the user.
[![function.jpg](https://i.postimg.cc/cCG0DW5j/function.jpg)](https://postimg.cc/JDxfnf8c)
- The main code block incorporates the function price_check and checks the condition whether the current bitcoin market value is greater than the selling price entered by the user and gives the different user alerts.
[![main.jpg](https://i.postimg.cc/y6hHVwG1/main.jpg)](https://postimg.cc/Jthgxdmv)

## Output
(I) **Output Window**

- Here, the user is asked to enter the corresponding country currency in which he/she wants to invest.
[![out1.jpg](https://i.postimg.cc/TYXHP1DF/out1.jpg)](https://postimg.cc/Z0VL7Tjx)

(II) **Buzzer**
[![Hardware-connection.jpg](https://i.postimg.cc/yYch5LLZ/Hardware-connection.jpg)](https://postimg.cc/JG7BH5Vr)

(III) **SMS**
[![SMS-alert.jpg](https://i.postimg.cc/mD72R1J8/SMS-alert.jpg)](https://postimg.cc/KkvyDjZM)

(IV) **Email**
[![Email-Alert.jpg](https://i.postimg.cc/Qthv9BV6/Email-Alert.jpg)](https://postimg.cc/qtD1Wvsn)

(V) **Telegram Bot**
[![Telegram-Alert.jpg](https://i.postimg.cc/ydxXbBG1/Telegram-Alert.jpg)](https://postimg.cc/dkMy7Mvp)
