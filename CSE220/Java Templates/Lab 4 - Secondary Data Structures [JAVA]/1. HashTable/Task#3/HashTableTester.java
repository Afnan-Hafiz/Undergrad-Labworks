//DO NOT TOUCH THIS TESTER CLASS
public class HashTableTester {
    //DO NOT TOUCH THIS TESTER MAIN METHOD    
    public static void main(String[] args){

        //DO NOT TOUCH ANY CODE BELOW
        Object[][] pairs = {
            {34, "Abid"},
            {4, "Rafi"},
            {6, "Karim"},
            {3, "Chitra"},
            {22, "Nilu"},
            {18, "Niloy"},
            {30, "Laima"}
        };

        HashTable ht = new HashTable( 6 );
        ht.createFromArray(pairs);
        
        System.out.println("Expected HashTable at the Beginning");
        String exOut = "0: (3, 'Chitra') --> null\n"
                     + "1: (22, 'Nilu') --> (4, 'Rafi') --> (34, 'Abid') --> null\n"
                     + "2: null\n"
                     + "3: (30, 'Laima') --> (18, 'Niloy') --> (6, 'Karim') --> null\n"
                     + "4: null\n"
                     + "5: null";
        System.out.println(exOut);
        System.out.println("----------------------");
        System.out.println("Your HashTable at the Beginning");
        ht.printHashTable();
                            
        System.out.println("===================Test#1===================");
        System.out.println("----------------------");
        System.out.println("Removing key 22");
        ht.remove( 22 );
        System.out.println("----------------------");
        exOut = "::::Excepted Output::::\n"
                    + "0: (3, 'Chitra') --> null\n"
                    + "1: (4, 'Rafi') --> (34, 'Abid') --> null\n"
                    + "2: null\n"
                    + "3: (30, 'Laima') --> (18, 'Niloy') --> (6, 'Karim') --> null\n"
                    + "4: null\n"
                    + "5: null";
        System.out.println( exOut );
        System.out.println("----------------------");
        System.out.println(":::  Your Output  :::");
        ht.printHashTable();

        System.out.println("===================Test#2===================");
        System.out.println("----------------------");
        System.out.println("Removing key 18");
        ht.remove( 18 );
        System.out.println("----------------------");
        exOut = "::::Excepted Output::::\n"
                    + "0: (3, 'Chitra') --> null\n"
                    + "1: (4, 'Rafi') --> (34, 'Abid') --> null\n"
                    + "2: null\n"
                    + "3: (30, 'Laima') --> (6, 'Karim') --> null\n"
                    + "4: null\n"
                    + "5: null";
        System.out.println( exOut );
        System.out.println("----------------------");
        System.out.println(":::  Your Output  :::");
        ht.printHashTable();
        
        System.out.println("===================Test#3===================");
        System.out.println("----------------------");
        System.out.println("Removing key 6");
        ht.remove( 6 );
        System.out.println("----------------------");
        exOut = "::::Excepted Output::::\n"
                    + "0: (3, 'Chitra') --> null\n"
                    + "1: (4, 'Rafi') --> (34, 'Abid') --> null\n"
                    + "2: null\n"
                    + "3: (30, 'Laima') --> null\n"
                    + "4: null\n"
                    + "5: null";
        System.out.println( exOut );
        System.out.println("----------------------");
        System.out.println(":::  Your Output  :::");
        ht.printHashTable();
        
        System.out.println("===================Test#4===================");
        System.out.println("----------------------");
        System.out.println("Removing key 3");
        ht.remove( 3 );
        System.out.println("----------------------");
        exOut = "::::Excepted Output::::\n"
                    + "0: null\n"
                    + "1: (4, 'Rafi') --> (34, 'Abid') --> null\n"
                    + "2: null\n"
                    + "3: (30, 'Laima') --> null\n"
                    + "4: null\n"
                    + "5: null";
        System.out.println( exOut );
        System.out.println("----------------------");
        System.out.println(":::  Your Output  :::");
        ht.printHashTable();
        System.out.println("===================Test#5===================");
        System.out.println("----------------------");
        System.out.println("Removing key 534");
        ht.remove( 534 );
        System.out.println("----------------------");
        exOut = "::::Excepted Output::::\n"
                    + "0: null\n"
                    + "1: (4, 'Rafi') --> (34, 'Abid') --> null\n"
                    + "2: null\n"
                    + "3: (30, 'Laima') --> null\n"
                    + "4: null\n"
                    + "5: null";
        System.out.println( exOut );
        System.out.println("----------------------");
        System.out.println(":::  Your Output  :::");
        ht.printHashTable();
        System.out.println("===================TheEnd===================");
    }
}
