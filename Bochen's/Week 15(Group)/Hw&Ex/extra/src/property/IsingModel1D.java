package property;

public class IsingModel1D {
    private double[] spins;
    private double J;
    private double h;
    private final int N;

    public IsingModel1D(double[] spins, double J, double h) {
        this.spins = spins.clone();
        this.J = J;
        this.h = h;
        N = spins.length;
    }
    
    public double energy() {
        double energy = 0;
        for (int i = 0; i < N; i++) {
            energy += -J * spins[i] * (spins[(i + 1 + N) % N] + spins[(i - 1 + N) % N]) / 2;
        }
        energy += -h * magnetisation();
        return energy;
    }

    public double magnetisation() {
        double mag = 0;
        for (int i = 0; i < spins.length; i++) {
            mag += spins[i];
        }
        return mag;
    }
    public double changeEnergy(int index) {
        var spinsNew = spins.clone();
        spinsNew[index] *= -1;
        var other = new IsingModel1D(spinsNew, J, h);
        return other.energy() - energy();
    }

    public void transform(int index) {
        spins[index] *= -1;
    }

}
