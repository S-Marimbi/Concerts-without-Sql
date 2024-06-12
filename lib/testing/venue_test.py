class Venue:
    def __init__(self, name, city):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Venue name must be a non-empty string.")
        if not isinstance(city, str) or len(city) == 0:
            raise Exception("City must be a non-empty string.")
        self.name = name
        self.city = city
        self._concerts = []

    def add_concert(self, concert):
        if not isinstance(concert, Concert):
            raise Exception("Concert must be an instance of Concert.")
        self._concerts.append(concert)

    def concerts(self):
        return self._concerts if self._concerts else None

    def bands(self):
        if not self._concerts:
            return None
        bands = list(set(concert.band for concert in self._concerts))
        return bands

    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None