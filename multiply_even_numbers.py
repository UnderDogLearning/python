def multiply_even_numbers(nums):
    sum = 1
    for num in nums:
        if num % 2 == 0:
            sum = sum * num
    return sum
