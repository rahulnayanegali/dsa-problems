const graph = {
  'a': ['b', 'c'],
  'b': ['d'],
  'c': ['e'],
  'd': ['f'],
  'e': [],
  'f': []
}

const depthFirstSearch = (graph, source) => {
  if (graph[source]) {
    console.log(source)
  }

  for (let neighbor of graph[source]) {
    depthFirstSearch(graph, neighbor)
  }
}

console.log(depthFirstSearch(graph, 'a'))