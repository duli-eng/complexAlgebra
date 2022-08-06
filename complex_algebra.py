# complex_algebra.py

import math
import numpy as np


def main():
    a = 5.9
    b = -7.5
    z1 = np.complex(a, b)
    z2 = np.complex(np.sqrt(2), np.pi)
    zp = np.power(z1, 2)
    radius = math.sqrt(np.power(a, 2) + np.power(b, 2))
    theta = math.atan(b/a)
    theta = 180 * theta/math.pi

    print(f"\nz1 = {z1:.4f}")
    
    print("\nz2polar = (radius = %0.4f,theta = %0.4f)" % (radius, theta))
    print(f"z2 = {z2:.4f}")
    print(f"z1 + z2 = {z1+z2:.4f}")
    print(f"z1 - z2 = {z1-z2:.4f}")
    print(f"z1 * z2 = {z1*z2:.4f}")
    print(f"z1 / z2 = {z1/z2:.4f}")

    print(f"z1^2 = {zp:.4f}")


if __name__ == "__main__":
    main()
