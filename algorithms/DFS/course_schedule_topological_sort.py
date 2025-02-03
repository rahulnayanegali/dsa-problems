from collections import defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Create adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        print(graph)
        # Initialize visited set and recursion stack
        visited = set()
        rec_stack = set()

        def dfs(course):
            visited.add(course)
            rec_stack.add(course)

            for neighbor in graph[course]:
                if neighbor in rec_stack:
                    return False  # Cycle detected
                if neighbor not in visited:
                    if not dfs(neighbor):
                        return False

            rec_stack.remove(course)
            return True

        # Perform DFS for each course
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False

        return True


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print(f"Test case 1: {solution.canFinish(numCourses1, prerequisites1)}")

    # Test case 2
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print(f"Test case 2: {solution.canFinish(numCourses2, prerequisites2)}")

    numCourses3 = 4
    prerequisites3 = [[1, 0], [2, 1], [3, 2]]
    print(f"Test case 3: {solution.canFinish(numCourses3, prerequisites3)}")