

To build your muscle memory for coding patterns, here are some frequently asked questions by companies that cover the patterns we discussed:

## Two Pointers Pattern

1. "Remove Duplicates from Sorted Array"
    ``` javascript
    /**
     * @param {number[]} nums
    * @return {number}
    */
    var removeDuplicates = function(nums) {
        let i = 0;
        for (let j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) 
                nums[++i] = nums[j];
            console.log(i)
        }
        return ++i;
    };
    ```
2. "Container With Most Water"
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

