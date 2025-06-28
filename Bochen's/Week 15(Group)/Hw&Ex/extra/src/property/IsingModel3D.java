package property;

import static java.lang.StrictMath.exp;
import static java.lang.StrictMath.random;

public class IsingModel3D {
    private double[][][] spins;
    private double J;
    private double h;
    private final int Nx;
    private final int Ny;
    private final int Nz;

    public IsingModel3D(double[][][] spins, double J, double h) {
        this.spins = spins.clone();
        this.J = J;
        this.h = h;
        Nx = spins.length;
        Ny = spins[0].length;
        Nz = spins[0][0].length;
    }

    public double energy() {
        double energy = 0;
        for (int i = 0; i < Nx; i++) {
            for (int j = 0; j < Ny; j++) {
                for (int k = 0; k < Nz; k++) {
                    energy += -J * spins[i][j][k] * (spins[(i + 1 + Nx) % Nx][j][k] + spins[(i - 1 + Nx) % Nx][j][k]
                + spins[(i + 1 + Nx) % Nx][(j + 1 + Ny) % Ny][k] + spins[(i - 1 + Nx) % Nx][(j - 1 + Ny) % Ny][k]
                + spins[(i + 1 + Nx) % Nx][j][(k + 1 + Nz) % Nz] + spins[(i - 1 + Nx) % Nx][j][(k - 1 + Nz) % Nz]
                + spins[(i + 1 + Nx) % Nx][(j + 1 + Ny) % Ny][(k + 1 + Nz) % Nz] + spins[(i - 1 + Nx) % Nx][(j - 1 + Ny) % Ny][(k - 1 + Nz) % Nz] );
                }
            }
        }
        energy += -h * magnetisation();
        return energy;
    }

    public double magnetisation() {
        double mag = 0;
        for (int i = 0; i < Nx; i++) {
            for (int j = 0; j < Ny; j++) {
                for (int k = 0; k < Nz; k++) {
                    mag += spins[i][j][k];
                }
            }
        }
        return mag;
    }
    public double changeEnergy(int ix, int iy, int iz) {
        var spinsNew = spins.clone();
        spinsNew[ix][iy][iz] *= -1;
        var other = new IsingModel3D(spinsNew, J, h);
        return other.energy() - energy();
    }

    public void transform(int ix, int iy, int iz) {
        spins[ix][iy][iz] *= -1;
    }

    public void next(double kT) {
        for (int i = 0; i < Nx; i++) {
            for (int j = 0; j < Ny; j++) {
                for (int k = 0; k < Nz; k++) {
                    double delta = changeEnergy(i, j, k);
                    if(delta < 0) {
                        transform(i, j, k);
                    } else {
                        if (exp(- delta / kT) > random()) {
                            transform(i, j, k);
                        }
                    }
                }
            }
        }
    }
}
