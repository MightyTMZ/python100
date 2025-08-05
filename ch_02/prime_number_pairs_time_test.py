from prime_number_pairs import main_v1, main_v2
import time

# Time main_v1
start = time.perf_counter()
main_v1()
end = time.perf_counter()
runtime_v1 = end - start
print(f"main_v1 runtime: {runtime_v1:.6f} seconds")

# Time main_v2
start = time.perf_counter()
main_v2()
end = time.perf_counter()
runtime_v2 = end - start
print(f"main_v2 runtime: {runtime_v2:.6f} seconds")

# Calculate percentage improvement
if runtime_v1 > 0:
    improvement = ((runtime_v1 - runtime_v2) / runtime_v1) * 100
    print(f"main_v2 is {improvement:.2f}% faster than main_v1")
else:
    print("Runtime of main_v1 is too small to compare meaningfully.")
