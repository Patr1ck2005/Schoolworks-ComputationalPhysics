package enterance;

import property.Integration.IntegrationRandom;
import property.Regression;
import util.chat.Scatter;

import java.util.function.Function;

import static java.lang.StrictMath.*;

public class IntegrationMCCal2 {
    public static void main(String[] args) {
        double il = 2;
        double iu = 6;
        double det = 0.01;
        double xl = 0;
        double xu = 1;
        Function<Double, Double> f = x -> 2.0 / (1 + x);

        var integration = new IntegrationRandom(f, xl, xu);
        var n = new double[(int) ((iu - il) / det + 1)];
        var value = new double[n.length];
        var error = new double[n.length];
        var x0 = new double[n.length];
        var y0 = new double[n.length];
        for (int i = 0; i < n.length; i++) {
            n[i] = pow(10, il + i * det);
            integration.setN((int) n[i]);
            value[i] = integration.value();
            error[i] = abs((value[i] - 2 * log(2)) / 2 / log(2));
            x0[i] = log10(n[i]);
            y0[i] = log10(error[i]);
            System.out.println("n = 10^" + (il + i * det) + "\tvalue = " + value[i] + "\terror = " + error[i]);
        }

        var regression = new Regression(x0, y0);
        var y = new double[n.length];
        for (int i = 0; i < n.length; i++) {
            y[i] = regression.calculateRegression(x0[i]);
        }

        System.out.println("k = " + regression.getA());

        var scatter = new Scatter(x0, y0, y);
        scatter.draw();
    }
}
