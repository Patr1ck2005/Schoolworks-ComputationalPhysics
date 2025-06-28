package property.Integration;

import java.util.function.Function;

/**
 * This class provides methods to calculate numerical integration with the set precision.
 */
public class IntegrationPrecise extends Integration {
    private double precision = 1e-12;

    /**
     * Constructs an Integration object with default parameters: precision = 1e-6.
     *
     * @param function The integrand function.
     * @param a        The lower limit of integration.
     * @param b        The upper limit of integration.
     */
    public IntegrationPrecise(Function<Double, Double> function, double a, double b) {
        super(function, a, b);
    }

    /**
     * Gets the integration accuracy.
     *
     * @return The integration accuracy.
     */
    public double getPrecision() {
        return precision;
    }

    /**
     * Sets the integration accuracy.
     *
     * @param precision The integration accuracy.
     */
    public void setPrecision(double precision) {
        this.precision = precision;
    }

    @Override
    public double value() {
        Function<Double, Double> function = getFunction();
        double a = getA();
        double b = getB();
        int maxIterations = 12;
        var R = new double[maxIterations + 1][maxIterations + 1];
        double h = b - a;
        R[0][0] = 0.5 * h * (function.apply(a) + function.apply(b));

        for (int i = 1; i <= maxIterations; i++) {
            h *= 0.5;
            double sum = 0;
            for (int k = 1; k <= Math.pow(2, i - 1); k++) {
                sum += function.apply(a + (2 * k - 1) * h);
            }
            R[i][0] = 0.5 * R[i - 1][0] + sum * h;
            for (int j = 1; j <= i; j++) {
                R[i][j] = R[i][j - 1] + (R[i][j - 1] - R[i - 1][j - 1]) / (Math.pow(4, j) - 1);
            }
            if (Math.abs(R[i][i] - R[i - 1][i - 1]) < precision) {
                return R[i][i];
            }
        }
        return Double.NaN;
    }
}
