# pyautogui-bruteforce
This script automates brute forcing a text field through the gui for sites that do not have an invalid credentials timeout response.

## Abstract
I needed a quick way to brute force flash login page. Didn't know what tool to use so wrote a python script using pyautogui.

## Situation
I noticed a company's website that uses flash was allowing me to enter in invalid credentials without timing out. So I set out to see if a brute force attack was possible. 

## Solution/Tools used
I initially tried to brute force through burp suite but it was having trouble parsing the AMF (Action Message Format) it was receiving. After a little bit of trying different things I settled on using pyautogui to manipulate the GUI. I figured it would be good enough for a proof of concept. My script runs through a password list, enters a password, hits the "ENTER" key, CTRL A (to select the previously entered word), enters next word until it runs through the whole list.

## After thoughts
In the end I was able to successfully brute force the login page without getting timed out or IP banned. I wrote a vulnerability report and notified the company.
Using pyautogui was good enough to get the job done in this situation but I'm sure there is a more efficient way to do this. Does anyone have suggestions for a way to brute force a flash site that sends AMF traffic? 

## INSTRUCTIONS:
1.	From a command prompt navigate into your new “Brooty” folder.
2.	From the Chrome or Internet Explorer web browser navigate to the site with the password text field you wish to brute force.
3.	Enter credentials into the “Username” field.
4.	From the command prompt type “brooty.py”.
5.	Press “OK” on popup.
6.	Click in “Password” field.
7.	After 5 seconds the script will enter in passwords until it runs through the full list.
8. It runs through these passwords at about 3 words a second. So it will run through the provided 6250 words in about 35 minutes.
9.	If you want to end the scripts before it is done with the password list click in the command prompt and press “CTRL C” until it exits.

Note 1: The program will keep running through CTRL A, enter password, press enter, commands if you click somewhere else on the screen so be careful.

Note 2: You can also open up a notepad and let the program run in there to see what it is doing.
