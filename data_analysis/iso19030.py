import numpy as np
import pandas as pd

class Init():
    """데이터베이스로 부터 데이터 요청함. 데이터 목록은 아래와 같음.

    LATITUDE, LONGITUDE, SPEED OVER GROUND, LONGITUDINAL GROUND SPEED, LONGITUDINAL WATER SPEED, HEADING GYRO, HEADING GPS, RUDDER ANGLE, SEA DEPTH,
    REL' WIND SPEED, REL' WIND DIRECTION, TRUE WIND SPEED, TRUE WIND DIRECTION, FWD' DRAFT, AFT' DRAFT, PROPELLER RPM, SHAFT TORQUE, SHAFT THRUST, SHAFT POWER, 
    SEAWATER TEMP, AIR_TEMP, AIR_PRESSURE, TRUE CURRENT SPEED, TRUE CURRENT DIRECTION, TOTAL WAVE HEIGHT, TOTAL WAVE DIRECTION, TOTAL WAVE PERIOD, SWELL WAVE HEIGHT, 
    SWELL WAVE DIRECTION, SWELL WAVE PERIOD, WIND WAVE HEIGHT, WIND WAVE DIRECTION, WIND WAVE PERIOD.
    Parameters
    ----------
    callSign : string, default='3ewb4'
        요청하고자 하는 선박의 Call Sign입니다.
    beginDate : string, default='2017-01-10'
        요청하고자 하는 시작날짜입니다.
    endDate : string, default='2017-02-10'
        요청하고자 하는 마지막 날짜입니다.
    Example
    ----------
    dbCon = sqlcon('3ewb4','2017-01-01','2017-02-01')

    shipData = dbCon.query(isShuffle=True, isPD= False, meanTime = 10)
    """

    def __init__(self, callSign='3ewb4', beginDate='2017-01-01', endDate='2017-01-10', speedCheck=7, draftForeCheck=10, draftAftCheck=10, windSpeedCheck=7.9, waveHeightCheck=2, waterdepthCheck=300, draftType='B'):
        self.callSign = callSign
        self.beginDate = beginDate
        self.endDate = endDate
        self.speedCheck = speedCheck
        self.draftForeCheck = draftForeCheck
        self.draftAftCheck = draftAftCheck
        self.windSpeedCheck = windSpeedCheck
        self.waveHeightCheck = waveHeightCheck
        self.waterdepthCheck = waterdepthCheck
        self.draftType = draftType


def make_datablock(self):


def chauvenet_filter(self):


def validation_filter(self):


def wind_Correct(self):


def calculate_pv(self):


def make_speedPowerTable(self):

def expected_speed(self):


def reference_filter(self):

def calculate_pi(self)


def calculate_bhp(self):


def  calculate_power(self):


def correction_wind(self):