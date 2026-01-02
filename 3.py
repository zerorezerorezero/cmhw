import cmath

def root3(a, b, c, d):
    """
    求解三次方程 ax³ + bx² + cx + d = 0 的所有根
    
    參數:
        a, b, c, d: 方程係數
    
    返回:
        包含三個根的列表（可能包含複數根）
    """
    # 處理 a = 0 的情況（退化為二次方程）
    if a == 0:
        if b == 0:
            if c == 0:
                return [] if d == 0 else []
            return [-d / c]
        # 二次方程求根公式
        discriminant = c**2 - 4*b*d
        sqrt_disc = cmath.sqrt(discriminant)
        return [(-c + sqrt_disc) / (2*b), (-c - sqrt_disc) / (2*b)]
    
    # 標準化為 x³ + px + q = 0 的形式
    # 首先除以 a
    b, c, d = b/a, c/a, d/a
    
    # 使用 Tschirnhaus 變換消除二次項: x = t - b/3
    p = c - b**2 / 3
    q = d + 2*b**3 / 27 - b*c / 3
    
    # 計算判別式
    discriminant = -(4*p**3 + 27*q**2)
    
    # 使用 Cardano 公式
    # 計算輔助量
    Q = cmath.sqrt(-p/3)
    R = q / 2
    
    # 計算 S 和 T
    inside = cmath.sqrt(R**2 + Q**6)
    S = (R + inside) ** (1/3)
    T = (R - inside) ** (1/3)
    
    # 三個立方根的單位根
    omega = cmath.exp(2j * cmath.pi / 3)  # e^(2πi/3)
    
    # 計算三個根（在變換後的坐標系中）
    t1 = S + T
    t2 = omega * S + omega**2 * T
    t3 = omega**2 * S + omega * T
    
    # 變換回原坐標系: x = t - b/3
    shift = b / 3
    x1 = t1 - shift
    x2 = t2 - shift
    x3 = t3 - shift
    
    # 將接近實數的複數轉換為實數
    roots = []
    for root in [x1, x2, x3]:
        if abs(root.imag) < 1e-10:
            roots.append(root.real)
        else:
            roots.append(root)
    
    return roots


# 測試範例
if __name__ == "__main__":
    # 範例 1: x³ - 6x² + 11x - 6 = 0，根為 1, 2, 3
    print("範例 1: x³ - 6x² + 11x - 6 = 0")
    roots = root3(1, -6, 11, -6)
    print(f"根: {roots}\n")
    
    # 範例 2: x³ - 1 = 0，根為 1, (-1±√3i)/2
    print("範例 2: x³ - 1 = 0")
    roots = root3(1, 0, 0, -1)
    print(f"根: {roots}\n")
    
    # 範例 3: x³ + x² - x - 1 = 0
    print("範例 3: x³ + x² - x - 1 = 0")
    roots = root3(1, 1, -1, -1)
    print(f"根: {roots}\n")
    
    # 驗證範例 1 的根
    print("驗證範例 1:")
    a, b, c, d = 1, -6, 11, -6
    for i, root in enumerate(root3(a, b, c, d), 1):
        value = a*root**3 + b*root**2 + c*root + d
        print(f"f({root:.6f}) = {value:.10f}")