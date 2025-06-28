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
    int L = 10;  // Size of the lattice (L x L)
    double J = 1.0;  // Interaction strength
    double k_B = 1.0;  // Boltzmann constant
    int numTemperatures = 100;  // Number of temperatures
    double minT = 1.0;  // Minimum temperature
    double maxT = 4.0;  // Maximum temperature
    int numEquilibrationSteps = 1000;  // Number of equilibration steps
    int numMeasurementSteps = 2000;  // Number of measurement steps

    // Temperature range
    std::vector<double> temperatures;
    for (int i = 0; i < numTemperatures; ++i) {
        double T = minT + i * (maxT - minT) / (numTemperatures - 1);
        temperatures.push_back(T);
    }

    // Output file
    std::ofstream outputFile("magnetization_data.txt");

    // Perform simulations for different temperatures and lattice sizes
    for (double T : temperatures) {
        for (int currentL = L; currentL <= 2 * L; currentL += L) {
            // Initialize the lattice
            std::vector<std::vector<int>> lattice;
            initializeLattice(lattice, currentL);

            double magnetization = calculateMagnetization(lattice, currentL);

            // Equilibration steps
            for (int step = 0; step < numEquilibrationSteps; ++step) {
                monteCarloStep(lattice, currentL, J, k_B, T);
            }

            // Measurement steps
            for (int step = 0; step < numMeasurementSteps; ++step) {
                monteCarloStep(lattice, currentL, J, k_B, T);
                magnetization = calculateMagnetization(lattice, currentL);
            }

            // Output lattice size, magnetization, and temperature to file
            outputFile << currentL << " " << magnetization << " " << T << std::endl;
        }
    }

    // Close the output file
    outputFile.close();

    std::cout << "Simulation completed. Results are saved in magnetization_data.txt." << std::endl;

    return 0;
}