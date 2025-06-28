package enterance;

import util.chat.Plot;

import java.awt.*;

import static java.lang.StrictMath.*;

public class BuffonDraw {
    public static void main(String[] args) {
        double a = 1;
        double b = 3;
        int l = 10;
        int N = 1000;
        int n = 0;
        var x = new double[N];
        var p = new double[N];
        for (int i = 0; i < N; i++) {
            x[i] = l * b * Math.random();
            p[i] = PI * random();
            int t = (int) floor(x[i] / b);
            double dx = a / 2 * sin(p[i]);
            if (x[i] - t * b - dx < 0 || x[i] - t * b + dx > b) {
                n++;
            }
        }
        double pi = 2 * N * a / n / b;
        System.out.println("N = " + N + "\t n = " + n + "\t pi = " + pi);

        var data = new double[N + l + 1][2][3];
        var colors = new Color[N + l + 1];

        for (int i = 0; i < N; i++) {
            int t = (int) floor(x[i] / b);
            double y = l * b * random();
            double dx = a / 2 * sin(p[i]);
            double dy = a / 2 * cos(p[i]);
            data[i][0][0] = x[i] - dx;
            data[i][0][1] = x[i];
            data[i][0][2] = x[i] + dx;
            data[i][1][0] = y - dy;
            data[i][1][1] = y;
            data[i][1][2] = y + dy;
            if (x[i] - t * b - dx < 0 || x[i] - t * b + dx > b) {
                colors[i] = Color.RED;
            } else {
                colors[i] = Color.GREEN;
            }
        }

        for (int i = N; i < N + l + 1; i++) {
            data[i][0][0] = (i - N) * b;
            data[i][0][1] = (i - N) * b;
            data[i][0][2] = (i - N) * b;
            data[i][1][0] = -a;
            data[i][1][1] = l * b / 2;
            data[i][1][2] = l * b + a;
            colors[i] = Color.GRAY;
        }

        var plot = new Plot(data);
        plot.setTitle("Buffon's Needle");
        plot.setColors(colors);
        plot.draw();

/*        double a = 1;
        double b = 3;
        int N = 100000;
        int n = 0;
        var x = new double[N];
        var p = new double[N];
        for (int i = 0; i < N; i++) {
            x[i] = b * Math.random() / 2;
            p[i] = PI * random();
            int t = (int) floor(x[i] / b);
            double dx = a / 2 * sin(p[i]);
            if (x[i] - t * b - dx < 0 || x[i] - t * b + dx > b) {
                n++;
            }
        }
        double pi = 2 * N * a / n / b;
        System.out.println("N = " + N + "\t n = " + n + "\t pi = " + pi);

        var x0 = new double[n];
        var p0= new double[n];
        int k = 0;
        for (int i = 0; i < N; i++) {
            int t = (int) floor(x[i] / b);
            double dx = a / 2 * sin(p[i]);
            if (x[i] - t * b - dx < 0 || x[i] - t * b + dx > b) {
                x0[k] = x[i];
                p0[k] = p[i];
                k++;
            }
        }

        var scatter = new Scatter(p0, x0);
        scatter.setTitle("The x - phi figure for the crossing needles");
        scatter.setXLabel("phi");
        scatter.setYLabel("x");
        scatter.draw();*/
    }
}
