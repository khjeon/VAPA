import sys
import os
sys.path.append(os.path.join(sys.path[0],'data_process'))
sys.path.append(os.path.join(sys.path[0],'data_analysis'))
sys.path.append(os.path.join(sys.path[0],'helper'))
import datain as di
import dataout as do

datain = di.Init('3FFB8','2017-02-20','2017-10-22','7','8.676','10.392','6.7','1','300','B')
shipDatas = datain.queryAll(isShuffle=False, isPD=True, meanTime = 0)
shipParticular = datain.QueryShipParticualr()
print(shipParticular)

print(shipParticular['loa'])
# dataout = do.Init(shipDatas)
# dataout.to_print(['SPEED_VG'])
# dataout.to_csv(['SPEED_VG'])