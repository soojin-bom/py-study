#list의 각 원소들을 element라고 부른다.
s = [1, 'four', 9, 16, 25]

#list를 변수에 담을 수 있다.
print(s)

#각 element들의 번호는 0부터 시작한다.
print(s[1])

#총 몇개의 element가 있는지 셀 수 있다.
print(len(s))

#element는 수정할 수 있다.
s[1] = 4
print(s[1])

#element는 삭제할 수 있다.
del s[2]
print(s)

#list의 끝에 element를 추가할 수 있다.
s.append('룰루랄라~')
print(s)