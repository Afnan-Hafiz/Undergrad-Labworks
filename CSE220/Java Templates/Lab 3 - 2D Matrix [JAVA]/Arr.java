//DO NOT TOUCH THIS CODE
class Arr{
    
    // HELPER METHOD TO PRINT 2D ARRAY
    public static void print2D(Object[][] arr) {
        if( arr!=null ){
            int maxWidth = findMaxWidth(arr);
            int row = arr.length, col = arr[0].length;
            for (int r=0; r<row; r++) {
                System.out.print("| ");
                for (int c=0; c<col; c++) {
                    System.out.printf("%-"+maxWidth+"s | ",arr[r][c]);
                }
                System.out.println();
            }
        } else {
            System.out.println(arr);
        }
    }

    // HELPER METHOD TO PRINT LINEAR ARRAY
    public static void print(Object[] arr) {
        if( arr!=null ){
            System.out.print("[ ");
            for (int i=0; i<arr.length; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println("]");
        } else {
            System.out.println(arr);
        }
    }

    // HELPER METHOD TO FIND THE MAXIMUM ELEMENT LENGTH
    public static int findMaxWidth(Object[][] arr2D) {
        int maxWidth = 0;
        for (Object[] arr : arr2D) {
            for (Object elem : arr) {
                maxWidth = Math.max(maxWidth, elem.toString().length());
            }
        }
        return maxWidth;
    }

}