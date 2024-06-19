def combinationSum(candidates, target):
    sol = []

    def backtrack(comb, start):
        com_sum = sum(comb)
        if com_sum == target:
            sol.append(comb.copy())
            # return

        elif com_sum < target:
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(comb, i)
                comb.pop()

    backtrack([], 0)
    return sol


print(combinationSum([2, 3, 6, 7], 7))
