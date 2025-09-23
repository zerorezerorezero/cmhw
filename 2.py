import cmath

def root2(a,b,c):
    R=b**2-4*a*c # 判別式
    if (R>0): # 兩實根
        x1=(-b+R**0.5)/(2*a)
        x2=(-b-R**0.5)/(2*a)
        f1=a*(x1**2)+b*x1+c
        f2=a*(x2**2)+b*x2+c
        r1=cmath.isclose(f1, 0, rel_tol=1e-09, abs_tol=0.0) # 裡面原本的 *, 的部分會出錯誤提示先刪掉了
        r2=cmath.isclose(f2, 0, rel_tol=1e-09, abs_tol=0.0)
        print("x1={},x2={},f1={},f2={},f1-check={},f2-check={}".format(x1,x2,f1,f2,r1,r2))
    elif(R==0): # 重根
        x=-b/(2*a)
        f=a*(x**2)+b*x+c
        r=cmath.isclose(f, 0, rel_tol=1e-09, abs_tol=0.0)
        print("x={},f={},f-check={}".format(x,f,r))
    else: # 虛根
        x1=(-b+(cmath.sqrt(R)))/(2*a)
        x2=(-b-(cmath.sqrt(R)))/(2*a)
        f1=a*(x1**2)+b*x1+c
        f2=a*(x2**2)+b*x2+c
        r1=cmath.isclose(f1, 0, rel_tol=1e-09, abs_tol=0.0)
        r2=cmath.isclose(f2, 0, rel_tol=1e-09, abs_tol=0.0) 
        print("x1={},x2={},f1={},f2={},f1-check={},f2-check={}".format(x1,x2,f1,f2,r1,r2))

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

root2(a,b,c)


