package enterance;

import property.Regression;
import util.chat.Scatter;

import static java.lang.StrictMath.*;
import static util.Vector.line;
import static util.Vector.value;

public class Buffon {
    public static void main(String[] args) {
        int num = 1001;
        var a = value(line(0.1, 0.9, num));
        double b = 1;
        var x0 = new double[num];
        var lnX = new double[num];
        var error = new double[num];
        var lnError = new double[num];
        for (int i = 0; i < num; i++) {
            int N = 100000;
            int n = 0;
            for (int j = 0; j < N; j++) {
                double x = b * Math.random();
                double p = PI * random();
                int t = (int) floor(x / b);
                double dx = a[i] / 2 * sin(p);
                if (x - t * b - dx < 0 || x - t * b + dx > b) {
                    n++;
                }
            }
            x0[i] = a[i] / b;
            lnX[i] = log(x0[i]);
            double p0 = (double) n / N;
            double pi = (x0[i] <= 1)? 2 * x0[i] / p0 : 2 * (x0[i] - sqrt(x0[i] * x0[i] - 1) + acos(1 / x0[i])) / p0;
            error[i] = abs(pi - PI) / PI;
            lnError[i] = log(error[i]);
//            System.out.println("a/b = " + a / b[i] + "\t N = " + N + "\t n = " + n + "\t pi = " + pi);
        }

        var regression = new Regression(lnX, lnError);
        var lnFit = regression.calculateRegression(lnX);

        var scatter1 = new Scatter(x0, error);
        scatter1.setXLabel("x");
        scatter1.setYLabel("error");
        scatter1.draw();

        var scatter2 = new Scatter(lnX, lnError, lnFit);
        scatter2.setXLabel("ln x");
        scatter2.setYLabel("ln error");
        scatter2.draw();

    }
}
