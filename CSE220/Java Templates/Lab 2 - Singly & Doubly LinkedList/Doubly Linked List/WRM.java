public class WRM {
    Patient dh;

    //The constructor is already created for you
    public WRM() {
        dh = new Patient(null, null, null, null, null, null);
        dh.next = dh;
        dh.prev = dh;
    }

    public void registerPatient(int id, String name, int age, String bloodgroup) {
        // To Do
    }

    public void servePatient() {
        // To do
    }

    public void showAllPatient() {
        // To Do
    }

    public boolean canDoctorGoHome() {
        // To Do
        return false; // Delete this line once you're ready
    }

    public void cancelAll() {
        // To Do
    }


    public void reverseTheLine() {
        // To Do
    }

}