def repeatedNumber(nums):
    n = len(nums)
    
    # XOR of all numbers from 1 to n
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i
    
    # XOR of all numbers in the array
    xor_nums = 0
    for num in nums:
        xor_nums ^= num
    
    # XOR of the missing and repeated numbers
    xor_missing_repeated = xor_all ^ xor_nums
    
    # Find the rightmost set bit in the XOR result
    rightmost_set_bit = xor_missing_repeated & -xor_missing_repeated
    
    # Separate the numbers into two groups based on the rightmost set bit
    group1, group2 = 0, 0
    for i in range(1, n + 1):
        if i & rightmost_set_bit:
            group1 ^= i
        else:
            group2 ^= i
    
    for num in nums:
        if num & rightmost_set_bit:
            group1 ^= num
        else:
            group2 ^= num
    
    # Check which number is repeated
    for num in nums:
        if num == group1:
            return [group1, group2]
        elif num == group2:
            return [group2, group1]

# Example
input_nums = [3, 1, 2, 5, 3]
result = repeatedNumber(input_nums)
print(result)  # Output: [3, 4]
