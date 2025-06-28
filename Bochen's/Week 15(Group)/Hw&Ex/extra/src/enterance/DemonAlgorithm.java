package enterance;

import property.IsingModel1D;
import util.chat.Plot;

import static java.lang.StrictMath.*;
import static util.Vector.line;
import static util.Vector.value;

public class DemonAlgorithm {
    public static void main(String[] args) {
/*        int N = 100;
        double J = 1;
        double h = 0;
        double Ei = -20;
        double[] s = value(line(1, 1, N));
        var isingModel = new IsingModel(s, J, h);
        double Ed = isingModel.energy() + Ei;*/

/*        int steps = 1500;
        int warmSteps = 1000;
        var time = value(line(1, steps, steps));
        var energy = new double[steps];
        var mag = new double[steps];
        double avrEnergy = 0.0;
        double avrMag = 0.0;
        double avrMagSq = 0.0;

        for (int i = 0; i < steps; i++) {
            int index = (int) ((N - 1) * random());
            double delta = isingModel.changeEnergy(index);
            if (Ed <= delta) {
                isingModel.transform(index);
                Ed = isingModel.energy() + Ei;
            }
            energy[i] = isingModel.energy();
            mag[i] = isingModel.magnetisation();

            if (i > warmSteps) {
                avrEnergy += energy[i];
                avrMag += mag[i];
                avrMagSq += mag[i] * mag[i];
            }
        }

        avrEnergy /= (steps - warmSteps);
        avrMag /= (steps - warmSteps);
        avrMagSq /= (steps - warmSteps);

        System.out.println("Average energy: " + avrEnergy);
        System.out.println("Average Magnetisation: " + avrMag);
        System.out.println("Average Magnetisation Square: " + avrMagSq);

        var plot = new Plot(time, energy, mag);
        plot.setXLabel("Monte Calo steps");
        plot.setKeys("energy", "magnetisation");
        plot.draw();*/

/*        double kB = 1.380649 * pow(10, -23);
        double T = 4 * J / log(1 + 4 * J / Ed) / kB;
        System.out.println("T = " + T);
        System.out.println("M = " + (abs(Ed) / J));*/

        int N = 100;
        double J = 1;
        double h = 0;
        double[] Ei = {-40, -60, -80};
        double[] s = value(line(1, 1, N));
        var isingModel = new IsingModel1D(s, J, h);
        double E0 = isingModel.energy();
        var kT = new double[Ei.length];
        var MSq = new double[Ei.length];

        for (int i = 0; i < Ei.length; i++) {
            double Ed = E0 + Ei[i];
            kT[i] = 4 * J / log(1 + 4 * J / Ed);
            MSq[i] = abs(Ed) * abs(Ed) / J / J;
            System.out.println("kT = " + kT[i]);
            System.out.println("E = " + (E0 - Ed));
            System.out.println("exact E/N = " + (- tanh(J / kT[i])));
        }

        var plot = new Plot(kT, MSq);
        plot.setXLabel("kT");
        plot.setYLabel("MSq");
        plot.draw();
    }
}
