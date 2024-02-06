class Motor:

    def __init__(self):
        self.pornit = False

    def porneste(self):
        self.pornit = True

    def opreste(self):
        self.pornit = False


class Avion:

    def __init__(self, motoare):
        self.motoare = motoare

    def porneste(self):
        for motor in self.motoare:
            motor.porneste()

    def opreste(self):
        self._opreste_motoare(self.motoare, fortat=True)

    def _opreste_motoare(self, care_motoare, fortat=False):
        for motor in care_motoare:
            motor.opreste()

    def num_motoare_active(self):
        return len([motor for motor in self.motoare if motor.pornit])


motor_1 = Motor()
motor_2 = Motor()
air_moldova = Avion([motor_1, motor_2])

print(air_moldova.num_motoare_active())
air_moldova.porneste()
print(air_moldova.num_motoare_active())
motor_1.opreste()
motor_2.opreste()
print(air_moldova.num_motoare_active())

air_moldova.opreste()

#
info = [1, 2, 3, 4]
sorted_info = sorted(info, reverse=True)

info.sort()
