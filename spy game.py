def spy_game(nums):
    l =[]
    for num in nums:
        if num == 0 or num == 7:
            l.append(num)
    if l == [0 , 0, 7]:
        return True
    else:
        return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))