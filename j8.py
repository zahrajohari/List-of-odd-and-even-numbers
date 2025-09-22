numbers=list(range(0,100))
even_numbers=[]
odd_numbers=[]
for num in numbers:
    if num%2==0:
     even_numbers.append(num)
     
    else :
        odd_numbers.append(num)
        
print("even_numbers:",even_numbers) 
print("odd_numbers:", odd_numbers)