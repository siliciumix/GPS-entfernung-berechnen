import math

def calculate_distance(lat1, lon1, lat2, lon2):
    # Konstanten für die Berechnung der Erdkrümmung
    R = 6371  # Radius der Erde in Kilometern

    # Umwandlung der Koordinaten in Radiant
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

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

# Entfernung berechnen
distance = calculate_distance(start_lat, start_lon, end_lat, end_lon)

# Ergebnis ausgeben
print(f"Die Entfernung zwischen der Davidwache in Hamburg und dem Viktualienmarkt in München beträgt {distance:.2f} km.")
