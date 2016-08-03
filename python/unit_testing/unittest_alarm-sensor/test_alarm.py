'''
Created on Dec 16, 2014

@author: remusav
'''

import unittest
from alarm import Alarm

class AlarmTest(unittest.TestCase):


    def testAlarmIsOffByDefault(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)

    def testCheckTooLowPressureSoundsAlarm(self):
        alarm = Alarm(sensor=TestSensor(15))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def testCheckTooHighPressureSoundsAlarm(self):
        alarm = Alarm(sensor=TestSensor(22))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def testCheckNormalPressureDoesntSoundAlarm(self):
        alarm = Alarm(sensor=TestSensor(18))
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)

class TestSensor:
    def __init__(self, pressure):
        self.pressure = pressure
    def sample_pressure(self):
        return self.pressure

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()