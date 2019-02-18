# 有一个列表lst = [1,4,9,16,2,5,10,15]，生成一个新列表，要求新列表元素是lst相邻2项的和
# 示例：
lst = [1,4,9,16,2,5,10,15]
[lst[i] + lst[i+1] for i in range(len(lst)-1)]

# 等价于：
lst = [1,4,9,16,2,5,10,15]
newlist = []
for i in range(len(lst)-1):
    newlist.append(lst[i] + lst[i+1])
print(newlist)
