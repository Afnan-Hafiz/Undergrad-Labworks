//This class will behave like a Doubly Node which will be used in the WRM class
public class Patient{

    public Integer id;
    public String name;
    public Integer age;
    public String bloodGroup;
    public Patient next; //this points to the next patient
    public Patient prev; //this points to the previous patient

    public Patient(Integer id,String name,Integer age,String bloodGroup,Patient next,Patient prev){
        // To Do
    }

}