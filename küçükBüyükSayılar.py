largest = None
smallest = None

while True:
    number = input("Enter number")
    if number == "done":
        break
    try:
        number1 = int(number)
    except:
        print("Invalid input")
        continue
        
    if largest is None:
        largest = number1
    elif number1 > largest:
        largest = number1
   
    
    if smallest is None:
        smallest = number1
    elif number1 < smallest:
        smallest = number1
        
        
        
print("Maximum is",largest) 
print("Minimum is",smallest)
  	   

       
