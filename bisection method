def fun(x):
  f = x**2 - 2
  return f

def solve(a,b):
  
  tol = 1e-5
  
  c= (a+b)/2
  
  for i in range(54):
    fa = fun(a)
    fb = fun(b)
    fc = fun(c)
    
    if((fa*fb)<0):
      if((fc*fa) > 0):
        a=c
      elif((fc*fb) > 0):  
        b=c
      c=(a+b)/2
      if(abs(fc) <= tol):
        break
    
    else:
      break
    
  return c
