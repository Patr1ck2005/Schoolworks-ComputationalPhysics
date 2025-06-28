import java.util.Scanner;
import java.util.function.Function;

import static java.lang.StrictMath.*;

/**
 * This class implements the Muller's Bisection method to find roots of transcendental equations.
 */
public class FullMB {

    static int N = 100;
    static double epsilon = 1e-10;

    public static void main(String[] args) {

        System.out.println("Enter the h");
        Scanner scanner = new Scanner(System.in);
        double h = scanner.nextDouble();

        Function<Double, Double> f = (x) -> x * tan(x) - sqrt(h * h - x * x);
        Function<Double, Double> g = (x) -> x / tan(x) + sqrt(h * h - x * x);

        System.out.println("Root of x tan(x) - sqrt(h^2 - x^2) = 0");
        int n = (int) (abs(h / PI));
        for (int i = n; i >= 0; i--) {
            double xl = -(i + 1.0 / 2) * PI;
            double xu = -i * PI;
            rank(xl, xu, f);
        }
        for (int i = 0; i <= n; i++) {
            double xl = i * PI;
            double xu = (i + 1.0 / 2) * PI;
            rank(xl, xu, f);
        }
        System.out.println();
        System.out.println("Root of x cot(x) + sqrt(h^2 - x^2) = 0");
        n = (int) (abs(h / PI) - 1.0 / 2);
        for (int i = n; i >= 0; i--) {
            double xl = -(i + 1) * PI;
            double xu = -(i + 1.0 / 2) * PI;
            rank(xl, xu, g);
        }
        for (int i = 0; i <= n; i++) {
            double xl = (i + 1.0 / 2) * PI;
            double xu = (i + 1) * PI;
            rank(xl, xu, g);
        }
    }

    /**
     * Find roots within a given range using the Muller's Bisection method.
     *
     * @param xl Lower bound of the range
     * @param xu Upper bound of the range
     * @param f  The function for which roots are to be found
     */
    public static void rank(double xl, double xu, Function<Double, Double> f) {
        double step = 0.001;
        double n = (xu - xl) / step;
        for (int i = 0; i < n - 3; i++) {
            double x = xl + i * step;
            if (f.apply(x) * f.apply(x + step) < 0) {
                double root = fullMB(x, x + step, x + 2 * step, f);
                System.out.printf("%.3f\t", root);
            }
        }
    }

    /**
     * Muller's Bisection method to find a root of a function within a given interval.
     *
     * @param x0       Initial point 1
     * @param x1       Initial point 2
     * @param x2       Initial point 3
     * @param function The function for which the root is to be found
     * @return The estimated root
     */
    public static double fullMB(double x0, double x1, double x2, Function<Double, Double> function) {
        double x = 0;

        for (int i = 0; i < N; i++) {
            double f0 = function.apply(x0);
            double f1 = function.apply(x1);
            double f2 = function.apply(x2);

            double h1 = x1 - x0;
            double h2 = x2 - x1;
            double delta1 = (f1 - f0) / h1;
            double delta2 = (f2 - f1) / h2;
            double d = (delta2 - delta1) / (h1 + h2);

            double b = delta2 + h2 * d;
            double D = Math.sqrt(b * b - 4 * f2 * d);

            double denominator = b + ((b >= 0) ? 1 : -1) * D;

            double dx = -2 * f2 / denominator;
            x = x2 + dx;

            if (Math.abs(dx) < epsilon) {
                break;
            }

            x0 = x1;
            x1 = x2;
            x2 = x;
        }

        return x;
    }
}
