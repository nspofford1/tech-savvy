
import cmath

#Making each variable possible numbers
print('Solve the quadratic equation: ax**2 + bx + c = 0')
a=float(input('Enter a:'))
b=float(input('Enter b:'))
c=float(input('Enter c:'))

#The direct equation
equation=(b**2)-(4*a*c)


#Defining what each solution is a function of
OneSolution=(-b-cmath.sqrt(equation))/(2*a)
SecondSolution=(-b+cmath.sqrt(equation))/(2*a)


#Here Are the Two Solutions
print(OneSolution)
print(SecondSolution)

def quadratic(a,b,c):   
print ("a", 5)
print ("b", 4)
print ("b",3)
return;   