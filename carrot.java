import java.util.Scanner;

public class carrot {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b;
        a = sc.nextInt();
        b = sc.nextInt();
        String[] c = new String[a];
        for (int i = 0; i < a; i++) {
            c[i] = sc.nextLine();
            sc.next();
        }
        System.out.println(b);
    }
}