def firstEven(arr):
  """
  To co ja napisałem.
  """
  left = 0
  right = len(arr) - 1

  mid = -1
  candidate = None
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] % 2 == 0:  # parzysta
      candidate = arr[mid]
      right = mid - 1
    elif arr[mid] % 2 == 1:  # nieparzysta
      left = mid + 1
    elif left == right:
      candidate = arr[left]

  return candidate


def firstEven(arr):
  """
  Rozwiązanie z odpowiedzi.
  """
  left = 0
  right = len(arr) - 1

  while left < right:
    mid = (left + right) // 2
    if arr[mid] % 2 != 0:  # parzysta
      left = mid + 1
    else:
      right = mid

  return arr[left]

print(firstEven([5, 99, 3, 7, 111, 13, 4, 24, 4, 8]))
print(firstEven([5, 99, 3, 7, 111, 13, 4, 24, 4]))
print(firstEven([5, 99, 3, 7, 111, 13, 4, 24]))
print(firstEven([5, 99, 3, 7, 111, 13, 4]))
print(firstEven([5, 99, 3, 7, 111, 13]))
print(firstEven([5, 13, 2]))
print(firstEven([1, 2]))
print(firstEven([8]))