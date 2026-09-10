# Formules pour le calcul de frais de port
#def calculate_shipping_cost(weight_kg, distance_km, express=false):

# jusqu'à 1kg 5$ ; de 1 à 5kg 10$ ; plus de 5kg 15$

def calculate_shipping(weight):
  if wieght <= 2:
    return 5
  elif weight <=5:
    return 10
  elif weight <=10:
    return 15
else:
    return 20

weight = float(input("Entrer le poids de votre colis en KG svp: "))

shipping_cost = 
calculate_shipping(weight)

print(f"shipping cost: $
{shipping_cost}")
