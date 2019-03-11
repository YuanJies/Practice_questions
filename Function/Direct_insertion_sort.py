# 增加一个哨兵位,每轮比较将待比较数放入
# 哨兵依次和待比较数的前一个数据比较,大数靠右移动,找到哨兵中值的插入位置
# 每一轮结束后,得到一个从开始到待比较数位置的一个有序序列

# 示例：（Wayne）

m_list = [[1, 9, 8, 5, 6, 7, 4, 3, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9],
          [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 2]]
#nums = [0, 1, 9, 8, 5, 6]
nums = [0] + m_list[0]
sentinel, *origin = nums    # 哨兵位,待比较数字

count_swap = 0
count_iter = 0

length = len(nums)
for i in range(2, length):    # 从2开始
    nums[0] = nums[i]    # 放置哨兵
    j = i - 1    # 拿索引为1的值与哨兵比较
    count_iter += 1
    if nums[j] > nums[0]:    # 大数右移,找到插入位置
        while nums[j] > nums[0]:
            nums[j+1] = nums[j]    # 依次右移
            j -= 1
            count_swap += 1
        nums[j+1] = nums[0]    # 将哨兵插入,注意在右侧要+1
print(nums, count_swap, count_iter)
