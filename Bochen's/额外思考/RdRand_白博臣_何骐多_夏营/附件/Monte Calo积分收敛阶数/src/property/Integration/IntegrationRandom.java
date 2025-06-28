package property.Integration;

import util.RealRand;

import java.util.Random;
import java.util.function.Function;

import static java.lang.StrictMath.*;

/**
 * This class provides methods to calculate numerical integration using Monte Carlo methods.
 */
public class IntegrationRandom extends Integration {
    private int N = 1000;

    /**
     * Constructs an Integration object with default parameters: N = 1000.
     *
     * @param function The integrand function.
     * @param a        The lower limit of integration.
     * @param b        The upper limit of integration.
     */
    public IntegrationRandom(Function<Double, Double> function, double a, double b) {
        super(function, a, b);
    }

    public void setN(int N) {
        this.N = N;
    }

    @Override
    public double value() {
        Function<Double, Double> function = getFunction();
        double a = getA();
        double b = getB();
        int n = 0;
        var m = m(function, a, b);
        double max = m[0];
        double min = m[1];
        for (int i = 0; i < N; i++) {
            var rand = new Random();
            double x = a + (b - a) * rand.nextDouble();
            double y = min + (max - min) * rand.nextDouble();
            double y0 = function.apply(x);
            if (y < y0 && y > min) {
                n++;
            }
        }
        return (b - a) * (max - min) * n / N + (b - a) * min;
    }

    private double[] m(Function<Double, Double> function, double a, double b) {
        int num = 1000;
        double epsilon = (b - a) / num;
        double max = function.apply(a);
        double min = function.apply(a);
        for (int i = 0; i < num; i++) {
            double x = a + i * epsilon;
            double y = function.apply(x);
            max = max(max, y);
            min = min(min, y);
        }
        return new double[]{max, min};
    }
}
