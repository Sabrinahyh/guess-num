import random

r = random.randint(1,100)
while True:
	num = input('請輸入數字: ')
	num = int(num)
	if num == r: 
		print('終於答對了！')
		break
	elif num > r:
		print('猜錯了，數字比' ,num,'小一點哦!')
	elif num < r:
		print('猜錯了，數字比' ,num,'大一點哦！')