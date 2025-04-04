function sortColors(nums) {
  function quickSort(arr, low = 0, high = arr.length - 1) {
      if (low < high) {
          const pivotIndex = partition(arr, low, high);
          quickSort(arr, low, pivotIndex - 1);
          quickSort(arr, pivotIndex + 1, high);
      }
  }

  function partition(arr, low, high) {
      const pivot = arr[high];
      let i = low - 1;
      for (let j = low; j < high; j++) {
          if (arr[j] < pivot) {
              i++;
              [arr[i], arr[j]] = [arr[j], arr[i]];
          }
      }
      [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
      return i + 1;
  }

  quickSort(nums);
  return nums;
}

console.log(sortColors([2,0,2,1,1,0]))