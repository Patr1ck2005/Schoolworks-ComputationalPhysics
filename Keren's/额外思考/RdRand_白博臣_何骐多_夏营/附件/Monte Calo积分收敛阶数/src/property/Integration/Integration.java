package property.Integration;

import java.util.function.Function;

/**
 * This class provides methods to calculate integration using various numerical methods.
 */
public abstract class Integration {
    private final Function<Double, Double> function;
    private final double a;
    private final double b;

    /**
     * Constructs an Integration.
     *
     * @param function The integrand function.
     * @param a        The lower limit of integration.
     * @param b        The upper limit of integration.
     */
    public Integration(Function<Double, Double> function, double a, double b) {
        this.function = function;
        this.a = a;
        this.b = b;
        if (a > b) {
            throw new IllegalArgumentException("a > b");
        }
    }

    /**
     * Gets the integrated function.
     *
     * @return the integrated function
     */
    public Function<Double, Double> getFunction() {
        return function;
    }

    /**
     * Gets the integration upper limit.
     *
     * @return the integration upper limit
     */
    public double getA() {
        return a;
    }

    /**
     * Gets the integration lower limit.
     *
     * @return the integration lower limit
     */
    public double getB() {
        return b;
    }

    /**
     * Calculates the value of the integration.
     *
     * @return The value of the integration.
     */
    public abstract double value();
}
