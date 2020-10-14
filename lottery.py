#!/bin/python3

import requests
import re
from bs4 import BeautifulSoup

res  = requests.get('http://www.taiwanlottery.com.tw/index_new.aspx')
soup = BeautifulSoup(res.text,'html.parser')
'''開獎日期 期數'''
date    = []#Announced date
periods = [] #Number of periods
for span in soup.select('span'):
	match = re.search(r'^<span class="font_black15">(.*?)\s(.*?)</span>',str(span))
	if match:
		date.append(match.group(1))
		periods.append(match.group(2))

'''special_ball 特別號'''
special_ball = []
for div in soup.select('div'):
	match = re.search(r'^<div class="ball_red">(.*?)<',str(div))
	if match:
		special_ball.append(match.group(1))
'''lemon_ball 今彩五三九 三九樂合彩'''
lemon_ball = []
for div in soup.select('div'):
	match = re.search(r'^<div class="ball_tx ball_lemon">(.*?)<',str(div))
	if match:
		lemon_ball.append(match.group(1))
def wei_li():
	wei_li__order  = []
	wei_li__sorted = []
	counter = 0
	for div in soup.select('div'):
		match = re.search(r'^<div class="ball_tx ball_green">(.*?)<',str(div))
		if match:
			counter += 1
			if counter <= 6:
				wei_li__order.append(match.group(1))
			elif 6 < counter <= 12:
				wei_li__sorted.append(match.group(1))
	print("******************威力彩******************")
	print("******************38樂合彩****************")
	print(date[1],periods[1])
	print('*******開獎順序*******',''.join(wei_li__order))
	print('*******大小排序*******',''.join(wei_li__sorted))
	print('*******第二區號*******',int(special_ball[1]))
	print("******************************************")

def big_lottery():
	big_lottery__order  = []
	big_lottery__sorted = []
	counter = 0
	for div in soup.select('div'):
		match = re.search(r'^<div class="ball_tx ball_yellow">(.*?)<',str(div))
		if match:
			counter += 1
			if 21 <= counter <= 26:
				big_lottery__order.append(match.group(1))
			elif 27 <= counter <= 32:
				big_lottery__sorted.append(match.group(1))

	print("******************大樂透******************")
	print("******************49樂合彩****************")
	print(date[3],periods[3])
	print('*******開獎順序*******',''.join(big_lottery__order))
	print('*******大小排序*******',''.join(big_lottery__sorted))
	print('*******特別號碼*******',int(special_ball[2]))
	print("******************************************")

def colorful_539():
	colorful_539__order  = lemon_ball[0:5]
	colorful_539__sorted = lemon_ball[5:10]

	print("******************今彩539*****************")
	print("******************39樂合彩****************")
	print(date[6],periods[6])
	print('*******開獎順序*******',''.join(colorful_539__order))
	print('*******大小排序*******',''.join(colorful_539__sorted))
	print("******************************************")


''' Bingo Bingo '''
def bingoBingo():
    bingoDiv = soup.find('div', class_='contents_box01')

    yellowBalls = bingoDiv.find_all("div", class_='ball_tx ball_yellow')    # 開出獎號
    redBall = bingoDiv.find('div', class_='ball_red')                       # 超級獎號
    blueBall = bingoDiv.find('div', class_='ball_blue_BB1')                 # 猜大小
    purpleBall = bingoDiv.find('div', class_='ball_blue_BB2')               # 猜單雙

    print('****************Bingo Bingo***************')
    print(date[0], periods[0])
    print('*******開出獎號*******')
    for index, number in enumerate(yellowBalls):
        print(number.text, end='')
        if index == (len(yellowBalls)/2-1):
            print('')
    print('')
    print('*******超級獎號******* {}'.format(redBall.text))
    print('********猜大小******** {}'.format(blueBall.text))
    print('********猜單雙******** {}'.format(purpleBall.text))
    print('******************************************')
# def happy_39():
# 	happy_39__order  = lemon_ball[10:15]
# 	happy_39__sorted = lemon_ball[15:20]
# 	counter = 0

# 	print("******************39樂合彩*****************")
# 	print(date[7],periods[7])
# 	print('*******開獎順序*******',''.join(happy_39__order))
# 	print('*******大小排序*******',''.join(happy_39__sorted))
# 	print("******************************************")
print("******************************************")
wei_li()
big_lottery()
colorful_539()
# happy_39()
bingoBingo()
