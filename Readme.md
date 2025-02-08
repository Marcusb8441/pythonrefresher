# Python Programming Assignment

## Overview
This repository contains two Python scripts that demonstrate the use of decorators, recursion, and performance optimization. The first script, `echo.py`, simulates an echo effect when a user yells at a mountain. The second script, `fib.py`, calculates Fibonacci numbers using recursion and optimizes performance with decorators.

### Contents:
1. `echo.py`: Simulates an echo effect.
2. `fib.py`: Calculates Fibonacci numbers with performance optimization using decorators.
3. `plot.png`: A graph showing the execution time for the Fibonacci sequence calculation.

## 1. Echo.py: Simulating an Echo Effect

### Description:
The `echo.py` script mimics the effect of yelling at a mountain, where the mountain repeats your words with a "fading" effect. Each repetition fades out the sound one character at a time.

### Screenshot of `echo.py` Code and Output:
![Echo.py Code and Output](pythonrefresher/images/echo.png)

---

## 2. Fib.py: Fibonacci Sequence with Performance Optimization

### Description:
The `fib.py` script calculates the nth Fibonacci number using recursion. It uses two decorators:
- **`@lru_cache`**: Caches results to avoid redundant calculations.
- **`@timer`**: Measures and prints the time it takes for each Fibonacci calculation.

### Screenshot of `fib.py` Code and Output:
![Fib.py Code and Output](pythonrefresher/images/fib.png)

---

## 3. Execution Time Plot for Fibonacci Calculation

### Plot Description:
The graph shows the execution time for calculating Fibonacci numbers from 1 to 100. The x-axis represents the Fibonacci number (n), and the y-axis represents the execution time in seconds. As the Fibonacci number increases, the execution time increases as well, which is visible in the plot.

### Screenshot of Execution Time Plot:
![Execution Time Plot](pythonrefresher/images/plot.png)

---

## Conclusion

This project demonstrates basic Python functionality, such as recursion, decorators, and performance optimization. The `fib.py` script shows how decorators can be used to improve performance in recursive algorithms, while `echo.py` shows how string manipulation can simulate a real-world echo effect.

---

## Instructions to Run the Code

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repository-name.git
