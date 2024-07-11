# Lists of keywords, time of day, vehicle types, and cities by GCC country
keywords = [
    "Compilation",
    "Footage",
    "Drive",
    "Road trip",
    "Dashcam",
    "GoPro",
    "Road",
    "Rush hour",
    "Traffic",
    "Commute"
]

times_of_day = [
    "Morning",
    "Midday",
    "Afternoon",
    "Evening",
    "Night"
]

vehicle_types = [
    "Van",
    "Truck",
    "Bus",
    "Car",
    "Motorcycle",
    "Trailer",
    "Ambulance",
    "Fire truck",
    "Police car",
    "Taxi",
    "SUV",
    "RV"
]

gcc_countries = {
#    "Saudi Arabia": [
#        "Riyadh", "Jeddah", "Mecca", "Medina", "Dammam",
#        "Khobar", "Dhahran", "Jubail", "Tabuk", "Abha"
#    ],
    "United Arab Emirates": [
        "Dubai", "Abu Dhabi", "Sharjah", "Al Ain", "Ajman",
        "Fujairah", "Ras Al Khaimah", "Umm Al Quwain", "Khor Fakkan", "Dibba Al-Fujairah"
    ],
    "Qatar": [
        "Doha", "Al Wakrah", "Al Rayyan", "Al Khor", "Umm Salal",
        "Al Daayen", "Madinat Al Shamal", "Mesaieed", "Al Ruwais", "Zubarah"
    ],
    "Kuwait": [
        "Kuwait City", "Ahmadi", "Farwaniya", "Jahra", "Hawalli",
        "Mubarak Al-Kabeer", "Sabah Al-Salem", "Al Ahmadi", "Salwa", "Al Jahra"
    ],
    "Oman": [
        "Muscat", "Salalah", "Seeb", "Sohar", "Nizwa",
        "Sur", "Rustaq", "Bahla", "Ibri", "Barka"
    ],
    "Bahrain": [
        "Manama", "Riffa", "Muharraq", "Hamad Town", "A'ali",
        "Isa Town", "Sitra", "Budaiya", "Jidhafs", "Al-Malikiyah"
    ]
}

# Generating search strings
search_strings = []

for country, cities in gcc_countries.items():
    for city in cities:
        for time in times_of_day:
            for vehicle in vehicle_types:
                for keyword in keywords:
                    search_string = f"{keyword} {time} {vehicle} {city} {country}"
                    search_strings.append(search_string)

# Printing the first few search strings to verify
for idx, search_str in enumerate(search_strings[:100], start=1):
    print(f"{idx}. {search_str}")
