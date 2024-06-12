class Band:
    def __init__(self, name, hometown):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Band name must be a non-empty string.")
        if not isinstance(hometown, str) or len(hometown) == 0:
            raise Exception("Hometown must be a non-empty string.")
        self.name = name
        self.hometown = hometown
        self._concerts = []

    def add_concert(self, concert):
        if not isinstance(concert, Concert):
            raise Exception("Concert must be an instance of Concert.")
        self._concerts.append(concert)

    @property
    def concerts(self):
        return self._concerts if self._concerts else None

    @property
    def venues(self):
        if not self._concerts:
            return None
        venues = list(set(concert.venue for concert in self._concerts))
        return venues

    def play_in_venue(self, venue, date):
        if not isinstance(venue, Venue):
            raise Exception("Venue must be an instance of Venue.")
        concert = Concert(date, self, venue)
        self.add_concert(concert)
        venue.add_concert(concert)
        return concert

    def all_introductions(self):
        if not self._concerts:
            return None
        return [concert.introduction() for concert in self._concerts]