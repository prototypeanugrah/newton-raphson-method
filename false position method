def fun(x):
  f = x**2 - 3*x +2
  return f

def denom(l,u):
  d = fun(l) - fun(u)
  return d  
  
  def num(l,u):
  n = fun(u)*(l-u)
  return n

def solve(l,u):
  c = u - num(l,u)/denom(l,u)
  fl = fun(l)
  fu = fun(u)
      
  if(fl*fu<0):
    for i in range(20):
      tol=1e-5
      fc = fun(c)

      if(fl*fc>0):
        l=c
      elif(fu*fc>0):
        u=c
    
      c = u - num(l,u)/denom(l,u)
    
      if(abs(fc) <= tol):
         break
  else:
    break
  
  return c
