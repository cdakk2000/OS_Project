top = 0   # Variable to help calculate Completion Time
a_tat = 0.0  # Average Turn Around Time
a_wt = 0.0  # Average Waiting Time
with open("C:/Users/cdakk/Desktop/STUDIA/skryptowejezyki/Projekt_SO/Algorytmy szeregowania procesow/data_arrivalTime.txt") as f:
    at = [int(x) for x in f.read().split(", ")]  # List of arrival times
with open("C:/Users/cdakk/Desktop/STUDIA/skryptowejezyki/Projekt_SO/Algorytmy szeregowania procesow/data_bursttime.txt") as f:
    bt = [int(x) for x in f.read().split(", ")]  # List of burst times
n = len(at)  # Number of procces
at1 = []  # List to help with sorting procces
bt1 = []  # List to help with sorting procces
bt2 = []  # List to help with sorting procces
clock = 0  # Timer
ptr = 0  # Pointer to help

# Sorting proccesses without knowing about them before
flag = True
while flag:
    for i in range(len(at)):
        if(at[i] == clock):
            at1.append(at[i])
            bt1.append(bt[i])
            bt2.append(bt[i])
    if((at1[ptr] <= clock) and (bt1[ptr] > 0)):
            bt1[ptr] -= 1

    if(bt1[ptr] == 0):
        ptr += 1
        if (ptr == len(bt)):
            flag = False
    clock += 1

# print(at1)
# print(bt2)

ct = []  # Completion Time
tat = []  # Turn Around Time
wt = []  # Waiting Time
t = 0  # Iterator to help sorting procces depending of burst Time
k = 1  # Iterator to help sorting procces depending of burst Time
time = 0  # Iterator to help sorting procces depending of burst Time

# Sorting proccesses depending of burst Time
for j in range(0, len(at1)):
    time = time + bt[j]
    t = bt2[k-1]
    for i in range(k, len(at1)):
        if(time >= at1[i] and bt2[i] < t):
            temp = at1[k]
            at1[k] = at1[i] 
            at1[i] = temp
            temp = bt2[k]
            bt2[k] = bt2[i]
            bt2[i] = temp
    k += 1

# print(at1)
# print(bt2)

#Calculate Completion Times
for i in range(n):
    if i == 0:
        top = top + bt2[i]
        ct.append(top)
    elif i > 0:
        if top < at1[i]:
            top = at1[i] + bt2[i]
            ct.append(top)
        else:
            top = top + bt2[i]
            ct.append(top)

#Calculate Turn Around Time and Waiting Time
for i in range(n):
    var = ct[i] - at1[i]
    tat.append(var)
    var = tat[i] - bt2[i]
    wt.append(var)



# Display proccesses in order
print()
print("   Process Id", "  Arrival Time  ", "  Burst Time  ", "  Completion Time  ", "  Turn Around Time  " , "  Waiting Time")
for i in range(n):
    print("   " + str((i + 1)) + "\t\t\t" + str(at1[i]) + "\t\t" + str(bt2[i]) + "\t\t" + str(ct[i]) + "\t\t" +str(tat[i]) +"\t\t" + str(wt[i]))
    a_tat = a_tat + tat[i]
    a_wt = a_wt + wt[i]

a_tat = a_tat/n
a_wt = a_wt/n

print()
print("Average Trun Around Time : %f" %a_tat)
print("Average Waiting Time : %f" %a_wt)
