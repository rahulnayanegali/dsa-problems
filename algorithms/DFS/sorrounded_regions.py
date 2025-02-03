def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """
    row = len(board)
    col = len(board[0])
    visited = [[False for _ in range(col)] for _ in range(row)]

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # [[0,1], [0,-1],[1,0],[-1,0]]
    def dfs(i, j, visited):
        if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != 'O':
            return

        visited[i][j] = True

        if i == 0 or i == row - 1 or j == 0 or j == col - 1:
            print(i, j)
            newman = visited
            print(newman[i][j])
            if board[i][j] == 'X':
                return True

        for dr, dc in directions:
            rr = i + dr
            cc = j + dc

            if visited[rr][cc] == False and board[rr][cc] == 'O':
                if dfs(rr, cc, visited):
                    board[rr][cc] = 'X'
                    return True
        return False

    for i in range(1, row - 1):
        for j in range(1, col - 1):
            if board[i][j] == 'O':
                # visited[i][j] = True
                if not visited[i][j]:
                    # print(i,j)
                    dfs(i, j, visited)

    print(visited)

solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])