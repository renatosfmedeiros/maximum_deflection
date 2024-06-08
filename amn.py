import math

E = float(input("Insira o Modulo de Elasticidade (GPa): ")
          ) * 10**9  # GigaPascals
v = float(input("Insira o coeficiente de Poisson: "))  # Poisson's ratio
# mm, thickness of the plate
t = float(input("Insira a espessura t em mm: "))
# Pascal, distributed load
q_0 = float(input("Insira a carga em Pascal: "))
a = float(input("Insira o valor do a em mm: "))  # mm, major axis
b = float(input("Insira o valor do b em mm: "))  # mm, minor axis

w_max_analitycal = float(
    input("Insira o valor do Ansys para Wmax (deflexao maxima): "))

sigma_x_max_analitycal = float(
    input("Insira o valor do Ansys para sigma x maximo (tensao normal maxima em x): "))

sigma_y_max_analitycal = float(
    input("Insira o valor do Ansys para sigma y maximo (tensao normal maxima em y): "))

results = []

print("\nMaximum Deflection:\n")

for m in [1, 3, 5]:
    for n in [1, 3, 5]:
        amn = math.sin((m*math.pi)/2)*math.sin((n*math.pi)/2) / \
            ((m*n) * ((m**2 / a ** 2) + (n**2 / b**2)) ** 2)
        label = f"a{m}{n}"
        print(f"{label}: {amn}")
        results.append(amn)

print(f"\nSum of all amn values: \n{sum(results)}\n")

print("\nFlexural Rigidity:\n")

D = E * t ** 3 / (12 * (1 - v ** 2))

print(f"D: {D}\n")

w_max = 16 * q_0 / (math.pi ** 6 * D) * sum(results)

print(f"Wmax: {w_max}" + " mm\n")

print("Bending Moments:\n")

print("Mx_max: \n")

total_amn_mx_max = 0

for m in [1, 3, 5]:
    for n in [1, 3, 5]:
        amn_mx_max = (((m ** 2 / a ** 2) + v * (n ** 2 / b ** 2)) * (math.sin(m * math.pi / 2)
                      * math.sin(n * math.pi / 2))) / ((m * n) * ((m ** 2 / a ** 2) + (n ** 2 / b ** 2)) ** 2)
        print(f"Mx_max: amn value for m={m}, n={n}: {amn_mx_max}")
        total_amn_mx_max += amn_mx_max

print(f"\nTotal amn_mx_max: {total_amn_mx_max}" + " mm^2\n")

mx_max = ((16 * q_0) / math.pi ** 4) * total_amn_mx_max

print(f"Mx_max: {mx_max}" + " Nmm/mm\n")

print("My_max: \n")

total_amn_my_max = 0

for m in [1, 3, 5]:
    for n in [1, 3, 5]:
        amn_my_max = ((v * (m ** 2 / a ** 2) + (n ** 2 / b ** 2)) * (math.sin(m * math.pi / 2)
                      * math.sin(n * math.pi / 2))) / ((m * n) * ((m ** 2 / a ** 2) + (n ** 2 / b ** 2)) ** 2)
        print(f"My_max: amn value for m={m}, n={n}: {amn_my_max}")
        total_amn_my_max += amn_my_max

print(f"\nTotal amn_my_max: {total_amn_my_max}" + " mm^2\n")

my_max = ((16 * q_0) / math.pi ** 4) * total_amn_my_max

print(f"My_max: {my_max}" + " Nmm/mm\n")

print("Maximum normal stress:\n")

sigma_x_max = (6 * mx_max) / (t ** 2) / 1e6

print(f"Sigma_x_max: {sigma_x_max}" + " MPa\n")

sigma_y_max = (6 * my_max) / (t ** 2) / 1e6

print(f"Sigma_y_max: {sigma_y_max}" + " MPa\n")

print("Error:\n")

error_w_max = abs(((w_max - w_max_analitycal) / w_max_analitycal)) * 100

error_sigma_x_max = abs(
    ((sigma_x_max - sigma_x_max_analitycal) / sigma_x_max_analitycal)) * 100

error_sigma_y_max = abs(
    ((sigma_y_max - sigma_y_max_analitycal) / sigma_y_max_analitycal)) * 100

print(f"Error in W_max: {error_w_max:.2f}%")

print(f"Error in Sigma_x_max: {error_sigma_x_max:.2f}%")

print(f"Error in Sigma_y_max: {error_sigma_y_max:.2f}%")



"""
Insira o Modulo de Elasticidade (GPa): 200
Insira o coeficiente de Poisson: 0.3
Insira a espessura t em mm: 0.635
Insira a carga em Pascal: 52
Insira o valor do a em mm: 445
Insira o valor do b em mm: 355
Insira o valor do Ansys para Wmax (deflexao maxima): 1.0647
Insira o valor do Ansys para sigma x maximo (tensao normal maxima em x): 4.8975
Insira o valor do Ansys para sigma y maximo (tensao normal maxima em y): 6.4627

Maximum Deflection:

a11: 5931020219.121278
a13: -57011393.886986636
a15: 4833135.890877436
a31: -116966297.71872146
a33: 8135830.204555938
a35: -1121404.8850018058
a51: 11108206.296482136
a53: -1706343.168847223
a55: 379585.29402376193

Sum of all amn values:
5778671537.14766


Flexural Rigidity:

D: 4689521520.146521

Wmax: 1.0664084227625676 mm

Bending Moments:

Mx_max:

Mx_max: amn value for m=1, n=1: 44069.541284044506
Mx_max: amn value for m=1, n=3: -1509.3303606070835
Mx_max: amn value for m=1, n=5: 312.0362863811926
Mx_max: amn value for m=3, n=1: -5594.4146266937805
Mx_max: amn value for m=3, n=3: 544.0684109141298
Mx_max: amn value for m=3, n=5: -117.70356344821768
Mx_max: amn value for m=5, n=1: 1428.8170962370564
Mx_max: amn value for m=5, n=3: -251.97741334154858
Mx_max: amn value for m=5, n=5: 70.51126605447124

Total amn_mx_max: 38951.54837954072 mm^2

Mx_max: 332696.7525080938 Nmm/mm

My_max:

My_max: amn value for m=1, n=1: 56047.51106127257
My_max: amn value for m=1, n=3: -4157.804590700835
My_max: amn value for m=1, n=5: 966.0873113653529
My_max: amn value for m=3, n=1: -2522.9134054573433
My_max: amn value for m=3, n=3: 691.9445810033652
My_max: amn value for m=3, n=5: -237.74678523197437
My_max: amn value for m=5, n=1: 508.85514854815517
My_max: amn value for m=5, n=3: -186.48352793310337
My_max: amn value for m=5, n=5: 89.67601769803613

Total amn_my_max: 51199.12581056423 mm^2

My_max: 437306.9517661339 Nmm/mm

Maximum normal stress:

Sigma_x_max: 4.950537578395592 MPa

Sigma_y_max: 6.507140456560986 MPa

Error:

Error in W_max: 0.16%
Error in Sigma_x_max: 1.08%
Error in Sigma_y_max: 0.69%

"""