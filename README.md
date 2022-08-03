
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
- The module is powered ON connected to the hotspot using Bolt App.<br />
[![Circuit.jpg](https://i.postimg.cc/B6ddqCT1/Circuit.jpg)](https://postimg.cc/XGk2LdDV)

*The stable blue and green LED's symbolises that the module has proper cloud access, is connected to the hotspot and has power supply.*

(b) **Code**

- In the following block of code, I have imported important files like _json_ for converting python dictionary to json strings, _time_ to return the number of seconds passed since epoch and _conf_ is the file containing private api keys and tokens.<br />
[![import.jpg](https://i.postimg.cc/zvGRGnq8/import.jpg)](https://postimg.cc/KkCY93KH)
- Now to fetch the data from Bolt Cloud, I have created an object called 'bolt' using which we can access the data on Bolt.
- For the Bolt Cloud to identify our device, we will need to provide the API key and the Device ID when creating the mybolt object. Since the conf file holds the API key and Device ID variables, we can use them as follows:

The below code will automatically fetch one's SID, Authentication TOKEN, TO_NUM and FROM_NUM that one have initialized in conf.py file. 

<p align="center">
  <img width="200" src="https://user-images.githubusercontent.com/97796804/182668571-f809cec2-30d1-4072-8610-90c3afa73325.JPG">
</p>
- The inputs from the user:<br />
<p align="center">
  <img width="200" src="https://user-images.githubusercontent.com/97796804/182668548-fdc2e57e-b6e1-4819-8443-83e4873ee544.JPG">
</p>
- Below is the function definition to check the current market value of bitcoin and return it to the user.
<p align="center">
  <img width="200" src="https://user-images.githubusercontent.com/97796804/182668524-f0c1166f-e9ee-438a-9566-a12c68391201.JPG">
</p>
- The main code block incorporates the function price_check and checks the condition whether the current bitcoin market value is greater than the selling price entered by the user and gives the different user alerts.
<p align="center">
  <img width="200" src="https://user-images.githubusercontent.com/97796804/182668497-e6d29851-14a3-4060-9684-722503e89c04.JPG">
</p>

## Output
(I) **Output Window**

- Here, the user is asked to enter the corresponding country currency in which he/she wants to invest.<br />
<p align="center">
  <img width="200" src="https://user-images.githubusercontent.com/97796804/182668487-258bdb84-a63f-4478-ad03-e3d29b16c72b.JPG">
</p>

(II) **Buzzer**<br />
<p align="center">
  <img width="200" src="https://user-images.githubusercontent.com/97796804/182668461-49e497ad-6de2-463b-a8f8-cabf5fd96e5b.JPG">
</p>

(III) **SMS**<br />
<p align="center">
  <img width="200" src="https://user-images.githubusercontent.com/97796804/182668443-0a144be8-b899-4fe3-a136-6c63ce7ec571.jpg">
</p>

(IV) **Email**<br />
<p align="center">
  <img width="200" src="https://user-images.githubusercontent.com/97796804/182668418-c0c92d36-ece4-4fb3-8b3e-08821083c99e.JPG">
</p>

(V) **Telegram Bot**<br />
<p align="center">
  <img width="200" src="https://user-images.githubusercontent.com/97796804/182667532-db73c663-e242-4fcd-8e5a-745a4ef71f90.jpg">
</p>
