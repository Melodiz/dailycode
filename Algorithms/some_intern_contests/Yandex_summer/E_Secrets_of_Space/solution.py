from scipy.optimize import curve_fit
import numpy as np

def read_data():
    with open('input.txt','r') as f:
        n = int(f.readline())
        x = []
        y = []
        for _ in range(n):
            a,b = map(float,f.readline().split())
            x.append(a)
            y.append(b)
    return np.array(x),np.array(y)
def main():
    x,y = read_data()
    def objective_function(x,a,b,c,d):
        res = a*np.tan(x)+(b*np.sin(x)+c*np.cos(x))**2 + d*np.sqrt(x)
        return res
    (a_opt,b_opt,c_opt,d_opt),_ = curve_fit(objective_function,x, y)
    print(f"{a_opt:.2f} {b_opt:.2f} {c_opt:.2f} {d_opt:.2f}")

if __name__ == "__main__":
    main()