To build your muscle memory for coding patterns, here are some frequently asked questions by companies that cover the patterns we discussed:

To build your muscle memory for coding patterns, here are some frequently asked questions by companies that cover the patterns:

## Two Pointers Pattern

1. "Remove Duplicates from Sorted Array"
    ``` javascript
    /**
     * Removes duplicates from a sorted array in-place
     * Time Complexity: O(n) - We traverse the array once
     * Space Complexity: O(1) - We modify the array in-place, using only constant extra space
     * 
     * @param {number[]} nums - Sorted array with duplicates
     * @return {number} - Length of array after removing duplicates
     */
    var removeDuplicates = function(nums) {
        // Slow pointer - tracks position for next unique element
        let i = 0;
        
        // Fast pointer - scans through the array
        for (let j = 1; j < nums.length; j++) {
            // If we find a new unique element
            if (nums[j] != nums[i]) 
                // Move slow pointer and place unique element
                nums[++i] = nums[j];
        }
        
        // Return length of unique elements (i+1 because i is 0-based index)
        return ++i;
    };
    ```
2. "Container With Most Water"
    ``` javascript
    /** 
     * @param {number[]} height
     * @return {number}
     */
    var maxArea = function(height) {
        let left = 0;                    // Left pointer starts at beginning
        let right = height.length - 1;   // Right pointer starts at end
        let max_area = 0;                // Track maximum area found

        while (left < right) {
            const width = right - left;  // Calculate current width
            const currentHeight = Math.min(height[left], height[right]);  // Height is min of two sides
            const area = width * currentHeight;  // Calculate current area

            if (area > max_area) 
                max_area = area;  // Update max area if current is larger

            // Move the pointer with smaller height
            if (height[left] > height[right]) 
                right -= 1;
            else 
                left += 1;
        }
        
        return max_area;
    };
    ```
3. "3Sum"
4. "Valid Palindrome"

## Fast and Slow Pointers Pattern

1. "Linked List Cycle"
2. "Find the Middle of Linked List"
3. "Happy Number"
4. "Palindrome Linked List"

## Sliding Window Pattern

1. "Maximum Sum Subarray of Size K"
2. "Longest Substring with K Distinct Characters"
3. "Fruits into Baskets"
4. "Longest Substring Without Repeating Characters"

## Merge Intervals Pattern

1. "Merge Intervals"
2. "Insert Interval"
3. "Interval List Intersections"
4. "Meeting Rooms II"

## Dynamic Programming

1. "Climbing Stairs"
2. "Coin Change"
3. "Longest Increasing Subsequence"
4. "House Robber"

## Depth-First Search (DFS)

1. "Number of Islands"
2. "Course Schedule"
3. "Binary Tree Maximum Path Sum"
4. "Word Search"

## Breadth-First Search (BFS)

1. "Binary Tree Level Order Traversal"
2. "Word Ladder"
3. "Shortest Path in Binary Matrix"
4. "Rotting Oranges"

## Binary Search

1. "Search in Rotated Sorted Array"
2. "Find Minimum in Rotated Sorted Array"
3. "Median of Two Sorted Arrays"
4. "Kth Smallest Element in a Sorted Matrix"

## Backtracking

1. "Subsets"
2. "Permutations"
3. "N-Queens"
4. "Palindrome Partitioning"

## Greedy Algorithms

1. "Jump Game"
2. "Gas Station"
3. "Task Scheduler"
4. "Minimum Number of Arrows to Burst Balloons"

Practicing these questions will help you internalize the patterns and improve your problem-solving skills for coding interviews. Remember to focus on understanding the underlying patterns rather than memorizing specific solutions

