cache = {} # n -> result

def K(n): 
  if n < 4:
    return 1
  else:
    if (n - 1) in cache:
      first = cache[n - 1]
    else:
      first = K(n - 1)
      cache[n - 1] = first

    if (n - 3) in cache:
      second = cache[n - 3]
    else:
      second = K(n - 3)
      cache[n - 3] = second
    
    return first - second


for i in range(111):
  print(f"K({i})={K(i)}")