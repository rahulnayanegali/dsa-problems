def topKFrequent(nums, k):
    freq_table = {}

    for i in range(0, len(nums)):
        if nums[i] not in freq_table:
            freq_table[nums[i]] = 1
        else:
            freq_table[nums[i]] += 1

    return list(dict(sorted(freq_table.items(), key=lambda x: x[1], reverse=True)).keys())[:k]


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
