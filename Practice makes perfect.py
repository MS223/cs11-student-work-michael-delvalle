 def is_even (x):
     if x % 2 == 0:
         return 'true'
     else:
         if x % 2 == 1:
             return 'false'

def is_int(x):
    if x == int(x):
        return True
    else:
        return False
print is_int(3.5)
