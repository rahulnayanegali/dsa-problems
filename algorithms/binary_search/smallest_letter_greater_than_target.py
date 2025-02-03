def find_smallest_letter(letters, target):
  start = 0
  end = len(letters) - 1
  
  while (start <= end):
    
    mid = start + (end - start) // 2
    
    if letters[mid] <= target:
      start = mid + 1
    else:
      end = mid - 1
      
  return letters[start] if start < len(letters) else letters[0]

print(find_smallest_letter(["x","x","y","y"], "z")) 
print(find_smallest_letter(["c","f","j"], "a"))
print(find_smallest_letter(["c","f","j"], "c"))