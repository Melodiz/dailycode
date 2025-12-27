import scipy.linalg as sl
import numpy as np
from scipy.optimize import brentq, newton, fsolve

def main():
    n = int(input())
    A = np.array([list(map(float, input().split())) for _ in range(n)])
    B = np.array([list(map(float, input().split())) for _ in range(n)])
    I = np.eye(n)
    
    def det_function(x):
        return np.linalg.det(B + x * A + x**2 * I)
    
    x_star = brentq(det_function, -100, 100)
    print(round(x_star, 4))



if __name__ == "__main__":
    main()