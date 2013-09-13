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
        first_half = self.insertion_sort_list(unsorted_list[:length_first])
      else:
        first_half = self.sort_list(unsorted_list[:length_first])
      if length_second <= cut_off:
        second_half = self.insertion_sort_list(unsorted_list[length_first:])
      else:
        second_half = self.sort_list(unsorted_list[length_first:])
      sorted_list = self.merge(first_half, second_half)
    return sorted_list 

class InsertionSort:
  def sort_list(self, unsorted_list):
    for k in range(len(unsorted_list)):
      for j in range(k, 0, -1):
        if unsorted_list[j] < unsorted_list[j - 1]:
          swap = unsorted_list[j]
          unsorted_list[j] = unsorted_list[j - 1]
          unsorted_list[j - 1] = swap
        else:
          break
    return unsorted_list
 
