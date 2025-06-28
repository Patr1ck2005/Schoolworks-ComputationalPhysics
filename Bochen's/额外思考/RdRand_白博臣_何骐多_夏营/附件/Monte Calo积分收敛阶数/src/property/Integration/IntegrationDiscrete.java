package property.Integration;

import java.util.function.Function;

import static java.lang.StrictMath.min;

/**
 * This class provides methods to calculate numerical integration with the set discrete.
 */
public class IntegrationDiscrete extends Integration {
    private String options = "T";
    private double h = 1e-6;

    /**
     * Constructs an Integration object with default parameters: h = 1e-6 and options = "T".
     *
     * @param function The integrand function.
     * @param a        The lower limit of integration.
     * @param b        The upper limit of integration.
     */
    public IntegrationDiscrete(Function<Double, Double> function, double a, double b) {
        super(function, a, b);
    }

    /**
     * Gets the integration interval.
     *
     * @return The integration interval.
     */
    public double getH() {
        return h;
    }

    /**
     * Sets the integration interval.
     *
     * @param h The integration interval.
     */
    public void setH(double h) {
        this.h = h;
    }

    /**
     * Gets the options of integration.
     *
     * @return The options of integration.
     */
    public String getOptions() {
        return options;
    }

    /**
     * Sets the options of integration.
     *
     * @param options The options of integration, <code>"T", "Trapezoidal" </code> for Trapezoidal, <code> "S", "Simpson" </code> for Simpson, <code>"R", "Rom-berg"</code> for Rom-berg.
     */
    public void setOptions(String options) {
        this.options = options;
    }

    @Override
    public double value() {
        Function<Double, Double> function = getFunction();
        double a = getA();
        double b = getB();
        double n = (b - a) / h;
        double sum = 0.0;
        int threadNum = 20;
        double num = n / threadNum;
        var threadIntegrations = new ThreadIntegration[threadNum];
        for (int i = 0; i < threadNum; i++) {
            threadIntegrations[i] = new ThreadIntegration(function, (a + i * num * h), min((a + (i + 1) * num * h), b), h, options);
            threadIntegrations[i].start();
        }
        for (int i = 0; i < threadNum; i++) {
            try {
                threadIntegrations[i].join();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            sum += threadIntegrations[i].getSum();
        }
        return sum;
    }
}


class ThreadIntegration extends Thread {
    private final Function<Double, Double> function;
    private final double xl;
    private final double xu;
    private final double h;
    private final String options;
    private double sum = 0.0;

    public ThreadIntegration(Function<Double, Double> function, double xl, double xu, double h, String options) {
        this.function = function;
        this.xl = xl;
        this.xu = xu;
        this.h = h;
        this.options = options;
    }

    public double getSum() {
        return sum;
    }

    @Override
    public void run() {
        double n = (xu - xl) / h;
        double xi;
        switch (options) {
            case "T", "Trapezoidal" -> {
                for (int i = 1; i < n; i++) {
                    xi = xl + i * h;
                    sum += function.apply(xi);
                }
                sum = (sum + (function.apply(xl) + function.apply(xu)) / 2) * h;
            }
            case "S", "Simpson" -> {
                for (int i = 1; i < n; i += 2) {
                    xi = xl + i * h;
                    sum += 2 * function.apply(xi) + function.apply(xi + h);
                }
                sum = (2 * sum + (function.apply(xl) + function.apply(xu))) * h / 3;
            }
            case null, default -> throw new IllegalArgumentException("Unsupported option: " + options);
        }
    }
}
