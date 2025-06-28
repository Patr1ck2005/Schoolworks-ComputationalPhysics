import static java.lang.StrictMath.*;

interface function {
    double cal(double x);
}

public class Derivative {
    public static void main(String[] args) {
        int n = 4;
        double[] h = new double[n];
        for (int i = 0; i < n; i++) {
            h[i] = pow(10, -1 * (i + 1));
        }
        function f = (x) -> x * exp(x * x);
        function d2f = (x) -> (4 * x * x * x + 6 * x) * exp(x * x);
        double f00, f01, f02, f11, f12, d2f1;
        double d2f0 = d2f.cal(2);

        for (double v : h) {
            f00 = f.cal(2);
            f01 = f.cal(2 + v);
            f02 = f.cal(2 + 2 * v);
            f11 = f.cal(2 - v);
            f12 = f.cal(2 - 2 * v);
            d2f1 = (-f02 + 16 * f01 - 30 * f00 + 16 * f11 - f12) / 12 / v / v;

            double err = abs((d2f1 - d2f0) / d2f0);

            System.out.printf("h = %f\n",v);
            System.out.printf("f'0(2.0)   = %.16f, f'(2.0)   = %.16f, relative error = %.16f\n",d2f0, d2f1, err);
        }
    }
}
