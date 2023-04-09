import random

r = random.randint(1,100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請輸入數字: ')
	num = int(num)
	if num == r: 
		print('終於答對了！')
		print('這是你猜的第',count,'次')
		break
	elif num > r:
		print('猜錯了，數字比' ,num,'小一點哦!')
	elif num < r:
		print('猜錯了，數字比' ,num,'大一點哦！')
	print('這是你猜的第',count,'次')