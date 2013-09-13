class MergeSort:
  def __init__(self, cut_off = 10):
    self.insertion_sort_list = InsertionSort().sort_list
    self.cut_off = cut_off

  def merge(self, first_half, second_half):
    i = 0
    j = 0
    length_first = len(first_half)
    length_second = len(second_half)
    total_length = length_first + length_second
    merged_list = range(total_length) 
    for k in merged_list:
      if i >= length_first:
        merged_list[k] = second_half[j]
        j += 1
      elif j >= length_second:
        merged_list[k] = first_half[i]
        i += 1
      elif first_half[i] <= second_half[j]:
        merged_list[k] = first_half[i]
        i += 1
      else:
        merged_list[k] = second_half[j]
        j += 1
    return merged_list

  def sort_list(self, unsorted_list):
    cut_off = 10;
    sorted_list = None
    if len(unsorted_list) == 1:
      sorted_list = unsorted_list
    else:
      length_first = len(unsorted_list)/2
      length_second = len(unsorted_list) - length_first
      if length_first <= cut_off:
        first_half = list(unsorted_list[:length_first])
        self.insertion_sort_list(first_half)
      else:
        first_half = self.sort_list(unsorted_list[:length_first])
      if length_second <= cut_off:
        second_half = list(unsorted_list[length_first:])
        self.insertion_sort_list(second_half)
      else:
        second_half = self.sort_list(unsorted_list[length_first:])
      sorted_list = self.merge(first_half, second_half)
    return sorted_list 

class InsertionSort:
  def sort_list(self, unsorted_list):
    for k in xrange(len(unsorted_list)):
      for j in xrange(k, 0, -1):
        if unsorted_list[j] < unsorted_list[j - 1]:
          swap = unsorted_list[j]
          unsorted_list[j] = unsorted_list[j - 1]
          unsorted_list[j - 1] = swap
        else:
          break

class SelectionSort:
  def sort_list(self, unsorted_list):
    total_length = len(unsorted_list)
    for k in xrange(total_length):
      idx_min = k
      for j in xrange(k, total_length):
        if unsorted_list[j] < unsorted_list[idx_min]:
          idx_min = j
      swap = unsorted_list[k]
      unsorted_list[k] = unsorted_list[idx_min]
      unsorted_list[idx_min] = swap

class ShellSort:
  def sort_list(self, unsorted_list):
    total_length = len(unsorted_list)
    stride = 1
    while stride < total_length / 3:
     stride = 3 * stride + 1
    while stride >= 1:
      for i in xrange(stride, total_length):
        for j in xrange(i, stride - 1, -stride):
          if unsorted_list[j] >= unsorted_list[j - stride] or j < stride:
            break
          else:
            swap = unsorted_list[j]
            unsorted_list[j] = unsorted_list[j - stride]
            unsorted_list[j - stride] = swap
        if i >= total_length:
          break
      stride = stride / 3
