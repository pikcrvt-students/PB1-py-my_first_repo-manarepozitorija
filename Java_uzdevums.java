class Main {
    public static void main(String[] args) {
         // apreiķināt y=2x - 1, ja x [-3; 1], Δx=0,5
     double x, y;
     x = -3.0;
     do {
            y = 2 * x - 1;
            System.out.println("x="+x+" y="+y);
            x += 0.5; //vai x = x + 0.5
     } while(x <= 1);
        
    }
}