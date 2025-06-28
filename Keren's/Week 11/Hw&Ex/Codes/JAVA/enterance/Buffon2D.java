package enterance;

import property.Regression;
import util.chat.Scatter;

import static java.lang.StrictMath.*;
import static java.lang.StrictMath.PI;
import static util.Vector.*;

public class Buffon2D {
    public static void main(String[] args) {
        var index = value(line(3, 5, 1001));
        var N = new double[index.length];

        double a = 2;
        double b = 2;
        double l = 1;
        var error = new double[index.length];
        var lnError = new double[index.length];
        for (int i = 0; i < index.length; i++) {
            N[i] = (int) pow(10, index[i]);
            int n = 0;
            for (int j = 0; j < N[i]; j++) {
                double x = a * random();
                double y = b * random();
                double theta = PI * random();
                double dx = l * cos(theta);
                double dy = l * sin(theta);
                if ((x - dx <= 0 || x + dx >= a) && (y - dy <= 0 || y + dy >= b)){
                    n++;
                }
            }
            double p0 = (double) n / N[i];
            double pi = 2 * l * l / a / b / p0;
            error[i] = abs(pi - PI) / PI;
            lnError[i] = log(abs(pi - PI) / PI);
        }

/*        double a = 2;
        double l = 1;
        var error = new double[index.length];
        var lnError = new double[index.length];
        for (int i = 0; i < index.length; i++) {
            N[i] = (int) pow(10, index[i]);
            int n = 0;
            for (int j = 0; j < N[i]; j++) {
                double x = a * random();
                double theta = PI * random();
                double dx = l * cos(theta);
                if (x - dx <= 0 || x + dx >= a){
                    n++;
                }
            }
            double p0 = (double) n / N[i];
            double pi = 2 * l / a/ p0;
            error[i] = abs(pi - PI) / PI;
            lnError[i] = log(abs(pi - PI) / PI);
        }*/

        var regression = new Regression(index, lnError);
        var lnFit = regression.calculateRegression(index);
        System.out.println("k = " + regression.getA());

        var scatter1 = new Scatter(N, error);
        scatter1.setTitle("error - N");
        scatter1.setXLabel("N");
        scatter1.setYLabel("error");
        scatter1.draw();

        var scatter2 = new Scatter(index, lnError, lnFit);
        scatter2.setTitle("ln error - ln N");
        scatter2.setXLabel("ln N");
        scatter2.setYLabel("ln error");
        scatter2.draw();
    }
}
