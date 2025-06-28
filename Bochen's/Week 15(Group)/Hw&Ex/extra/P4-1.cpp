#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <random>

// Function to initialize the 2D Ising lattice
void initializeLattice(std::vector<std::vector<int>>& lattice, int N) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, 1);

    for (int i = 0; i < N; ++i) {
        std::vector<int> row;
        for (int j = 0; j < N; ++j) {
            int spin = dis(gen) == 0 ? -1 : 1;
            row.push_back(spin);
        }
        lattice.push_back(row);
    }
}

// Function to calculate the magnetization of the 2D Ising model
double calculateMagnetization(std::vector<std::vector<int>>& lattice, int N) {
    double magnetization = 0.0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            magnetization += lattice[i][j];
        }
    }
    return magnetization;
}

// Function to calculate the energy difference for a spin flip
double calculateDeltaE(std::vector<std::vector<int>>& lattice, int N, int i, int j) {
    int spin = lattice[i][j];
    int left = lattice[i][(j - 1 + N) % N];
    int right = lattice[i][(j + 1) % N];
    int up = lattice[(i - 1 + N) % N][j];
    int down = lattice[(i + 1) % N][j];
    return 2 * spin * (left + right + up + down);
}

// Function to perform a Monte Carlo step in the 2D Ising model
void monteCarloStep(std::vector<std::vector<int>>& lattice, int N, double J, double k_B, double T) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);
    std::uniform_int_distribution<> disIndex(0, N - 1);

    for (int step = 0; step < N * N; ++step) {
        int i = disIndex(gen);
        int j = disIndex(gen);
        double delta_E = calculateDeltaE(lattice, N, i, j);

        if (delta_E <= 0 || dis(gen) < exp(-delta_E / (k_B * T))) {
            lattice[i][j] *= -1;
        }
    }
}

int main() {
    // Simulation parameters
    int N = 50;  // Size of the lattice (N x N)
    double J = 1.0;  // Interaction strength
    double k_B = 1.0;  // Boltzmann constant
    int numTemperatures = 100;  // Number of temperatures
    double minT = 0.0;  // Minimum temperature
    double maxT = 4.0;  // Maximum temperature
    int numEquilibrationSteps = 1000;  // Number of equilibration steps
    int numMeasurementSteps = 2000;  // Number of measurement steps

    // Temperature range
    std::vector<double> temperatures;
    for (int i = 0; i < numTemperatures; ++i) {
        double T = minT + i * (maxT - minT) / (numTemperatures - 1);
        temperatures.push_back(T);
    }

    // Initialize the lattice
    std::vector<std::vector<int>> lattice;
    initializeLattice(lattice, N);

    // Output file
    std::ofstream outputFile("magnetization_data.txt");

    // Perform simulations for different temperatures
    for (double T : temperatures) {
        double magnetization = calculateMagnetization(lattice, N);

        // Equilibration steps
        for (int step = 0; step < numEquilibrationSteps; ++step) {
            monteCarloStep(lattice, N, J, k_B, T);
        }

        // Measurement steps
        for (int step = 0; step < numMeasurementSteps; ++step) {
            monteCarloStep(lattice, N, J, k_B, T);
            magnetization = calculateMagnetization(lattice, N);
        }

        // Output magnetization and temperature to file
        outputFile << T << " " << magnetization << std::endl;
    }

    // Close the output file
    outputFile.close();

    // Identify the temperature range of phase transition
    double transitionTemperature = 0.0;
    for (int i = 0; i < numTemperatures - 1; ++i) {
        if (abs(temperatures[i] - temperatures[i + 1]) > 0.1 && transitionTemperature == 0.0) {
            transitionTemperature = temperatures[i];
        }
    }

    std::cout << "Phase transition occurs around T = " << transitionTemperature << std::endl;

    return 0;
}