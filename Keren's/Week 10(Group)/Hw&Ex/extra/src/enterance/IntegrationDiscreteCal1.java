package enterance;

import property.Integration.IntegrationDiscrete;
import util.Vector;
import util.chat.Scatter;

import java.util.function.Function;

import static java.lang.StrictMath.*;

public class IntegrationDiscreteCal1 {
    public static void main(String[] args) {
        double epsilon = 1e-6;

/*        Function<Double, Double> f1 = x -> sqrt(1 - x * x);
        Function<Double, Double> f2 = x -> sin(x) * sin(x);

        var integration1 = new IntegrationDiscrete(f1, -1, 1);
        var integration2 = new IntegrationDiscrete(f2, 0, PI);

        System.out.println("Integration 1: " + integration1.value() + "\nIntegration 2: " + integration2.value());*/

/*        var k = Vector.value(Vector.line(0, 1, 1001));
        var T = new double[k.length];
        var K = new double[k.length];

        for (int i = 0; i < k.length; i++) {
            double k0 = k[i];
            double theta0 = asin(k0);
            Function<Double, Double> f1 = x -> 1 / (sqrt(2 * cos(x) - 2 * cos(theta0)) + epsilon);
            Function<Double, Double> f2 = x -> 1 / (sqrt(1 - k0 * k0 * sin(x) * sin(x)) + epsilon);

            var integration1 = new IntegrationDiscrete(f1, 0, theta0);
            var integration2 = new IntegrationDiscrete(f2, 0, PI / 2);

            T[i] = integration1.value();
            K[i] = integration2.value();

            System.out.println("k0 = " + k0 + ",\ttheta0 = " + theta0);
            System.out.println("Integration 1: " + T[i] + ",\tIntegration 2: " + K[i]);
        }
        var scatter = new Scatter(k, T, K);
        scatter.setKeys("T", "K");
        scatter.draw();*/

        Function<Double, Double> f = x -> 1 / (1 + x) / sqrt(x + epsilon);

        var integration = new IntegrationDiscrete(f, 0, 1);

        System.out.println("Integration = " + 2 * integration.value());

    }
}
