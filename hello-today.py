from datetime import datetime
import random

#이름
name = input("성함이 어떻게 되시죠? ")

#날짜
year = datetime.today().year 
month = datetime.today().month
day = datetime.today().day

#날씨
weather = ["화창함","비가 많이 내림","안개가 꼈음"]
todayweather = random.choice(weather)

#컨디션
condition = ["매우 좋음","보통","많이 피곤함"]
todaycondition = random.choice(condition)

#결과
print("안녕하세요", name, "님.")
print("오늘 날짜는 ",year,"년 ",month,"월 ",day,"일","입니다.")
print("오늘의 날씨는 ",todayweather,", ","컨디션은 ",todaycondition,"입니다.")