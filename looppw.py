x = 3

while True:
	pw = input("請輸入密碼：")
	if pw == "4869":
		print("密碼正確！")
		break
	else:
		x = x - 1
		print("密碼錯誤，您還可再嘗試", x, "次")
		if x == 0:
			print("密碼錯誤已達 3 次，你GG了！")
			break
