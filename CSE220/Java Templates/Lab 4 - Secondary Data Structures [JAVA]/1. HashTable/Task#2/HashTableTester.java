//DO NOT TOUCH THIS TESTER CLASS
public class HashTableTester {
    //DO NOT TOUCH THIS TESTER MAIN METHOD    
    public static void main(String[] args){
        
        //DO NOT TOUCH ANY CODE BELOW
        HashTable ht = new HashTable( 3 );

        System.out.println("====================Test#1====================");
        ht.insert("apple", 20);
        ht.insert("coconut", 90);
        ht.insert("cherry", 50);
        System.out.println(":::Expected Output:::\n0 ('coconut', 90) --> \n1 ('apple', 20) --> \n2 ('cherry', 50) --> ");
        System.out.println("---------------------");
        System.out.println(":::  Your Output  :::");
        ht.show();
        System.out.println("====================Test#2====================");
        ht.insert("banana", 30);
        ht.insert("pineapple", 50);
        System.out.println(":::Expected Output:::\n0 ('coconut', 90) --> ('pineapple', 50) --> ('banana', 30) -->\n1 ('apple', 20) -->\n2 ('cherry', 50) -->");
        System.out.println("---------------------");
        System.out.println(":::  Your Output  :::");
        ht.show();
        System.out.println("====================Test#3====================");
        ht.insert("apple", 100);
        ht.insert("guava", 10);
        System.out.println(":::Expected Output:::\n0 ('coconut', 90) --> ('pineapple', 50) --> ('banana', 30) -->\n1 ('apple', 100) --> ('guava', 10) -->\n2 ('cherry', 50) -->");
        System.out.println("---------------------");
        System.out.println(":::  Your Output  :::");
        ht.show();
    }
}
