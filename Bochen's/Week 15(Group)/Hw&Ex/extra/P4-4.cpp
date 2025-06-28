#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <random>

// Function to initialize the 2D Ising lattice
void initializeLattice(std::vector<std::vector<int>>& lattice, int L) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, 1);

    for (int i = 0; i < L; ++i) {
        std::vector<int> row;
        for (int j = 0; j < L; ++j) {
            int spin = dis(gen) == 0 ? -1 : 1;
            row.push_back(spin);
        }
        lattice.push_back(row);
    }
}

// Function to calculate the magnetization of the 2D Ising model
double calculateMagnetization(std::vector<std::vector<int>>& lattice, int L) {
    double magnetization = 0.0;
    for (int i = 0; i < L; ++i) {
        for (int j = 0; j < L; ++j) {
            magnetization += lattice[i][j];
        }
    }
    return magnetization;
}

// Function to calculate the energy difference for a spin flip
double calculateDeltaE(std::vector<std::vector<int>>& lattice, int L, int i, int j) {
    int spin = lattice[i][j];
    int left = lattice[i][(j - 1 + L) % L];
    int right = lattice[i][(j + 1) % L];
    int up = lattice[(i - 1 + L) % L][j];
    int down = lattice[(i + 1) % L][j];
    return 2 * spin * (left + right + up + down);
}

// Function to perform a Monte Carlo step in the 2D Ising model
void monteCarloStep(std::vector<std::vector<int>>& lattice, int L, double J, double k_B, double T) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);
    std::uniform_int_distribution<> disIndex(0, L - 1);

    for (int step = 0; step < L * L; ++step) {
        int i = disIndex(gen);
        int j = disIndex(gen);
        double delta_E = calculateDeltaE(lattice, L, i, j);

        if (delta_E <= 0 || dis(gen) < exp(-delta_E / (k_B * T))) {
            lattice[i][j] *= -1;
        }
    }
}

int main() {
    // Simulation parameters
    std::vector<int> latticeSizes = {4, 8, 16, 32};  // Lattice sizes
    double J = 1.0;  // Interaction strength
    double k_B = 1.0;  // Boltzmann constant
    int numEquilibrationSteps = 1000;  // Number of equilibration steps
    int numMeasurementSteps = 2000;  // Number of measurement steps
    int numDataPoints = 50;  // Number of data points to generate

    // Output file
    std::ofstream outputFile("magnetization_data.txt");

    // Loop over lattice sizes
    for (int L : latticeSizes) {
        // Initialize the lattice
        std::vector<std::vector<int>> lattice;
        initializeLattice(lattice, L);

        // Loop over temperature range
        for (double T = 1.0; T <= 4.0; T += (4.0 - 1.0) / (numDataPoints - 1)) {
            // Equilibration steps
            for (int step = 0; step < numEquilibrationSteps; ++step) {
                monteCarloStep(lattice, L, J, k_B, T);
            }

            // Measurement steps
            double averageMagnetizationSquared = 0.0;
            for (int step = 0; step < numMeasurementSteps; ++step) {
                monteCarloStep(lattice, L, J, k_B, T);
                double magnetization = calculateMagnetization(lattice, L);
                averageMagnetizationSquared += (magnetization * magnetization) / numMeasurementSteps;
            }

            // Calculate ln(M^2) and ln(L)
            double ln_M_squared = log(averageMagnetizationSquared);
            double ln_L = log(L);

            // Output ln(M^2) and ln(L) to file
            outputFile << ln_L << " " << ln_M_squared << std::endl;
        }
    }

    // Close the output file
    outputFile.close();

    std::cout << "Simulation completed. Results are saved in magnetization_data.txt." << std::endl;

    return 0;
}