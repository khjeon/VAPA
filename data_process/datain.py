## writer : lee sang bong / lab021
import pymssql
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


    # ask for data from database
    def queryAll(self, tableName = 'min', isShuffle = False, isPD = True, meanTime = 0):
        """pandas 데이터 형태로 데이터 요청
        Parameters
        ----------
        tableName : string, default = "min"
            10초 데이터 or 10분 데이터를 요청할 것인지 선택
        isShuffle : boolean, default = "True"
            데이터를 무작위로 섞는 여부. True - 데이터를 섞음, False - 데이터를 섞지 않고 시간 순으로 정렬.
        isPD : boolean, default = "False"
            데이터 리턴은 PANDAS 형태로 가공할 것인지 여부. True - List 형태로 리턴, False - Pandas DataFrame 형태로 리턴.
        meanTime : int, default = 0
            데이터를 분단위로 normalizing 함. 예) meanTime = 10 - 10분 블록으로 평균을 냄.
        Returns
        -------
        result : DataFrame(Pandas) or array
            요청한 선박, 날짜에 해당하는 데이터.
        """
        conn = pymssql.connect(server='218.39.195.13:21000', user='sa', password='@120bal@', database='SHIP_DB_MARS')
    
        features = "[TIME_STAMP], [SPEED_VG], [SPEED_LW], [COURSE_OVER_GROUND], [SHIP_HEADING],[RUDDER_ANGLE], [WATER_DEPTH],\
        [REL_WIND_SPEED],[REL_WIND_DIR], [ABS_WIND_SPEED], [ABS_WIND_DIR],[DRAFT_FORE], [DRAFT_AFT], [SHAFT_REV],[SHAFT_TORQUE], [SHAFT_THRUST], [SHAFT_POWER], [BHP_BY_FOC],\
        [SST],[AIR_TEMP], [AIR_PRESSURE], [CURRENT_VEL],[CURRENT_DIR], [HTSGW], [MWSDIR],[MWSPER], [SWELL_SEQ1], [SWDIR_SEQ1], [SWDIR_SEQ1],[SWPER_SEQ1], [WVHGT], [WVDIR], [WVPER],[CURRENT_VEL_TAIL_TO_HEADING_NOWCAST]"

        if (tableName == 'sec'):
            if (self.draftType == "B"):
                stmt = "SELECT" + features + "FROM [SHIP_DB_MARS].[dbo].[SAILING_DATA] WHERE CALLSIGN ='"+self.callSign+"' AND TIME_STAMP > '"  + self.beginDate + "' AND TIME_STAMP < '"+ self.endDate +"' AND SPEED_VG >= '"+ self.speedCheck +"' AND DRAFT_FORE < '"+ self.draftForeCheck +"' AND DRAFT_AFT < '"+ self.draftAftCheck +"' AND ABS_WIND_SPEED < '"+ self.windSpeedCheck +"' AND HTSGW < '"+ self.waveHeightCheck +"' AND WATER_DEPTH > '"+ self.waterdepthCheck +"' AND AT_SEA = 1 AND IS_GOOD_DATA_FOR_ANALYSIS = 1 ORDER BY TIME_STAMP"
            else:
                stmt = "SELECT" + features + "FROM [SHIP_DB_MARS].[dbo].[SAILING_DATA] WHERE CALLSIGN ='"+self.callSign+"' AND TIME_STAMP > '"  + self.beginDate + "' AND TIME_STAMP < '"+ self.endDate +"' AND SPEED_VG >= '"+ self.speedCheck +"' AND DRAFT_FORE > '"+ self.draftForeCheck +"' AND DRAFT_AFT > '"+ self.draftAftCheck +"' AND ABS_WIND_SPEED < '"+ self.windSpeedCheck +"' AND HTSGW < '"+ self.waveHeightCheck +"' AND WATER_DEPTH > '"+ self.waterdepthCheck +"' AND AT_SEA = 1 AND IS_GOOD_DATA_FOR_ANALYSIS = 1 ORDER BY TIME_STAMP"
        else:
            if (self.draftType == "B"):
                stmt = "SELECT" + features + "FROM [SHIP_DB_MARS].[dbo].[SAILING_DATA_FOR_15016] WHERE CALLSIGN ='"+self.callSign+"' AND TIME_STAMP > '"  + self.beginDate + "' AND TIME_STAMP < '"+ self.endDate +"' AND SPEED_VG >= '"+ self.speedCheck +"' AND DRAFT_FORE < '"+ self.draftForeCheck +"' AND DRAFT_AFT < '"+ self.draftAftCheck +"' AND ABS_WIND_SPEED < '"+ self.windSpeedCheck +"' AND HTSGW < '"+ self.waveHeightCheck +"' AND WATER_DEPTH > '"+ self.waterdepthCheck +"' ORDER BY TIME_STAMP"
            else:
                stmt = "SELECT" + features + "FROM [SHIP_DB_MARS].[dbo].[SAILING_DATA_FOR_15016] WHERE CALLSIGN ='"+self.callSign+"' AND TIME_STAMP > '"  + self.beginDate + "' AND TIME_STAMP < '"+ self.endDate +"' AND SPEED_VG >= '"+ self.speedCheck +"' AND DRAFT_FORE > '"+ self.draftForeCheck +"' AND DRAFT_AFT > '"+ self.draftAftCheck +"' AND ABS_WIND_SPEED < '"+ self.windSpeedCheck +"' AND HTSGW < '"+ self.waveHeightCheck +"' AND WATER_DEPTH > '"+ self.waterdepthCheck +"' ORDER BY TIME_STAMP"

        _data = pd.read_sql(stmt,conn)
        #row의 데이터 결측이 있을 시 해당 row 삭제
        # _data = df.dropna(axis=0)
        _data['SPEED_CURRENT'] = _data['SPEED_VG'] + _data['CURRENT_VEL_TAIL_TO_HEADING_NOWCAST']

        if  meanTime > 0 :
            _data = _data.resample(rule=str(meanTime)+'min', on='TIME_STAMP').mean()
            # _data = _data.dropna(axis=0)

        if isShuffle == True:
            result = _data.sample(n=_data.shape[0],random_state=0)
        else:
            result = _data.head(_data.shape[0])

        if isPD == True:
            result = result.loc[:]

        if isPD == False:
            result = (result.loc[:])
            result = result.values

        return result

    def querySpeed(self, tableName = 'min', isShuffle = False, isPD = False, meanTime = 0):
        """pandas 데이터 형태로 데이터 요청
        Parameters
        ----------
        tableName : string, default = "min"
            10초 데이터 or 10분 데이터를 요청할 것인지 선택
        isShuffle : boolean, default = "False"
            데이터를 무작위로 섞는 여부. True - 데이터를 섞음, False - 데이터를 섞지 않고 시간 순으로 정렬.
        isPD : boolean, default = "False"
            데이터 리턴은 PANDAS 형태로 가공할 것인지 여부. True - List 형태로 리턴, False - Pandas DataFrame 형태로 리턴.
        meanTime : int, default = 0
            데이터를 분단위로 normalizing 함. 예) meanTime = 10 - 10분 블록으로 평균을 냄.
        Returns
        -------
        result : DataFrame(Pandas) or array
            요청한 선박, 날짜에 해당하는 데이터.
        """
        conn = pymssql.connect(server='218.39.195.13:21000', user='sa', password='@120bal@', database='SHIP_DB_MARS')
    
        features = "[TIME_STAMP], [SPEED_VG], [SPEED_LW], [CURRENT_VEL_TAIL_TO_HEADING_NOWCAST], [DRAFT_FORE], [DRAFT_AFT], [SHAFT_REV],[BHP_BY_FOC], [SST]"
        
        if (tableName == 'min'):
            tableName = "SAILING_DATA_10MIN"
        else:
            tableName = "SAILING_DATA"

        stmt = "SELECT" + features + "FROM [SHIP_DB_MARS].[dbo].[" + tableName + "] WHERE CALLSIGN ='"+self.callSign+"' AND TIME_STAMP > '"  + self.beginDate + "' AND TIME_STAMP <  '"+ self.endDate +"' AND AT_SEA = 1 AND IS_GOOD_DATA_FOR_ANALYSIS = 1 ORDER BY TIME_STAMP"
        df = pd.read_sql(stmt,conn)
        #row의 데이터 결측이 있을 시 해당 row 삭제
        _data = df.dropna(axis=0)
        _data['SPEED_CURRENT'] = _data['SPEED_VG'] + _data['CURRENT_VEL_TAIL_TO_HEADING_NOWCAST']

        if  meanTime > 0 :
            _data = _data.resample(rule=str(meanTime)+'min', on='TIME_STAMP').mean()
            _data = _data.dropna(axis=0)

        if isShuffle == True:
            result = _data.sample(n=_data.shape[0],random_state=0)
        else:
            result = _data.head(_data.shape[0])

        if isPD == True:
            pd.set_option('display.float_format', '{:.3f}'.format)
            result = result.loc[:, ['TIME_STAMP','SPEED_VG', 'SPEED_LW', 'CURRENT_STW']]
        if isPD == False:
            #pandad datetime을 numpy로 변환
            result.index = result.index.astype(str)
            result = result.reset_index().values
        return result

    def QueryShipParticualr(self):
        conn = pymssql.connect(server='218.39.195.13:21000', user='sa', password='@120bal@', database='SHIP_DB_MARS')
        stmt = "SELECT * FROM [SHIP_DB_MARS].[dbo].[SHIP_PARTICULAR_DETAIL] WHERE CALLSIGN ='"+self.callSign+"'"
        df = pd.read_sql(stmt,conn)
        return df
# dbCon = sqlcon('3ewb4','2017-01-01','2017-02-01')
# shipData = dbCon.querySpeed(isShuffle=False, isPD=True, meanTime = 0)
