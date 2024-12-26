

// Generate 1000 random words, each up to 10 characters long
function generateWords() {
  const words = [];
  for (let i = 0; i < 300; i++) {
    const wordLength = Math.floor(Math.random() * 10) + 1; // Random length between 1 and 10
    const word = Array.from({ length: wordLength }, () =>
      String.fromCharCode(97 + Math.floor(Math.random() * 26)) // Random lowercase letter
    ).join('');
    words.push(word);
  }
  return words;
}

// Generate a complex target string of 500 characters long
function generateTarget() {
  const targetLength = 100;
  return Array.from({ length: targetLength }, () =>
    String.fromCharCode(97 + Math.floor(Math.random() * 26)) // Random lowercase letter
  ).join('');
}

const wordsArray = generateWords();
const targetString = generateTarget();

const getMinimumPrefix = (wordsArray, target) => {
  if (!target.length || !wordsArray.length) return -1

  let prefixes = {};
  for (let word of wordsArray) {
    for (let i = 1; i <= word.length; i++) {
      prefixes[word.slice(0, i)] = i;
    }
  }

  // Now Dynamic Programming!!!

  let dp = new Array(target.length + 1).fill(Infinity)
  dp[0] = 0
  for (let i = 0; i < target.length; i++) {
    const indent = '   '.repeat(i);
    console.log(`${indent}i's Depth ${i}`)
    for (let j = i; j < target.length; j++ ) {
      const indent = '   '.repeat(j);
      let prefix = target.slice(i, j + 1)
      if(prefixes[prefix]) {
        console.log(`${indent}j's Depth ${j}`)
        console.log(`${indent}prefix found ${prefix}`)
        console.log(`${indent}before updating ${dp}`)
        dp[j + 1] = Math.min(dp[j+1], dp[i]+1)
        console.log(`${indent}before updating ${dp}`)
      }
    }
  }
  return dp[target.length] === Infinity ? -1 : dp[target.length]

}


function bruteForce(wordsArray, target) {
  if (!target.length || !wordsArray.length) return -1;

  let prefixes = {};
  for (let word of wordsArray) {
    for (let i = 1; i <= word.length; i++) {
      prefixes[word.slice(0, i)] = i;
    }
  }

  function tryCombinations(index, currentString, count, depth = 0) {
    const indent = '   '.repeat(depth);
    console.log(`${indent}Depth ${depth}: Trying combinations at index ${index}, current string: "${currentString}"`);

    if (currentString === target) {
      console.log(`${indent}Found match! Count: ${count}`);
      return count;
    }
    if (index >= target.length) {
      console.log(`${indent}Reached end of target without match`);
      return Infinity;
    }

    let minCount = Infinity;
    for (let j = index; j < target.length; j++) {
      let prefix = target.slice(index, j + 1);
      if (prefixes[prefix]) {
        console.log(`${indent} j=${j} Found valid prefix: "${prefix}"`);
        let result = tryCombinations(j + 1, currentString + prefix, count + 1, depth + 1);
        minCount = Math.min(minCount, result);
      }
    }

    console.log(`${indent}Returning minCount: ${minCount}`);
    return minCount;
  }

  let result = tryCombinations(0, "", 0);
  return result === Infinity ? -1 : result;
}


const inputs = [
  {words: ["abc","aaaaa","bcdef"], target:"aabcdabc"  },
  {words: ["ab", "bc", "cd"], target:"abcd"  },
  {words: ["a", "b", "ab"], target:"ab"  },
  {words: ["ah", "ze", "ko"], target:"zeko"  }
]

for (let { words, target} of inputs) {
  console.log(`   `)

  // Test DP approach
  console.time("DP Approach");
  const resultDP = getMinimumPrefix(words, target);
  console.timeEnd("DP Approach");
  console.log("DP Result:", resultDP);

  console.log(`   `)

  // Test Brute Force approach
  console.time("Brute Force Approach");
  const resultBruteForce = bruteForce(words, target);
  console.timeEnd("Brute Force Approach");
  console.log("Brute Force Result:", resultBruteForce);
  console.log(`   `)

}
