def binary_search(arr, target):
  start = 0
  end = len(arr) - 1

  while start <= end:
    mid = start + (end - start) // 2

    if arr[mid] == target:
      return mid

    elif arr[mid] < target:
      start = mid + 1

    else:
      end = mid - 1