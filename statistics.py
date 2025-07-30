import math

def all_values_in_range(readings):
  return all(0 < x < 50 for x in readings)

def calculateStats(numbers):
  # implement the computation of statistics here and return the results
  stats = {}
  numbers_without_nan = [reading for reading in numbers if not isinstance(reading, float) or not math.isnan(reading)]
  if numbers_without_nan:
    stats["avg"] = sum(numbers_without_nan) / len(numbers_without_nan)
    stats["max"] = max(numbers_without_nan)
    stats["min"] = min(numbers_without_nan)
  else:
    stats["avg"] = float('nan')
    stats["max"] = float('nan')
    stats["min"] = float('nan')
  return stats
