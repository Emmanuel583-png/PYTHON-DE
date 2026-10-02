# Raw stream of incoming sensor/metric data
metrics: list[float] = [12.5, 45.0, 89.2, 100.1, 5.4]

# 1. Pitfall: In-place mutation
# WRONG: metrics = metrics.append(60.0) -> metrics becomes None!
metrics.append(60.0) # CORRECT: Modifies 'metrics' directly

# 2. Advanced Slicing [start:stop:step]
top_three: list[float] = metrics[0:3]   # Takes index 0, 1, 2 (stops before 3)
every_other: list[float] = metrics[::2]  # Takes every second item
reversed_list: list[float] = metrics[::-1] # Reverses the list cleanly

# 3. List Unpacking (Pulling data straight out)
first_metric, second_metric, third_metric, *remaining_metrics = metrics

print("--- LIST INSPECTION ---")
print(f"Full List:           {metrics}")
print(f"Top 3 (Sliced):      {top_three}")
print(f"First & Second & third:      {first_metric}, {second_metric}, {third_metric}")
print(f"Remaining (Packed): {remaining_metrics}")
print(f"{reversed_list}")
print(f"{every_other}")