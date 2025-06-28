package enterance;

import util.Matrix;
import util.Vector;
import util.chat.Plot;

import java.awt.*;

public class MatrixCal2 {
    public static void main(String[] args) {
/*        var p = new Matrix(new double[][]{
                {0,   0,   1.0/4.0, 0,       0,       0},
                {0,   0,   1.0/4.0, 0,       0,       0},
                {1.0, 1.0, 0,       1.0/2.0, 1.0/2.0, 0},
                {0,   0,   1.0/4.0, 0,       0,       1.0/2.0},
                {0,   0,   1.0/4.0, 0,       0,       1.0/2.0},
                {0,   0,   0,       1.0/2.0, 1.0/2.0, 0}
        });
        var l0 = new Matrix(new double[][]{{1.0}, {0}, {0}, {0}, {0}, {0}});
        int n = 25;
        var x = Vector.value(Vector.line(1, n, n));
        var y = new double[6][n];
        var l = l0;
        for (int i = 0; i < n; i++) {
            l = p.multiplyMatrix(l);
            for (int j = 0; j < 6; j++) {
                y[j][i] = l.get(j, 0);
            }
        }
        var scatter = new Plot(x, y);
        String[] keys = new String[6];
        for (int i = 0; i < 6; i++) {
            keys[i] = "room" + (i + 1);
        }
        scatter.setKeys(keys);
        scatter.setColors(Color.RED, Color.BLUE, Color.GREEN, Color.MAGENTA, Color.CYAN, Color.YELLOW);
        scatter.draw();*/

        var p = new Matrix(new double[][]{
                {0,   0,   1.0/4.0, 0,       0,       0},
                {0,   0,   1.0/4.0, 0,       0,       0},
                {1.0, 1.0, 0,       1.0/2.0, 1.0/2.0, 0},
                {0,   0,   1.0/4.0, 0,       0,       1.0/2.0},
                {0,   0,   1.0/4.0, 0,       0,       1.0/2.0},
                {0,   0,   0,       1.0/2.0, 1.0/2.0, 0}
        });
        var l0 = new Matrix(new double[][]{{1.0}, {0}, {0}, {0}, {0}, {0}});
        int n = Integer.MAX_VALUE;
        var l = p.multiplyMatrix(l0);
        int index = 4;
        for (int i = 0; i < p.getColumn(); i++) {
            p.set(i, index, 0.0);
        }
        System.out.println(p.display());
        double expect = 0;
        for (int i = 1; i < n; i++) {
            l = p.multiplyMatrix(l);
            expect += i * l.get(index, 0);
            System.out.println("time = " + i + ", probability of now = " + l.get(index, 0) + ", expect = " + expect);
        }
        System.out.println(expect);
    }
}
