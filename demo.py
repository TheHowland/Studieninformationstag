from lcapyInskale import Circuit
cct = Circuit("04_resistor_mixed_simple.txt")


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

R1 = 10
R2 = 15
R3 = 30
R4 = 100
R5 = 150

Rs1 = series(R1, R2, R3)
Rs2 = parallel(R4, R5)
R_total = series(Rs1, Rs2)

U_total = 10
I_total = current(R_total, U_total)

Us1 = voltage(Rs1, I_total)
Is1 = I_total

Us2 = voltage(Rs2, I_total)
Is2 = I_total

U1 = voltage(R1, I_total)
I1 = I_total

U2 = voltage(R2, I_total)
I2 = I_total

U3 = voltage(R3, I_total)
I3 = I_total

U4 = Us2
I4 = current(R4, Us2)

U5 = Us2
I5 = current(R5, Us2)

print(f"R1:\t\t\t {R1:.4f} Ohm, U1: {U1:.4f} V, I1: {I1:.4f} A")
print(f"R2:\t\t\t {R2:.4f} Ohm, U2: {U2:.4f} V, I2: {I2:.4f} A")
print(f"R3:\t\t\t {R3:.4f} Ohm, U3: {U3:.4f} V, I3: {I3:.4f} A")
print(f"R4:\t\t\t {R4:.4f} Ohm, U4: {U4:.4f} V, I4: {I4:.4f} A")
print(f"R5:\t\t\t {R5:.4f} Ohm, U5: {U5:.4f} V, I5: {I5:.4f} A")
print(f"Rs1:\t\t {Rs1:.4f} Ohm, Us1: {Us1:.4f} V, Is1: {Is1:.4f} A")
print(f"Rs2:\t\t {Rs2:.4f} Ohm, Us2: {Us2:.4f} V, Is2: {Is2:.4f} A")
print(f"R_total:\t {R_total:.4f} Ohm, U_total: {U_total:.4f} V, I_total: {I_total:.4f} A")
pass



