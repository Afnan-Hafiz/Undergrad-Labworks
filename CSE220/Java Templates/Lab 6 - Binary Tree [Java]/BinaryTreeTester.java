//THIS IS THE DRIVER CODE
//DO NOT MAKE ANY CHANGES HERE
import java.util.Objects;
import java.util.Scanner;

public class BinaryTreeTester {

    public static void main(String[] args) {
        System.out.println("\nEnter any number between 1 to 7.\nTo run all tasks just press enter");
        System.out.print("Which Task do you wanna check: ");
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        sc.close();

        if( input.equals("1") || input.equals("") ) task1();
        if( input.equals("2") || input.equals("") ) task2();
        if( input.equals("3") || input.equals("") ) task3();
        if( input.equals("4") || input.equals("") ) task4();
        if( input.equals("5") || input.equals("") ) task5();
        if( input.equals("6") || input.equals("") ) task6();

        System.out.println(cyan+"\n===================== TheEnd ===================="+endFormat);
    }
    
    public static void task1(){
        Object[] tree;
        BTNode givenRoot, expectedRoot, returnedRoot ;
        taskPrint("\n===================== TASK#1 =====================");
        taskPrint("================== Mirror Tree ===================");
        // index              0    1   2   3   4   5
        tree = new Object[]{ null, 10, 20, 30, 40, 60 };
        givenRoot = treeConstruction(tree, 1);
        System.out.println("::Given Binary Tree::");
        BTPrinter.printNode(givenRoot);
        System.out.print("InOrder Printing: ");
        BTPrinter.inOrderPrint(givenRoot);
        
        System.out.println("--------------------------------------------------");
        // index              0    1   2   3   4      5    6   7
        tree = new Object[]{ null, 10, 30, 20, null, null, 60, 40 };
        expectedRoot = treeConstruction(tree, 1);
        System.out.println("::Expected Tree::");
        BTPrinter.printNode(expectedRoot);
        System.out.print("InOrder Printing: ");
        BTPrinter.inOrderPrint(expectedRoot);
        
        System.out.println(bold+"\n::Your Tree::");
        returnedRoot = Task1.convertMirror(givenRoot);
        BTPrinter.printNode(returnedRoot);
        System.out.print("InOrder Printing: ");
        BTPrinter.inOrderPrint(returnedRoot);
        
        if( isTreeEqual(expectedRoot, returnedRoot) ) successPrint("Task#1");
        else failedPrint("Task#1");
        System.out.println(normal);
    }
    
    public static void task2(){
        Object[] tree;
        BTNode root;
        taskPrint("\n===================== TASK#2 =====================");
        taskPrint("=============== Level Wise Minimum ===============");
        // index              0    1  2   3  4  5    6   7
        tree = new Object[]{ null, 4, 9, 2, 3, -5, null, 7 };
        root = treeConstruction(tree, 1);
        BTPrinter.printNode(root);
        System.out.println("--------------------------------------------------");
        System.out.println("Format: { Lvl(0): minVal, Lvl(1): minVal, Lvl(2): minVal }");
        Integer[] expectedArr = { 4, 2, -5 };
        System.out.println("\n::Expected Array::");
        printArr(expectedArr);
        System.out.println(bold+"\n::Your Returned Array::");
        Integer[] lvlArray = new Integer[ getDepth(root) ];
        Task2.smallestLevel(root, lvlArray, 0);
        printArr(lvlArray);
        
        if( isArrEqual(expectedArr, lvlArray) ) successPrint("Task#2");
        else failedPrint("Task#2");
        System.out.println(normal);
    }
    
    public static void task3(){
        Object[] tree;
        BTNode root;
        taskPrint("\n===================== TASK#3 =====================");
        taskPrint("============== Special Sum of Nodes ==============");
        // index              0   1  2  3  4    5     6  7  8   9   10    11    12  13    14    15   16     17   18  19 
        tree = new Object[]{null, 9, 4, 5, 18, null, 14, 3, 54, 12, null, null, 8, null, null, null, null, null, 91, 56 };
        root = treeConstruction(tree, 1);
        BTPrinter.printNode(root);
        System.out.println("--------------------------------------------------");
        System.out.println("::Expected Output::");
        System.out.println("15");
        Integer returnedInteger = Task3.sumTree(root);
        System.out.println(bold+"\n::Your Output::");
        System.out.println(returnedInteger);
        
        if( Objects.equals(returnedInteger, 15) ) successPrint("Task#3");
        else failedPrint("Task#3");
        System.out.println(normal);
    }
    
    public static void task4(){
        Object[] tree;
        BTNode givenRoot, expectedRoot;
        taskPrint("\n===================== TASK#4 =====================");
        taskPrint("============== Swap Children Nodes ===============");
        // index              0    1    2    3    4    5    6     7    8    9   10    11    12   13     14
        tree = new Object[]{null, 'A', 'B', 'C', 'D', 'E', null, 'F', 'G', 'H', 'I', null, null, null, 'J' };
        givenRoot = treeConstruction(tree, 1);
        BTPrinter.printNode(givenRoot);
        System.out.println("--------------------------------------------------");
        // index              0    1    2    3    4    5     6    7    8    9    10    11    12   13    14   15
        tree = new Object[]{null, 'A', 'C', 'B', 'F', null, 'E', 'D', 'J', null, null, null, 'I', null, 'G', 'H' };
        expectedRoot = treeConstruction(tree, 1);
        System.out.println("::Expected Output Tree::");
        BTPrinter.printNode(expectedRoot);        
        System.out.print("InOrder Printing: ");
        BTPrinter.inOrderPrint(expectedRoot);
        
        System.out.println(bold+"\n::Your Binary Tree::");
        Task4.swapChild(givenRoot, 0, 2);
        BTPrinter.printNode(givenRoot);
        System.out.print("InOrder Printing: ");
        BTPrinter.inOrderPrint(givenRoot);
        
        if( isTreeEqual(expectedRoot, givenRoot) ) successPrint("Task#4");
        else failedPrint("Task#4");
        System.out.println(normal);
    }
    
    public static void task5(){
        Object[] tree;
        BTNode root;
        taskPrint("\n===================== TASK#5 =====================");
        taskPrint("============== Subtraction of Nodes ==============");
        // index              0   1   2   3   4   5   6   7  8   9   10    11    12    13    14  15
        tree = new Object[]{null, 71, 27, 62, 80, 75, 41, 3, 87, 56, null, null, null, null, 19, 89 };
        root = treeConstruction(tree, 1);
        BTPrinter.printNode(root);
        System.out.println("--------------------------------------------------");
        System.out.println("::Expected Output::");
        System.out.println("111");
        Integer returnedInteger = Task5.subtractSummation(root);
        System.out.println(bold+"\n::Your Output::");
        System.out.println(returnedInteger);
        
        if( Objects.equals(returnedInteger, 111) ) successPrint("Task#5");
        else failedPrint("Task#5");
        System.out.println(normal);
    }
    
    public static void task6(){
        Object[] tree;
        BTNode root;
        taskPrint("\n===================== TASK#6 ======================");
        taskPrint("============= Difference of Level Sum =============");
        // index              0   1  2  3  4   5    6  7   8     9      10   11  12  13  14    15 
        tree = new Object[]{null, 1, 2, 3, 4, null, 5, 6, null, null, null, null, 7, 8, null, null};
        root = treeConstruction(tree, 1);
        BTPrinter.printNode(root);
        System.out.println("--------------------------------------------------");
        System.out.println("::Expected Output::");
        System.out.println("4");
        Integer returnedInteger = Task6.levelSum(root);
        System.out.println(bold+"\n::Your Output::");
        System.out.println(returnedInteger);
        
        if( Objects.equals(returnedInteger, 4) ) successPrint("Task#6");
        else failedPrint("Task#6");
        
    }
    
    private static BTNode treeConstruction( Object[] arr, int i ){
        if (i>=arr.length || arr[i]==null)
        return null;
        BTNode p = new BTNode(arr[i]);
        p.left = treeConstruction(arr, 2*i);
        p.right = treeConstruction(arr, 2*i+1);
        return p;
    }
    
    
    private static int getDepth( BTNode root ){
        return getDepthHelper(root,0);
    }
    
    private static int getDepthHelper( BTNode root, int lvl ){
        if( root==null){
            return lvl;
        }
        int leftLvl = getDepthHelper(root.left, lvl+1);
        int rightLvl = getDepthHelper(root.right, lvl+1);
        
        return leftLvl>rightLvl ? leftLvl: rightLvl;
    }
    
    private static boolean isTreeEqual( BTNode root1, BTNode root2  ){
        
        if(root1==null && root2==null) return true;
        if(root1==null && root2!=null) return false;
        if(root1!=null && root2==null) return false;
        //if elements didn't match
        if( !Objects.equals(root1.elem, root2.elem) ){
            return false;
        } 
        boolean left = isTreeEqual(root1.left, root2.left);
        boolean right = isTreeEqual(root1.right, root2.right);
        return left && right; 
    }
    
    private static boolean isArrEqual(Object[] arr1, Object[] arr2){
      if(arr1.length!=arr2.length) return false;
      else{
        for(int i=0; i<arr1.length; i++)
          if( !Objects.equals(arr1[i],arr2[i]) ) return false;
        return true;
      }
    }
    
    private static void printArr(Object[] arr){
        if(arr==null){
            System.out.println("null");
            return;
        }
        System.out.print("{ ");
        for(int i=0; i<arr.length; i++){
            System.out.print( "Lvl("+i+"): "+arr[i]);
            if (i!=arr.length-1)
            System.out.print(", ");
        }
        System.out.println(" }");
    }
    
    static final String green = "\u001B[32m", red = "\u001B[31m", white = "\u001B[37m", cyan = "\033[0;96m";
    static final String bold="\u001B[1m", underline = "\u001B[4m", normal = "\033[0;0m";
    
    static String taskFormat = cyan;
    static String sucsFormat = "\n"+green+bold+underline;
    static String failFormat = "\n"+red+bold+underline;
    static String endFormat = normal+white;

    private static void taskPrint(String task){
        System.out.println(taskFormat+task+endFormat);
    }

    private static void successPrint(String task){
            System.out.println(sucsFormat+"    "+task+" Success!! Output Matched!!!     "+endFormat);
    }
    
    private static void failedPrint(String task){
        System.out.println(failFormat+"    "+task+" Failed!! Output didn't Match!!!   "+endFormat);
    }
    
}