# -*- coding: utf-8
import numpy as np

def main():
    # 配列生成
    x = np.random.randint(1, 5, 5)
    y = np.random.randint(1, 5, 5)

    # 直交座標系 → 極座標系
    radii = np.sqrt(x ** 2 + y ** 2)
    theta = np.arctan2(y, x)

    print(radii)
    print(theta)
    
if __name__ == "__main__":
    main()