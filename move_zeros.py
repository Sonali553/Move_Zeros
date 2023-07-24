def move_Zeros(nums):
    res = []
    c = []
    for ele in nums:
        if ele != 0:
            res.append(ele)
        else:
            c.append(ele)
    return res + c
print(move_Zeros([0, 1, 0, 3, 12]))
print(move_Zeros([0]))
