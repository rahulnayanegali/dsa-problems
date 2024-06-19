function fibonacci(n) {
  // Base cases
  if (n <= 0) {
    return 0; // By definition, fib(0) = 0
  } else if (n === 1) {
    return 1; // By definition, fib(1) = 1
  } else {
    // Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2); // fib(n) = fib(n-1) + fib(n-2)
  }
}

