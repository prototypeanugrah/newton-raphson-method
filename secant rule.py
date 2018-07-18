


def f(x):
  f = x**3 -3*x
  return f

def solve(xl,xu):
  
  tol=1e-5
  last=xl
  new=xu
  sec = (new - last)/(f(new) - f(last))
  xr = new - f(new)*sec

  while(abs(f(xr)) >= tol):
    last=new
    new=xr
    xr = new - f(new)*sec
       
  return xr 
