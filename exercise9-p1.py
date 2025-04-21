# numerical_integration.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    """Integrand function f(x) = x^4 - 2x + 1."""
    return x**4 - 2*x + 1

def trapezoidal(f, a, b, N):
    """
    Composite trapezoidal rule.
    :param f: function to integrate
    :param a: lower limit
    :param b: upper limit
    :param N: number of subintervals
    :return: approximate integral
    """
    x = np.linspace(a, b, N+1)
    y = f(x)
    h = (b - a) / N
    return h * (0.5 * y[0] + y[1:-1].sum() + 0.5 * y[-1])

def simpson(f, a, b, N):
    """
    Composite Simpson’s rule (requires N even).
    :param f: function to integrate
    :param a: lower limit
    :param b: upper limit
    :param N: number of subintervals (must be even)
    :return: approximate integral
    """
    if N % 2 != 0:
        raise ValueError("Simpson’s rule requires N to be even.")
    x = np.linspace(a, b, N+1)
    y = f(x)
    h = (b - a) / N
    return (h / 3) * (y[0]
                      + 4 * y[1:-1:2].sum()
                      + 2 * y[2:-1:2].sum()
                      + y[-1])

def main():
    # Integration bounds and exact value
    a, b = 0.0, 2.0
    exact_value = 4.4

    # Test for N = 2,4,8,...,256
    Ns = [2**k for k in range(1, 9)]

    # Store results
    trap_results = []
    trap_errors = []
    simp_results = []
    simp_errors = []

    for N in Ns:
        I_trap = trapezoidal(f, a, b, N)
        trap_results.append(I_trap)
        trap_errors.append(abs((I_trap - exact_value) / exact_value))

        I_simp = simpson(f, a, b, N)
        simp_results.append(I_simp)
        simp_errors.append(abs((I_simp - exact_value) / exact_value))

    # Create DataFrame and print
    df = pd.DataFrame({
        'N (subintervals)': Ns,
        'Exact value': exact_value,
        'Trapezoidal': trap_results,
        'Trap Rel. Error': trap_errors,
        'Simpson': simp_results,
        'Simp Rel. Error': simp_errors
    })
    print("\nNumerical Integration Results:\n")
    print(df.to_string(index=False))

    # Plot convergence of relative error
    plt.figure()
    plt.loglog(Ns, trap_errors, 'o-', label='Trapezoidal Error')
    plt.loglog(Ns, [32/N**2 for N in Ns], '--', label='O(N⁻²) Bound')
    plt.xlabel('Number of Subintervals N')
    plt.ylabel('Relative Error')
    plt.title('Trapezoidal Rule Convergence')
    plt.legend()
    plt.grid(True, which='both', ls=':')
    plt.tight_layout()
    plt.savefig('ex9-p11.png')

    plt.figure()
    plt.loglog(Ns, simp_errors, 'o-', label="Simpson's Error")
    plt.loglog(Ns, [4.2666667/N**4 for N in Ns], '--', label='O(N⁻⁴) Bound')
    plt.xlabel('Number of Subintervals N')
    plt.ylabel('Relative Error')
    plt.title("Simpson's Rule Convergence")
    plt.legend()
    plt.grid(True, which='both', ls=':')
    plt.tight_layout()
    plt.savefig('ex9-p12.png')

    plt.show()

if __name__ == '__main__':
    main()
