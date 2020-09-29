def quick_sort(lst):
  if len(lst) < 2:
    return lst
  else:
    low_lst = []
    high_lst = []
    elem = lst[0]
    for i in lst[1:]:
      if i <= elem:
        low_lst.append(i)
      else:
        high_lst.append(i)
    return quick_sort(low_lst) + [elem] + quick_sort(high_lst)