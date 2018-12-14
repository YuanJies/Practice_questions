# 依次接收用户输入的3个数,排序后打印

# 转换int后,判断大小排序。使用分支结构完成
number_1 = int(input("Please enter the first number: "))
number_2 = int(input("Please enter the second number: "))
number_3 = int(input("Please enter the third number: "))
if number_1 >= number_2:
    if number_1 >= number_3:
        if number_2 >= number_3:
            print(number_1,number_2,number_3)
        else:
            print(number_1,number_3,number_2)
else:
    if number_3 >= number_2:
        print(number_3,number_2,number_1)
    else:
        if number_3 >= number_1:
            print(number_2,number_3,number_1)
        else:
            print(number_2,number_1,number_3)
	

#---------------------------------------------------------------------

# 使用列表
nums = []
for i in range(3):
    nums.append(int(input('{}: '.format(i))))

if nums[0] > nums[1]:
    if nums[0] > nums[2]:
        i3 = nums[0]
        if nums[1] > nums[2]:
            i2 = nums[1]
            i1 = nums[2]
        else:
            i2 = nums[2]
            i1 = nums[1]
    else:
        i2 = nums[0]
        i3 = nums[2]
        i1 = nums[1]
else:    # 0<1
    if nums[0] > nums[2]:
        i3 = nums[1]
        i2 = nums[0]
        i1 = nums[2]
    else:    # 0<2
        if nums[1] < nums[2]:    # 1<2
            i1 = nums[0]
            i2 = nums[1]
            i3 = nums[2]
        else:    # 1>2
            i1 = nums[0]
            i2 = nums[2]
            i3 = nums[1]
print(i1,i2,i3)



# 改进
nums = []
out = None
for i in range(3):
    nums.append(int(input("{}: ".format(i))))
    
if nums[0] > nums[1]:
    if nums[0] > nums[2]:
        if nums[1] > nums[2]:
            out = [2,1,0]
        else:
            out = [1,2,0]
    else:
        out = [1,0,2]
else:    # 0<1
    if nums[0] > nums[2]:
        out = [2,0,1]
    else:    # 0<2
        if nums[1] < nums[2]:    # 1<2
            out = [0,1,2]
        else:    # 1>2
            out = [0,2,1]
out.reverse()
for i in out:
    print(nums[i],end=',')


#---------------------------------------------------------------------

# 使用max函数或者min函数实现
nums = []
out = None
for i in range(3):
    nums.append(int(input("{}: ".format(i))))
    
# 此处不能使用for循环，不能一边迭代该列表，同时删除或增加该列表
while True:
    cur = min(nums)
    print(cur)
    nums.remove(cur)
    
    if len(nums) == 1:
        print(nums[0])
        break


#---------------------------------------------------------------------
# 列表sort实现
nums = []
for i in range(3):
    nums.append(int(input("{}: ".format(i))))
nums.sort()
print(nums)
