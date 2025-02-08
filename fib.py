import time
import matplotlib.pyplot as plt
from functools import lru_cache

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  
        end_time = time.time() 
        elapsed_time = end_time - start_time
        print(f"Finished in {elapsed_time:.8f}secs: {func.__name__}({args[0]}) -> {result}")
        return elapsed_time 
    return wrapper

@lru_cache(maxsize=None)  
@timer
def fib(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def track_times():
    execution_times = []
    cumulative_time = 0
    fibonacci_numbers = range(1, 101)  
    
    for n in fibonacci_numbers:
        time_taken = fib(n)  
        cumulative_time += time_taken  
        execution_times.append(cumulative_time)  
    return fibonacci_numbers, execution_times

def plot_execution_times(fibonacci_numbers, execution_times):
    plt.plot(fibonacci_numbers, execution_times)
    plt.xlabel('Fib Number')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Time for fib numbers')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    fibonacci_numbers, execution_times = track_times()
    plot_execution_times(fibonacci_numbers, execution_times)
