//DO NOT TOUCH THIS TESTER CLASS
public class HashTableTester {
    //DO NOT TOUCH THIS TESTER MAIN METHOD    
    public static void main(String[] args){

        //DO NOT TOUCH ANY CODE BELOW
        Object[][] pairs = {
            {"Colt",360},
            {"Cordelius",730},
            {"Shelly",300},
            {"Doug",1200},
            {"Emz",520},
            {"Bo",580}
        };

        int size = pairs.length;
        HashTable ht = new HashTable( size );
        ht.createFromArray(pairs);
        ht.printHashTable();

        Object[] pair = new Object[2];
        pair = new Object[]{"Doug",1200};
        String result = ht.searchHashtable( pair );
        System.out.println("----------------------");
        System.out.println("Searching (Doug,1200) ");
        System.out.println("----------------------");
        System.out.println("Excepted Output: Found");
        System.out.println("Your Output    : "+result);
        System.out.println("----------------------");
        System.out.println("Inserting (Doug,1200) ");
        System.out.println("----------------------");
        System.out.println("Expected Output: (Doug,1200) already Inserted. Cannot reinsert.");
        System.out.print(  "Your Output    : ");
        ht.insert( pair );
        System.out.println("============================================\n");
        
        pair = new Object[]{"Edgar",320};
        result = ht.searchHashtable( pair );
        System.out.println("----------------------");
        System.out.println("Searching (Edgar,320) :");
        System.out.println("----------------------");
        System.out.println("Excepted Output: Not Found");
        System.out.println("Your Output    : "+result);
        System.out.println("----------------------");
        System.out.println("Inserting (Edgar,320) ");
        System.out.println("----------------------");
        String exOut = "::::Excepted Output::::\n"
                    + "0 : (Key: Doug, Value: 1200) --> null\n"
                    + "1 : (Key: Shelly, Value: 300) --> null\n"
                    + "2 : (Key: Cordelius, Value: 730) --> null\n"
                    + "3 : (Key: Edgar, Value: 320) --> (Key: Bo, Value: 580) --> (Key: Emz, Value: 520) --> (Key: Colt, Value: 360) --> null\n"
                    + "4 : null"
                    + "5 : null";
        System.out.println( exOut );
        System.out.println("::::Your Output::::");
        ht.insert( pair );
        ht.printHashTable();
        System.out.println("============================================\n");

        pair = new Object[]{"Edgar",320};
        result = ht.searchHashtable( pair );
        System.out.println("----------------------");
        System.out.println("Searching (Edgar,320) ");
        System.out.println("----------------------");
        System.out.println("Excepted Output: Found");
        System.out.println("Your Output    : "+result);
        System.out.println("----------------------");
        System.out.println("Inserting (Edgar,320) ");
        System.out.println("----------------------");
        System.out.println("Excepted Output: (Edgar,320) already Inserted. Cannot reinsert.");
        System.out.print("Your Output    : ");
        ht.insert( pair );
        System.out.println("============================================\n");
    }
}
