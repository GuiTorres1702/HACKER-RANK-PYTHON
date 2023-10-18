year = int(input(''))

def is_leap(year):
    
    leap = False
		
    a = year % 4 == 0
    b = year % 100 == 0
    c = year % 400 == 0
    
    if a and b and c:
        leap = True
    elif not a:
        leap = False
    elif a and not b:
        leap = True
    elif a and b and not c:
        leap = False
        
    return leap

print(is_leap(year))