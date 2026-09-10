# Formules pour le calcul de frais de port
#def calculate_shipping_cost(weight_kg, distance_km, express=false):

# jusqu'à 1kg 5$ ; de 1 à 5kg 10$ ; plus de 5kg 15$


poids = float("Entrez le poids du colis en kg svp : " ))

if poid <= 1:
  frais_port = 5
else poids <=5:
    frais_port = 10
else:
  frais_port = 15

print("Les frais de port sont de :", frais_port, "$")
