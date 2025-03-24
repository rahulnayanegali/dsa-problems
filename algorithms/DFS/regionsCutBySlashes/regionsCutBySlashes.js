/**
 * @param {string[]} grid
 * @return {number}
 */

var regionsBySlashes = function(matrix) {
  const gridSize = matrix.length;
  const wrapperSize = 3
  const matrixSize = gridSize * wrapperSize;
  const grid = new Array(matrixSize)
      .fill()
      .map(() => new Array(matrixSize).fill("1"));
  
  // Populate grid w/ slashes
  for (let i = 0; i < gridSize; i++) {
      for (let j = 0; j < gridSize; j++) {
          const row = i * wrapperSize;
          const col = j * wrapperSize;

          if (matrix[i][j] === "\\") {
              grid[row][col] = "0";
              grid[row + 1][col + 1] = "0";
              grid[row + 2][col + 2] = "0";
          }
          // forward slash
          if (matrix[i][j] === "/") {
              grid[row][col + 2] = "0";
              grid[row + 1][col + 1] = "0";
              grid[row + 2][col] = "0";
          }
      }
  }

  return numIslands(grid);
};

var numIslands = function(grid) {
  const rows = grid.length
  const cols = grid[0].length
  let count = 0 // init to zero
  /**
  1. It is a graph problem, if the square of the grid is '1', follow its neightbours untill reching the waters all the sides.
  2. Use DFS to recursively trace all 4 sides when encounter '1' and marks the visited as '0' to avoid revists.
   */

   const dfs = (row, col) => {
      //Check if the current i, j is not out of bound
      if (row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] != '1' ) {
          return
      }        
      
      // Mark the current one as visited by changing it to zero

      grid[row][col] = '0'
      /**
      1. Goto all 4 directions when grid[i][j] == 1

       - Left: i = 0, j = j - 1
       - top: i = i - 1, j = 0
       - right: i = 0, j = j + 1
       - bottom: i = i + 1, j = 0
       */
      
      dfs(row, col+1)
      dfs(row, col - 1)
      dfs(row - 1, col)
      dfs(row + 1, col)
     
   }

   for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
          if (grid[i][j] === '1') {
              count += 1
              dfs(i, j)
          }
      }
   }

   return count
};

module.exports = regionsBySlashes;
