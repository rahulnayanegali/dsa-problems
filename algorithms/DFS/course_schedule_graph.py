class Solution:

    def canFinish(self, numCourses, prerequisites):
        graph = self.create_adjacency_list(numCourses, prerequisites)

        visited = set()
        recursion_stack = set()

        def dfs(course):
            visited.add(course)
            recursion_stack.add(course)

            neighbors = graph[course] or []

            for neighbor in neighbors:
                if neighbor in recursion_stack:
                    return True

                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            recursion_stack.remove(course)
            return False

        for course in range(numCourses):
            if course not in visited:
                if dfs(course):
                    return False

        return True

    def create_adjacency_list(self, numCourses, prerequisites):
        graph = {course: [] for course in range(numCourses)}

        for course, prerequisites in prerequisites:
            graph[course].append(prerequisites)

        return graph




