import math


class BirdVehicle(object):
    def __init__(self, id):
        self.id = id
        self.statics = {'s': [], 'e': [], 'd': []}
        for cls in AbstractStaticUnit.__subclasses__():
            staticUnit = cls(id)
            triggers = staticUnit.getTriggers()
            if 's' in triggers:
                self.statics['s'].append(staticUnit)
            if 'e' in triggers:
                self.statics['e'].append(staticUnit)
            if 'd' in triggers:
                self.statics['d'].append(staticUnit)

    def start(self, data):
        for staticUnit in self.statics['s']:
            staticUnit.start(data)

    def end(self, data):
        for staticUnit in self.statics['e']:
            staticUnit.end(data)

    def drop(self, data):
        for staticUnit in self.statics['d']:
            staticUnit.drop(data)


class BirdManager(object):
    def __init__(self):
        self.birds = {}

    def process_data(self, data):
        if data['id'] not in self.birds:
            self.birds[data['id']] = BirdVehicle(data['id'])
        bird = self.birds[data['id']]
        if data['type'] == 'DROP':
            bird.drop(data)
        elif data['type'] == 'START_RIDE':
            bird.start(data)
        elif data['type'] == 'END_RIDE':
            bird.end(data)

    def load_data(self, fileName):
        with open(fileName, 'r') as f:
            for rawLine in f:
                line = rawLine.split(',')
                data = {}
                data['time'] = int(line[0])
                data['id'] = line[1]
                data['type'] = line[2]
                data['x'] = float(line[3])
                data['y'] = float(line[4])
                data['user'] = line[5]
                self.process_data(data)

    def total_dropped_number(self):
        return len(self.birds)

    def farthest_from_dropped(self):
        return max([(unit.distance, unit.id)
                    for unit in DistanceFromDropped.instances])

    def longest_traveled_distance(self):
        return max([(unit.distance, unit.id)
                    for unit in TravelTimeAndDistance.instances])

    def paid_most(self):
        return max([(unit.paid_sum, unit.id)
                    for unit in PaidDuration.instances])

    def longest_idle(self):
        return max([(unit.idle_sum, unit.id)
                    for unit in IdleDuration.instances])

    def average_speed(self):
        total_time = sum([
            unit.cost_time for unit in TravelTimeAndDistance.instances])
        total_distance = sum([
            unit.distance for unit in TravelTimeAndDistance.instances])
        return total_distance / total_time


class AbstractStatsUnit(object):
    def __init__(self, id):
        self.id = id

    def getTriggers(self):
        raise NotImplementedError()

    def start(self):
        raise NotImplementedError()

    def end(self):
        raise NotImplementedError()

    def drop(self):
        raise NotImplementedError()


class DistanceFromDropped(AbstractStatsUnit):
    instances = []

    def __init__(self, id):
        self.x = None
        self.y = None
        self.distance = None
        self.__class__.instances.append(self)
        super().__init__(id)

    def getTriggers(self):
        return 'sed'

    def start(self, data):
        if self.x is None:
            self.x = data['x']
            self.y = data['y']

    def end(self, data):
        self.distance = \
            ((self.x - data['x'])**2 + (self.y - data['y'])**2)**0.5

    def drop(self, data):
        self.x = data['x']
        self.y = data['y']


class TravelTimeAndDistance(AbstractStatsUnit):
    instances = []

    def __init__(self, id):
        self.x = None
        self.y = None
        self.distance = 0
        self.cost_time = 0
        self.t = 0
        self.__class__.instances.append(self)
        super().__init__(id)

    def getTriggers(self):
        return 'se'

    def start(self, data):
        self.x = data['x']
        self.y = data['y']
        self.t = data['time']

    def end(self, data):
        self.distance += \
            ((self.x - data['x'])**2 + (self.y - data['y'])**2)**0.5
        self.cost_time += data['time'] - self.t


class PaidDuration(AbstractStatsUnit):
    instances = []

    def __init__(self, id):
        self.t = None
        self.paid_sum = 0
        self.__class__.instances.append(self)
        super().__init__(id)

    def getTriggers(self):
        return 'se'

    def start(self, data):
        self.t = data['time']

    def end(self, data):
        d = data['time'] - self.t
        if d >= 60:
            self.paid_sum += 1 + math.ceil(d / 60) * 0.15


class IdleDuration(AbstractStatsUnit):
    instances = []

    def __init__(self, id):
        self.t = None
        self.idle_sum = 0
        self.__class__.instances.append(self)
        super().__init__(id)

    def getTriggers(self):
        return 'dse'

    def drop(self, data):
        self.t = data['time']

    def start(self, data):
        self.idle_sum += data['time'] - self.t

    def end(self, data):
        self.t = data['time']


if __name__ == '__main__':
    b = BirdManager()
    b.load_data('events.txt')
    print(b.total_dropped_number())
    print(b.farthest_from_dropped())
    print(b.longest_traveled_distance())
    print(b.paid_most())
    print(b.longest_idle())
    print(b.average_speed())
