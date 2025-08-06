main.py
# main.py
# Student Learning AI (Starter backend)
print("Welcome to Student Learning AI - Project by Aarush Jha")

name = input("Enter your name: ")
subject = input("What subject do you need help with? ")

print(f"Hi {name}! Let's find resources for {subject}.")



# cpu_benchmark.py
import time
import random

def heavy_computation(n):
    total = 0
    for _ in range(n):
        total += random.random() * random.random()
    return total

def benchmark(repeats, size):
    start = time.perf_counter()
    for _ in range(repeats):
        heavy_computation(size)
    end = time.perf_counter()
    return round(end - start, 4)

if __name__ == "__main__":
    print("CPU Benchmark Simulator")
    tests = [(10000, 1000), (20000, 1000), (30000, 2000)]
    for r, s in tests:
        duration = benchmark(r, s)
        print(f"Test {r}×{s} → {duration}s")
