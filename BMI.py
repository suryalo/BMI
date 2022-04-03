height = input('身高(cm)： ')
weight = input('體重(kg)： ')
h = int(height)
w = int(weight)
h = h / 100
BMI = w / (h * h)

if BMI < 18.5:
	print('你的BMI值為：' , BMI, '過輕')
elif BMI >= 18.8 and BMI < 24:
	print('你的BMI值為：' , BMI, '正常')
elif BMI >= 24 and BMI < 27:
	print('你的BMI值為：' , BMI, '過重')
elif BMI >= 27 and BMI < 30:
	print('你的BMI值為：' , BMI, '輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('你的BMI值為：' , BMI, '中度肥胖')
else:
	print('你的BMI值為：' , BMI, '重度肥胖')