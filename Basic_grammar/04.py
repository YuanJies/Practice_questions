# 求100内所有奇数的和（2500）
sum = 0
for i in range(1,100,2):
    sum += i
print(sum)




# 判断学生成绩，成绩等级A~E。其中，90分以上为'A'，80~89分为'B'，70~79分为'C'，60~69分为'D'，60分以下为'E'
grade = int(input("Please enter the student's grade: "))
if grade < 60:
    print("E")
elif grade <= 69:
    print("D")
elif grade <= 79:
    print("C")
elif grade <= 89:
    print("B")
else:
    print("A")
