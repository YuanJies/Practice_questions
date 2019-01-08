# 输入5个数字，打印每个数字的位数，将这些数字排序打印，要求升序打印

nums = []
while len(nums) < 5:
    num = input("Please input a number:").strip().lstrip('0')
    if not num.isdigit():
        continue
    print('The length of {} is {}'.format(num, len(num)))
    nums.append(int(num))
print(nums)

# sort方法排序
lst = nums.copy()
lst.sort()    # 就地修改
print(lst)

#------------------------------------------------------------------

nums = []
while len(nums) < 5:
    num = input("Please input a number:").strip().lstrip('0')
    if not num.isdigit():
        continue
    print('The length of {} is {}'.format(num, len(num)))
    nums.append(int(num))
print(nums)

# 冒泡法
for i in range(len(nums)):
    flag = False
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = tmp
            flag = True
    if not flag:
        break
print(nums)


#------------------------------------------------------------------

lst = [0] * 5
for i in range(1,6):
    val = input(">>>>")
    lst[i-1] = val
    print('length='+str(len(val)))
print(sorted(lst, key=int))


#------------------------------------------------------------------

lst = []
for i in range(5):
    n = int(input('>>>>'))
    print(n)
    lst.append(n)
    
length = len(lst)
for s in range(length):
    for j in range(length-1-s):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)


#------------------------------------------------------------------

num = []
for i in range(5):
    num.append(int(input("请输入一个数字: ")))
    a = num[i]
    print("是"+str(len(str(a)))+"位数")
print(num)
length = len(num)
for x in range(length):
    for j in range(length - 1 - x):
        if num[j] > num[j+1]:
            tmp = num[j]
            num[j] = num[j+1]
            num[j+1] = tmp
print(num)
