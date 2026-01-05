#input
x1_input = int(input("x1? "))
y1_input = int(input("y1? "))
x2_input = int(input("x2? "))
y2_input = int(input("y2? "))

#delta
deltx = x2_input - x1_input
delty = y2_input - y1_input

#steps & inc
steps = max(abs(deltx), abs(delty))
X_inc = deltx / steps
Y_inc = delty / steps

#calculating
x = x1_input
y = y1_input
print(int(x), int(y))
for i in range(steps):
    x = x + X_inc
    y = y + Y_inc
    
#output
    print (round(x), round(y))