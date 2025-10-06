//DO NOT CHANGE THIS CLASS
public class Stack {
    private Node top;

    //DO NOT CHANGE THIS CONSTRUCTOR
    public Stack() {
        this.top = null;
    }

    // Push method
    //DO NOT CHANGE THIS METHOD
    public void push(int elem) {
        Node nn = new Node(elem, top);
        top = nn;
    }

    // Pop method
    //DO NOT CHANGE THIS METHOD
    public Integer pop() {
        if (top == null) {
            // Stack underflow
            return null; // Method returns Integer instead of int to ensure this line works. If you know exception, modify this using Stack Underflow exception.
        }
        int e = top.elem;
        top = top.next;
        return e;
    }

    // Peek method
    //DO NOT CHANGE THIS METHOD
    public Integer peek() {
        if (top == null) {
            // Stack underflow
            return null; // Method returns Integer instead of int to ensure this line works. If you know exception, modify this using Stack Underflow exception.
        }
        return top.elem;
    }

    // isEmpty method
    //DO NOT CHANGE THIS METHOD
    public boolean isEmpty() {
        return top == null;
    }
}
