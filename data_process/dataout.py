import pandas as pd
from pandas import DataFrame

class Init():
    """선박운항데이터 프로세싱 초기화.
    Parameters
    ----------
    shipDatas : DataFrame
        프로세싱하고자 하는 선박 운항데이터
    """
    def __init__(self, shipDatas):
        self.shipDatas = shipDatas

    def to_csv(self, fileds = [],  path = './sample.csv'):
        """데이터를 csv로 export
        Parameters
        ----------
        fileds : array, default = 모든 필드
            출력하고자 하는 필드명, 입력하지 않으면 모든 필드가 출력됨.
        path : string, default = './sample.csv'
            출력 경로 및 파일이름.
        """
        if (len(fileds) == 0):
            self.shipDatas.to_csv(path)
        else:
            csvDatas = self.shipDatas.loc[:, fileds]
            csvDatas.to_csv(path)

    def to_print(self, fileds = [], sep = ','):
        """데이터를 print로 출력
        Parameters
        ----------
        fileds : array, default = 모든 필드
            출력하고자 하는 필드명, 입력하지 않으면 모든 필드가 출력됨.
            각 필드 데이터를 순차적으로 출력함. 
        sep : string, default = ','
            각 필드별 데이터 구분자
        """
        if (len(fileds) != 0):
            outDatas = self.shipDatas.loc[:, fileds]
        else:
            outDatas = self.shipDatas
        for column in outDatas:
            for item in outDatas[column]:
                print(item)
            
            print(sep)

        
