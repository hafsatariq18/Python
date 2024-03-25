def fibonacchi(f):
  if f == 0:
   return 0
  elif f==1:
   return 1
  else:
   return fibonacchi(f-1) + fibonacchi(f-2)

print (fibonacchi(10))
print (fibonacchi(9))