import random

class Sensor(object):
    
    _OFFSET = 16
    
    def sample_presure(self):
        pressure_telemetry_value = self.ssample_pressure()
        return Sensor._OFFSET + pressure_telemetry_value
    
    @staticmethod
    def sample_actual_pressure():
        # placeholder implementation that simulate a real sensor in a real tire
        pressure_telemetry_value = 6 * random.random() * random.random()
        return pressure_telemetry_value