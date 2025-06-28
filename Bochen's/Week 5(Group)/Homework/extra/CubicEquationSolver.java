import static java.lang.StrictMath.*;

/**
 * This class solves a cubic equation of the form ax^3 + bx^2 + cx + d = 0 using Cardano's method.
 */
public class CubicEquationSolver {

    /**
     * Main method to solve a specific cubic equation and print the roots.
     * @param args Command line arguments (not used)
     */
    public static void main(String[] args) {
        double a = 1.0;
        double b = -70.5;
        double c = 1533.54;
        double d = -10082.44;
        System.out.println("Root of "+a+"x^3 + "+b+"x^2 + "+c+"x + "+d+" = 0");
        for (double[] root : solve(a, b, c, d)) {
            System.out.printf("%f+%fi\t", root[0], root[1]);
        }
    }

    /**
     * Solves the cubic equation given the coefficients a, b, c, and d.
     * @param a Coefficient of x^3
     * @param b Coefficient of x^2
     * @param c Coefficient of x
     * @param d Constant term
     * @return Array of arrays containing the real and imaginary parts of the roots
     */
    private static double[][] solve(double a, double b, double c, double d) {
        double A = b * b - 3 * a * c;
        double B = b * c - 9 * a * d;
        double C = c * c - 3 * b * d;
        double delta = B * B - 4 * A * C;
        if (A == 0 && B == 0) {
            return new double[][]{{-b / 3 / a, 0}, {-c / b, 0}, {-3 * d / c, 0}};
        } else {
            if (delta > 0) {
                double Y1 = A * b + 3 * a * ((-b + sqrt(B * B - 4 * a * c)) / 2);
                double Y2 = A * b + 3 * a * ((-b + sqrt(B * B + 4 * a * c)) / 2);
                double t1 = pow(Y1, 1.0 / 3) + pow(Y2, 1.0 / 3);
                double t2 = pow(Y1, 1.0 / 3) - pow(Y2, 1.0 / 3);
                return new double[][]{{(-b - t1) / 3 / a, 0}, {(-b + t1 / 2) / 3 / a, (-b + t2 * sqrt(3) / 2) / 3 / a}, {(-b + t1 / 2) / 3 / a, -(-b + t2 * sqrt(3) / 2) / 3 / a}};
            } else if (delta == 0) {
                double K = B / A;
                return new double[][]{{-b / a + K, 0}, {-K / 2, 0}, {-K / 2, 0}};
            } else {
                double T = (2 * A * b - 3 * a * B) / 2 / sqrt(A * A * A);
                double theta = acos(T);
                double t1 = cos(theta / 3);
                double t2 = sqrt(3) * sin(theta / 3);
                return new double[][]{{(-b - 2 * sqrt(A) * t1) / 3 / a, 0}, {(-b + sqrt(A) * (t1 + t2)) / 3 / a, 0}, {(-b + sqrt(A) * (t1 - t2)) / 3 / a, 0}};
            }
        }
    }
}
