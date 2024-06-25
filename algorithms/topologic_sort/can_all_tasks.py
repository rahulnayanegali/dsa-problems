def can_all_tasks(tasks, prerequisites):
    graph = create_adjacency_list(tasks, prerequisites)

    visited = set()
    recursion_stack = set()

    def dfs(task):
        visited.add(task)
        recursion_stack.add(task)

        neighbors = graph[task] or []

        for neighbor in neighbors:
            if neighbor in recursion_stack:
                return True

            if neighbor not in visited:
                if dfs(neighbor):
                    return True

        recursion_stack.remove(task)
        return False

    for course in range(tasks):
        if course not in visited:
            if dfs(course):
                return False

    return True


def create_adjacency_list(tasks, prerequisites):
    graph = {task: [] for task in range(tasks)}

    for task, prerequisites in prerequisites:
        graph[task].append(prerequisites)
    return graph
