def truthy(): 
  print("True")
  
def falsey(): 
  print("False")

def _if(bool_value, func1, func2):
    if bool_value:
        func1()
    else:
        func2()  
        
_if(True, truthy, falsey)
