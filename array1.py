rain = [0.00, 0.04, 0.11, 0.60, 0.87, 0.95, 1.00]

y = float(input("Input Value for Y: "))
for r in rain:
    if (r > y):
        print ("Using For")
        print("First r value greater than y {} is {}".format(y,r))
        break
    
for i in range(0,6):
    if (rain[i] > y):
        print ("Using Range")
        print("First r value greater than y {} is {}".format(y,r))
        break
    
for i in range(0,6):
    if (rain[i] > y):
        print("Y value {} is bounded by rain value {} and {}".format(y,rain[i-1], rain[i]))
        break