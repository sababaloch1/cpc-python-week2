# Task 5: Dictionary of Dortmund events and dates, then filter for 19.09.2026

# Create a dictionary of events and their dates
dortmund_events = {
    "DEW21 Museumsnacht": "19.09.2026",
    "DASA Arbeitswelt Ausstellung – Physikanten Show": "19.09.2026",
    "Dortmunder U – Fassadenmapping 'what is wisdom'": "19.09.2026",
    "Handwerkskammer Dortmund – Führungen durch die Werkstätten": "19.09.2026",
    "Polizeipräsidium Dortmund – Museumsnacht Programm": "19.09.2026",
    "Museum für Kunst und Kulturgeschichte – KONSUM. Ausstellung": "19.09.2026",
    "Kindermuseum Adlerturm – Museumsrallye": "19.09.2026",
    "Naturmuseum Dortmund – Nächtliche Museumstour": "19.09.2026",
    "Hoesch-Museum – Stahlgeschichte Führung": "19.09.2026",
    "Zeche Zollern – Highland Games & Dudelsackmusik": "19.09.2026",
    "BORUSSEUM – Borussia Dortmund Geschichte": "19.09.2026",
    "Deutsches Fußballmuseum – Kurzführungen": "19.09.2026",
    "Phoenix des Lumières – Immersive Kunst": "19.09.2026",
    "Dortmunder Kunstverein – Zeitgenössische Kunst": "19.09.2026",
    "Künstler*innenhaus Dortmund – Ausstellung 'Widerstand und Wunden'": "19.09.2026",
    "St. Reinoldi – Lesung mit Saša Stanišić": "19.09.2026",
    "Baukunstarchiv NRW – Frank Goosen liest": "19.09.2026",
    "Stadt- und Landesbibliothek – Lesungen & Führungen": "19.09.2026",
    "VHS Dortmund – VR-Welten & KI-Kunst": "19.09.2026",
    "domicil – Jazz, Clubsound & Ruhrpott-Balkan": "19.09.2026",
    "Konzerthaus Dortmund – Museumsnacht Konzert": "19.09.2026",
    "Friedensplatz – Open-Air-Party mit Marquess": "19.09.2026",
    "DiS# Festival 2026 – TANZORCHESTER PASCHULKE": "19.09.2026",
    "Hannes Weyland – Jubiläumskonzert 'Fluchtwagen'": "19.09.2026",
    "CantaStrophe – Chorauftritt": "19.09.2026",
    "Phoenix Harmonists – Männerchor": "19.09.2026",
    "Blaze Bayley – Iron Maiden Anniversary": "19.09.2026",
    "The Kerry Kenny Band": "19.09.2026",
    "Julian Sas – Blue Notez Club": "19.09.2026",
    "Dronetale – Theater im Depot": "19.09.2026",
    "The Prom – Naturbühne Hohensyburg": "19.09.2026",
    "Impro-Theater Workshop – Union Salon": "19.09.2026",
    "Rebecca – Opernhaus Dortmund": "19.09.2026",
    "Wilfried Schmickler – RuhrHOCHdeutsch Spiegelzelt": "19.09.2026",
    "Whitney Houston meets Pink – Hansa Theater Hörde": "19.09.2026",
    # Add other events that are NOT on 19.09.2026 for demonstration
    "Techno Classica Salon": "24.09.2026",
    "Djelem Djelem – Roma Kulturfestival": "26.09.2026",
    "Dortmunder Museumsnacht – Sonntag": "20.09.2026",
    "nachtfrequenz – Nordi by Night VII": "27.09.2026",
}

# Filter events that are running on 19.09.2026
night_of_museums_events = [
    event for event, date in dortmund_events.items() if date == "19.09.2026"
]

# Display the results
print("Events during the Night of Museums in Dortmund on 19.09.2026:\n")
for event in night_of_museums_events:
    print(f"- {event}")