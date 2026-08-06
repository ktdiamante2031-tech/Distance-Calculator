import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

x_difference_squared = math.pow(x2 - x1, 2)
y_difference_squared = math.pow(y2 - y1, 2)
distance = math.sqrt(x_difference_squared + y_difference_squared)

print(f"\nThe distance between the two points is {distance:.2f}")

"""
Reflection and evaluation
Using a library is more practical than writing all calculations from scratch because they save us time, ensuring high-quality, and  
better performance code. Libraries provide pre-tested and optimized functions so the coder can focus on core project goals instead 
of fixing math or logic errors. Mainly, code libraries allow us to reuse code that has already been written and tested, saving effort 
to other code.

Guide Questions
1.The math library simplified my program by making me not have to make very long code for square roots.
2. The library made the powers and square roots easier to do otherwise the code would have been very large and incomprehensible.
3. The program would be so so so much difficult without .pow() and .sqrt() and I would have researched the fast inverse root method 
which I dont know how to and make this code much more larger and it will become code sphagetthi.
"""
