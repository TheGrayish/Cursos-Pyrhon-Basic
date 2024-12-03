def fibonacci(num):
    if num==0 or num==1:
     return num
    else:
       return fibonacci(num-2) + fibonacci(num - 1)
    
for x in range(10):
   print("Lista:",x,"Serie:",fibonacci(x))

