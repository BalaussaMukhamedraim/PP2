def spy_game(nums):
    """Returns True if the list contains 0, 0, 7 in order."""
    code = [0, 0, 7] 
    index = 0 
    
    for num in nums:
        if num == code[index]: 
            index += 1  
        if index == len(code): 
            return True
    
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False
print(spy_game([0, 0, 7]))  # True
print(spy_game([7, 0, 0]))  # False