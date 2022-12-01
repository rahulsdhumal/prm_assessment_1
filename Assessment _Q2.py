def validate_triangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True       
a = int(input("Enter 1st side of triangle : "))
b = int(input("Enter 2nd side of triangle : "))
c = int(input("Enter 3rd side of triangle : "))

if validate_triangle(a, b, c):
    print("Valid Triangle")
else:
    print("Invalid Triangle")

def validate_rectangle(l1,b1,l2,b2):
    if (l1 == l2 and b1 == b2) :
        return True
    else:
        return False       
l1 = int(input("\nEnter Length (l1) of Rectangle : "))
b1 = int(input("Enter breadth (b1) of Rectangle : "))
l2 = int(input("Enter Length (l2) of Rectangle : "))
b2 = int(input("Enter breadth (b2) of Rectangle : "))
if validate_rectangle(l1,b1,l2,b2):
    print("Valid Rectangle")
else:
    print("Invalid Rectangle")