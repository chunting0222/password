password = 'a123456'
i = 3
while i > 0:
	pwd = input('請輸入密碼： ')
	if pwd == password:
		print('登入成功！')
		break
	else:
		if i == 1:
			print('登入失敗！')
		else:
			print('密碼錯誤，還有',i - 1,'次輸入機會')
	i = i - 1