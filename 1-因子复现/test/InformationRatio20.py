import numpy as np
import pandas as pd
import warnings
from jaqs_fxdayu.data import RemoteDataService


from jaqs_fxdayu.data.dataservice import LocalDataService
dataview_folder = r'../data'
ds = LocalDataService(fp=dataview_folder)
start = 20130101
end = 20180101

def run_formula(dv, param=None):
    defult_param = {'t1': 1, 't2': 20}
    if not param:
        param = defult_param

    t1 = param['t1']
    t2 = param['t2']
    hs300 = ds.index_daily(['000300.SH'], start, end, 'trade_date,close')
    hs300 = pd.Series(list(hs300[0]['close']), index=hs300[0]['trade_date'], name='hs300')
    hs300_1 = dv.get_ts('close') + np.nan
    for i in range(hs300_1.shape[0]):
        hs300_1.iloc[:, i] = hs300
    dv.append_df(hs300_1, 'hs300')

    InformationRatio20 = dv.add_formula('InformationRatio20',
                                        "Ts_Mean((close/Delay(close,%s)-hs300/Delay(hs300,%s)),%s)/(StdDev(close/Delay(close,%s)-hs300/Delay(hs300,%s),%s))^0.5"% (t1, t1, t2, t1, t1, t2)
                                        , is_quarterly=False, add_data=True)
    return InformationRatio20



