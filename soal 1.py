# Menghitung Jarak fokus lensa
n = 1.50
R1 = 22
R2 = 17.5

#Mencari nilai 1/f
f_inv = (n - 1) * (1/R1 + 1/R2)

#Mencari nilai f
f = 1 / f_inv  

# Output the result
print(f"Nilai f = {f:.2f} cm")
