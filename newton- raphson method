# newton-raphson-method
def fun(x):
  f=pow(x,2)-2
  return f
  
  h=1e-6
def deriv(x):
  fprime=(fun(x+h)-fun(x-h))/(2*h)
  return (fprime)
  
  def newt(x0):
  newx = x0 - fun(x0)/deriv(x0)
  return newx

def solve(x0):
  tol=1e-5
  new = newt(x0)
  last = x0
  
  while(abs(new-last) > tol):
    print(last)
    last = new
    new = newt(new)
  
  r = new  
    
  return r
