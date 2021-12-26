# 這是一個設定使用者密碼並且檢查輸入密碼的程式

pwd = input('請設定您的密碼：')	# 設定使用者密碼

while True:
	pwd_input = input('請確認您的密碼：')		# 確認使用者設定的密碼
	if pwd == pwd_input:
		break
	else:
		print('\n')
		pwd = input('請重新設定密碼：')		# 再次重新設定密碼


pwd_check = input('請輸入您設定的密碼：')
while True:
	if pwd_check == pwd:	# 檢查密碼是否輸入正確
		print('密碼正確！')
		break	
	else:
		print('密碼錯誤！')
		print('\n')
		pwd_check = input('請重新輸入密碼：')