package enterance;

import property.Regression;
import util.chat.Scatter;

import static java.lang.StrictMath.log;
import static util.Vector.line;
import static util.Vector.value;

public class AcceptRejectCalPi {
    public static void main(String[] args) {
        int num = 1000;
        var index = value(line(3, 8, num));
        var N = new double[num];
        var error = new double[num];
        var lnError = new double[num];
        for (int i = 0; i < num; i++) {
            System.out.println(i);
            N[i] = Math.pow(10, index[i]);
            double sum = 0;
            for (int j = 0; j < N[i]; j++) {
                double x = Math.random();
                sum += Math.sqrt(1 - x * x);
            }
            double pi = 4 * sum / N[i];
            error[i] = Math.abs(pi - Math.PI) / Math.PI;
            lnError[i] = log(error[i]);
        }

        var regression = new Regression(index, lnError);
        var lnFit = regression.calculateRegression(index);

        var scatter1 = new Scatter(N, error);
        scatter1.setXLabel("N");
        scatter1.setYLabel("error");
        scatter1.draw();

        var scatter2 = new Scatter(index, lnError, lnFit);
        scatter2.setXLabel("ln N");
        scatter2.setYLabel("ln error");
        scatter2.draw();
    }
}
