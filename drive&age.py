drive = input("你有沒有開車 ")
if drive != '有' and drive != '沒有':
	print("只能輸入有/沒有")
	raise SystemExit
age = input("請輸入你的年齡 ")
age = int(age)

if drive == '有':
	if age >=18:
		print("你通過測驗了")
	if age <18:
		print("你怎麼可以開車")
elif drive == '沒有':
	if age >=18:
		print("你可以去考駕照了")
	if age <18:
		age = 18-age
		print("你再過", age , "年就可以考駕照了")