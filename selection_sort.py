def selection_sort(lst):
  lst_len = len(lst)
  for i in range(lst_len-1):
    min_el = lst[i]
    pos = i
    for j in range(i+1, lst_len):
      if lst[j] < min_el:
        min_el = lst[j]
        pos = j
    if i != pos:
      lst[pos], lst[i] = lst[i], lst[pos]
  return lst