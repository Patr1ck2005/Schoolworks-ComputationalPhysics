# romberg_integration.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    """Integrand function f(x) = sin(x)."""
    return np.sin(x)

def romberg(f, a, b, M):
    """
    Build Romberg integration table of size (M+1)x(M+1).
    :param f: integrand function
    :param a: lower limit
    :param b: upper limit
    :param M: maximum depth (rows/cols = M+1)
    :return: 2D numpy array R where R[i,j] is the Romberg estimate
    """
    R = np.zeros((M+1, M+1))
    for i in range(M+1):
        N = 2**i
        x = np.linspace(a, b, N+1)
        y = f(x)
        # Basic trapezoidal estimate
        R[i, 0] = (b - a) / (2 * N) * (y[0] + 2 * y[1:-1].sum() + y[-1])
        # Richardson extrapolation
        for j in range(1, i+1):
            R[i, j] = (4**j * R[i, j-1] - R[i-1, j-1]) / (4**j - 1)
    return R

def main():
    a, b = 0.0, np.pi
    exact_value = 2.0
    M = 6  # builds R[0..6,0..6]

    # Compute Romberg table
    R = romberg(f, a, b, M)

    # Display as DataFrame
    row_labels = [f"2^{i} panels" for i in range(M+1)]
    col_labels = [f"R[{i},{i}]" for i in range(M+1)]
    df = pd.DataFrame(R, index=row_labels, columns=[f"R[{j}]" for j in range(M+1)])
    print("Romberg Integration Table for ∫₀^π sin(x) dx:\n")
    print(df.to_string())
    print(f"\nExact value = {exact_value}\n")

    # Plot diagonal convergence
    diag = np.diag(R)
    plt.figure()
    plt.plot(range(M+1), diag, 'o-', label='R[i,i]')
    plt.axhline(exact_value, linestyle='--', label='Exact = 2.0')
    plt.xticks(range(M+1), [f"R[{i},{i}]" for i in range(M+1)])
    plt.xlabel('Romberg Level i')
    plt.ylabel('Approximation')
    plt.title('Romberg Diagonal Convergence')
    plt.legend()
    plt.grid(True, which='both', ls=':')
    plt.tight_layout()
    plt.savefig('ex9-p21.png')

    # Plot absolute error on semilog-y
    errors = np.abs(diag - exact_value)
    plt.figure()
    plt.semilogy(range(M+1), errors, 'o-')
    plt.xticks(range(M+1), [f"R[{i},{i}]" for i in range(M+1)])
    plt.xlabel('Romberg Level i')
    plt.ylabel('Absolute Error')
    plt.title('Romberg Diagonal Absolute Error')
    plt.grid(True, which='both', ls=':')
    plt.tight_layout()
    plt.savefig('ex9-p22.png')

    plt.show()

if __name__ == '__main__':
    main()
