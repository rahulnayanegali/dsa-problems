def shipWithinDays(weights, D):
    def feasible(capacity):
        days = 1
        total = 0
        for weight in weights:
            total += weight
            if total > capacity:  # too heavy, wait for the next day
                total = weight
                days += 1
                if days > D:  # cannot ship within D days
                    return False
        return True

    left, right = min(weights), sum(weights)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left


print(shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(shipWithinDays([1, 2, 3, 4, 5], 3))


