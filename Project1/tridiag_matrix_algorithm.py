import numpy as np
import matplotlib.pyplot as plt
import time


def tridiagonal_matrix_algorithm(a, b, c, f, x):
    """
    Function implementing the tridiagonal matrix algorithm, which solves the
    problem Au = f for an nxn tridiagonal matrix A.

    Arguments:
        b (array) : The diagonal of the matrix
        a (array) : The diagonal below b
        c (array) : The diagonal above b
        f (array) : RHS vector

    Returns:
        The solution u of the problem Au = f
    """

    n       = len(b)
    h       = x[1] - x[0]
    b_squig = h**2*f
    u       = np.zeros(n)
    c_prime = np.zeros(n-1)
    d_prime = np.zeros(n)

    start = time.process_time()
    c_prime[0]  = c[0] / b[0]
    d_prime[0]  = b_squig[0] / b[0]

    for i in range(1, n-1):
        c_prime[i] = c[i]/(b[i]-(a[i-1]*c_prime[i-1]))

    for j in range(1, n):
        d_prime[j] = (b_squig[j]-(a[j-1]*d_prime[j-1])) \
                     / (b[j]-(a[j-1]*c_prime[j-1]))

    u[n-1] = d_prime[n-1]
    for k in range(n-2, -1, -1):
        u[k] = d_prime[k] - (c_prime[k]*u[k+1])

    end = time.process_time()
    runtime = end - start

    return np.concatenate([np.zeros(1), u, np.zeros(1)]), runtime

def run_tma(n):
    """
    Function for setting up and running the tridiagonal matrix algorithm and
    calculating the closed-form solution.

    Argument(s):
        n (int) : Number of grid points in matrix

    Returns:
        x (array) : independent variable
        u_sol (array) : Closed-form solution of problem
        u_algorithm (array) : Numerical solution of problem
    """
    x = np.linspace(0, 1, n+2)
    f = 100*np.exp(-10*x)

    a = np.ones(n-1)*(-1)
    b = np.ones(n)*(2)
    c = np.ones(n-1)*(-1)

    u_algorithm, runtime = tridiagonal_matrix_algorithm(a, b, c, f[1:-1], x[1:-1])
    u_solution  = 1 - (1-np.exp(-10))*x - np.exp(-10*x)

    return x, u_solution, u_algorithm, runtime


if __name__ == '__main__':

    n_ = [10, 100, 1000]

    for i in n_:
        x, sol, algorithm, runtime = run_tma(i)
        plt.plot(x, sol, label="Closed-form solution")
        plt.plot(x, algorithm, label="Algorithm solution")
        plt.legend()
        plt.xlabel('$x$')
        plt.ylabel('$u (x)$')
        plt.title("Approximation by tridiagonal matrix algorithm, n={}".format(i))
        plt.savefig("Figures/t_m_a_n_{}.png".format(i))
        plt.show()
















# y0
