
def calculateStats(numbers):
  # implement the computation of statistics here and return the results
  stats = {}
  if numbers:
    stats["avg"] = sum(numbers) / len(numbers)
    stats["max"] = max(numbers)
    stats["min"] = min(numbers)
  else:
    stats["avg"] = float('nan')
    stats["max"] = float('nan')
    stats["min"] = float('nan')
  return stats
