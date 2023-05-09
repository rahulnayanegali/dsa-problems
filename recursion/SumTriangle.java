import java.util.ArrayList;
public class SumTriangle {
    public static void main(String[] args) {
        ArrayList<int[]> outputArray = new ArrayList<>();
        int[] inputArr = {1,2,3,4,5};
        getSumTriangle(inputArr, outputArray, 0);
        for (int[] arr : outputArray) {
            for (int num : arr) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }

    static void getSumTriangle(int[] arr, ArrayList outputArray, int i){

//      return when array gets reduced to single element.
        if (arr.length == 1) {
            return;
        }

//        retain original array if it's first element
        if (i == 0){
            outputArray.add(arr);
            getSumTriangle(arr, outputArray, i+1);
        } else {
            int[] newSmallerArray = new int[arr.length -1];
            for (int j = 0; j < arr.length-1; j++) {
                newSmallerArray[j] = arr[j] + arr[j+1];
            }
//          store the new reduced array to the start of the output array.
            outputArray.add(0, newSmallerArray);

//          call recursively with the reduced array
            getSumTriangle(newSmallerArray, outputArray, i+1);
        }
    }
}

