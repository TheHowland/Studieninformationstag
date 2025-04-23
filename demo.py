def parallel(*args):
    resistance = 0
    for arg in args:
        resistance += 1 / arg

    return 1 / resistance

def series(*args):
    resistance = 0
    for arg in args:
        resistance += arg

    return resistance

def current(R, V):
    return V / R

def voltage(R, I):
    return R * I

R1 = 100
R2 = 100
R3 = 100
R4 = 100

Rs1 = series(R1, R2)
Rs2 = parallel(R3, R4)
R_total = series(Rs1, Rs2)

U_total = 10
I_total = current(R_total, U_total)

Is1 = I_total
Us1 = voltage(Rs1, Is1)

Is2 = I_total
Us2 = voltage(Rs2, Is2)

I1 = I_total
U1 = voltage(R1, I1)

I2 = I_total
U2 = voltage(R2, I2)

U3 = Us2
I3 = current(R3, Us2)

U4 = Us2
I4 = current(R4, Us2)

print(f"R1:\t\t {R1:>8.4f} Ohm,\t U1: {U1:>10.4f}\t V, I1: {I1:>10.4f} A")
print(f"R2:\t\t {R2:>8.4f} Ohm,\t U2: {U2:>10.4f}\t V, I2: {I2:>10.4f} A")
print(f"R3:\t\t {R3:>8.4f} Ohm,\t U3: {U3:>10.4f}\t V, I3: {I3:>10.4f} A")
print(f"R4:\t\t {R4:>8.4f} Ohm,\t U4: {U4:>10.4f}\t V, I4: {I4:>10.4f} A")
print(f"Rs1:\t {Rs1:>8.4f} Ohm,\t Us1: {Us1:>9.4f}\t V, Is1: {Is1:9.4f} A")
print(f"Rs2:\t {Rs2:>8.4f} Ohm,\t Us2: {Us2:>9.4f}\t V, Is2: {Is2:>9.4f} A")
print(f"R_tot:\t {R_total:8.4f} Ohm,\t U_tot: {U_total:7.4f}  V, I_tot: {I_total:7.4f} A")
pass



