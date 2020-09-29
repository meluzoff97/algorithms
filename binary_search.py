def binary_search(lst, x):
  start = 0
  end = len(lst) - 1
  while start <= end:
    mid = (start + end) // 2
    elem = lst[mid]
    if elem == x:
      return mid
    else:
      if elem > x:
        end = mid - 1
      else:
        start = mid + 1
  return None