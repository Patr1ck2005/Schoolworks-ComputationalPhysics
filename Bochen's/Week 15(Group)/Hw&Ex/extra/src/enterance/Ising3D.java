package enterance;

import property.IsingModel3D;
import util.chat.Plot;

import java.awt.*;

import static java.lang.StrictMath.sqrt;
import static util.Vector.line;
import static util.Vector.value;

public class Ising3D {
    public static void main(String[] args) {
        int steps = 1500;
        int warmSteps = 1000;
        int n = 10;
        var spins = new double[n][n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    spins[i][j][k] = 1.0;
                }
            }
        }

        var kT = value(line(1, 10, 10));
        var energy = new double[kT.length];
        var mag = new double[kT.length];
        var magSq = new double[kT.length];
        for (int i = 0; i < kT.length; i++) {
            var isingModel3D = new IsingModel3D(spins, 1, 0);
            for (int j = 0; j < steps; j++) {
                System.out.println("kT " + kT[i] + " step " + j);
                isingModel3D.next(kT[i]);
                if (j > warmSteps) {
                    energy[i] += isingModel3D.energy();
                    mag[i] += isingModel3D.magnetisation();
                    magSq[i] += mag[i] * mag[i];
                }
            }
            energy[i] = energy[i] / (steps - warmSteps);
            mag[i] = mag[i] / (steps - warmSteps);
            magSq[i] = magSq[i] / (steps - warmSteps) - mag[i] * mag[i];
        }

        var plot1 = new Plot(kT, energy);
        plot1.draw();

        var m = new double[kT.length + 1][2][];
        m[0] = new double[][]{kT, mag};
        for (int i = 1; i < kT.length + 1; i++) {
            m[i][0] = new double[2];
            m[i][1] = new double[2];
            m[i][0][0] = kT[i - 1];
            m[i][0][1] = kT[i - 1];
            m[i][1][0] = mag[i - 1] + sqrt(magSq[i - 1]);
            m[i][1][1] = mag[i - 1] - sqrt(magSq[i - 1]);
        }

        var colors = new Color[m.length];
        colors[0] = Color.RED;
        for (int i = 1; i < kT.length + 1; i++) {
            colors[i] = Color.BLACK;
        }

        var plot2 = new Plot(m);
        plot2.draw();
    }
}
