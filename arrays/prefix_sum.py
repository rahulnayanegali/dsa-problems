def product_except_self_optimized(nums):
    n = len(nums)
    prod = [1] * n

    # Calculate prefix products and store in prod
    for i in range(1, n):
        prod[i] = prod[i - 1] * nums[i - 1]

    # Calculate suffix products and update prod in-place
    suffix = 1
    for i in range(n - 1, -1, -1):
        prod[i] *= suffix
        suffix *= nums[i]

    return prod

# Example usage:
nums = [1, 2, 3, 4, 5]
print("The product array is:", product_except_self_optimized(nums))