// const graph = {
//   'a': ['b', 'c'],
//   'b': ['d'],
//   'c': ['e'],
//   'd': ['f'],
//   'e': [],
//   'f': []
// }

const graph = {
  f: ['g', 'i'],
  g: ['h'],
  h: [],
  i: ['g', 'k'],
  j: ['i'],
  k: ['x','z'],
  x: ['y'],
  y: [],
  z: []
};


// const hasPath = (graph, src, dst) => {
//   console.log('src:', src, 'dst:', dst)
//   if (src === dst) return true

//   for (let neighbor of graph[src]) {
//     if (hasPath(graph, neighbor, dst)) {
//       return true
//     }
//   }

//   return false
// }


console.log(hasPath(graph, 'f', 'j'))