def generateParenthesis(n):
    def backtrack(combination, open_count, close_count):
        # If we have used up all the parentheses, add the combination to the result
        if open_count == close_count == 0:
            result.append(combination)
            return

        # If we have more open parentheses, we can add a closing parenthesis
        if open_count > close_count:
            backtrack(combination + ')', open_count, close_count - 1)

        # If we have not used up all the open parentheses, we can add an opening parenthesis
        if open_count > 0:
            backtrack(combination + '(', open_count - 1, close_count)

    result = []
    backtrack('', n, n)
    return result