# 這是一個設定使用者密碼並且檢查輸入密碼的程式

pwd = input('請設定您的密碼：')				# 設定使用者密碼

while True:
	pwd_input = input('請確認您的密碼：')		# 確認使用者設定的密碼
	if pwd == pwd_input:
		break
	else:
		print('\n')
		pwd = input('請重新設定密碼：')		# 再次重新設定密碼


pwd_check = input('請輸入您設定的密碼：')
i = 3
while True:
	if pwd_check == pwd:					# 檢查密碼是否輸入正確
		print('密碼正確！')
		break	
	elif i > 0:								# 給3次機會重新輸入密碼
		print('密碼錯誤！')
		print('\n')
		print('您還有',i,'次機會！')
		i = i - 1
		pwd_check = input('請重新輸入密碼：')
	elif i == 0:							# 密碼錯誤3次，鎖定帳戶
		print('輸入錯誤，已鎖定帳戶！')
		break