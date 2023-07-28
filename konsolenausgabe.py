import math

# Konstanten für die Berechnung der Erdkrümmung
R = 6371  # Radius der Erde in Kilometern

def calculate_distance(lat1_rad, lon1_rad, lat2_rad, lon2_rad):
    # Differenzen der Koordinaten
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine-Formel
    a = math.sin(dlat/2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c

    return distance

# GPS-Koordinaten der Davidwache in Hamburg
start_lat = 53.549071152736225
start_lon = 9.962645416253864

# GPS-Koordinaten des Viktualienmarkts in München
end_lat = 48.13488
end_lon = 11.57717

# Umwandlung der Koordinaten in Radiant
start_lat_rad = math.radians(start_lat)
start_lon_rad = math.radians(start_lon)
end_lat_rad = math.radians(end_lat)
end_lon_rad = math.radians(end_lon)

# Entfernung berechnen
distance = calculate_distance(start_lat_rad, start_lon_rad, end_lat_rad, end_lon_rad)

# Ergebnis ausgeben
print()
print(f"Die Entfernung zwischen der Davidwache in Hamburg und dem Viktualienmarkt in München beträgt {distance:.2f} km.")
print()