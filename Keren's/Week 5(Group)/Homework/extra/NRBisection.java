/**
 * This class demonstrates the numerical methods of finding roots using a combination of NR and Bisection methods.
 */

import java.util.Scanner;

import static java.lang.StrictMath.*;

public class NRBisection {
    static double epsilon = 1e-10;

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the lower bound");
        double xl = scanner.nextDouble();
        System.out.println("Enter the upper bound");
        double xu = scanner.nextDouble();
        int num = 100;
        int n = (int) ((xu - xl) * num);

        System.out.printf("In %.3f to %.3f, there are roots\n", xl, xu);
        for (int i = 0; i <= n; i++) {
            double x1 = xl + (double) i / num;
            double x2 = xl + (double) (i + 1) / num;
            if (function(x1) * function(x2) < 0) {
                findRoot(x1, x2);
            }
        }
    }

    /**
     * Finds the root of the function within the given range.
     *
     * @param x1 The lower bound of the range
     * @param x2 The upper bound of the range
     */
    private static void findRoot(double x1, double x2) {
        double x0;
        if (abs(function(x1)) < abs(function(x2))) {
            x0 = x1;
        } else {
            x0 = x2;
        }
        double root = solve(x1, x2, x0);
        System.out.printf("%.3f\t", root);
    }

    /**
     * Defines the function for which the root is to be found.
     *
     * @param x The input value
     * @return The value of the function at x
     */
    private static double function(double x) {
        return 4 * cos(x) - exp(x);
    }

    /**
     * Computes the derivative of the function at a given point.
     *
     * @param x The point at which the derivative is to be computed
     * @return The value of the derivative at x
     */
    private static double derivative(double x) {
        return -4 * sin(x) - exp(x);
    }

    /**
     * Implements the NR method to find a new approximation for the root.
     *
     * @param x The current approximation for the root
     * @return The new approximation using the NR method
     */
    private static double xNR(double x) {
        return x - function(x) / derivative(x);
    }

    /**
     * Recursively applies the combined NR and Bisection methods to find the root.
     *
     * @param x1 The lower bound of the range
     * @param x2 The upper bound of the range
     * @param x  The current approximation for the root
     * @return The calculated root
     */
    private static double solve(double x1, double x2, double x) {
        if (abs(function(x)) < epsilon) {
            return x;
        } else {
            double xN = xNR(x);

            if (x1 < xN && x2 > xN) {
                return solve(x1, x2, xN);
            }

            else {
                xN = (x1 + x2) / 2;
                if (function(x1) * function(xN) <= 0) {
                    // Update parameter
                    if (abs(function(x1)) < abs(function(xN))) {
                        return solve(x1, xN, x1);
                    } else {
                        return solve(x1, xN, xN);
                    }
                } else {
                    if (abs(function(x2)) < abs(function(xN))) {
                        return solve(x2, xN, x2);
                    } else {
                        return solve(x2, xN, xN);
                    }
                }
            }
        }
    }
}
