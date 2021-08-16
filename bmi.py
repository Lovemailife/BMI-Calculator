print('BMI值計算機')
hight = input('身高(公分)')
weight = input('體重(公斤)')
hight = float(hight)
weight = float(weight)
hight = hight / 100
bmi = weight / hight / hight
if bmi < 18.5:
    print(bmi, '體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print(bmi, '正常')
elif bmi >= 24 and bmi < 27:
    print(bmi, '體重過重')
elif bmi >= 27 and bmi <30:
    print(bmi, '輕度肥胖')
elif bmi >= 30 and bmi <35:
    print(bmi, '中度肥胖')
else:
    print(bmi, '重度肥胖')


    