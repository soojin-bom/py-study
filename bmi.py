name = input("이름을 입력하세요. ")
weight = int(input("몸무게를 kg 단위로 입력하세요. "))
height = int(input("키를 cm 단위로 입력하세요"))

meter = height / 100
bmi = weight / (meter * meter)

if bmi < 18.5:
    print(name,"님의 비만지수는 ",bmi,"입니다. ","저체중입니다.")
elif bmi < 22.9:
    print(name,"님의 비만지수는 ",bmi,"입니다. ","정상입니다.")
elif bmi < 34.9:
    print(name,"님의 비만지수는 ",bmi,"입니다. ","비만입니다.")
else:
    print(name,"님의 비만지수는 ",bmi,"입니다. ","고도 비만이야!!!")