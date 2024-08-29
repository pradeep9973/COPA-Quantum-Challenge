import airportsdata as ad


class Airport:
    def __init__(self, iata: str, name: str, city: str, coordinates: tuple, nearby_airports: set = None) -> None:
        self.iata = iata
        self.name = name
        self.city = city
        self.coordinates = coordinates
        self.nearby_airports = nearby_airports

    def add_nearby_airport(self, airport) -> None:
        if airport not in self.nearby_airports:
            self.nearby_airports.add(airport)

    def __repr__(self) -> str:
        return f'({self.name}, {self.iata}, {self.city}, {self.coordinates}, {self.nearby_airports})'
    

