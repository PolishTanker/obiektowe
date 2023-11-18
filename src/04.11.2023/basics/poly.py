from loguru import logger


class Room:

    def __init__(self):
        self.occupants = []

    def enter(self, actor: str):
        logger.info(f'Entering room {actor=}')
        self.occupants.append(actor)
        print(self.occupants)

    def leave(self, actor: str):
        logger.info('Leaving room')
        if actor not in self.occupants:
            return RuntimeError
        self.occupants.remove(actor)
        print(self.occupants)

    def get_occupants(self) -> list[str]:
        return []


class FixedCapacityRoom(Room):

    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        super().__init__()

    def enter(self, actor: str):
        logger.info(f'Enterning fixed capacity room; current actor count: {len(self.occupants)}')
        if self.capacity == len(self.occupants):
            raise RuntimeError('Cannot enter; room full')
    



class TemperatureStabilizedRoom(Room):
    pass


class FreezerRoom(Room):
    pass


class PremiumRoom(Room):
    pass


r = FixedCapacityRoom(2)
r.enter('gg')
r.leave('gg')
r.leave('gg')