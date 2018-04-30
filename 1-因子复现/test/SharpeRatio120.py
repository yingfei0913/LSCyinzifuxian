def run_formula(dv, param=None):
    defult_param = {'t1': 1, 't2': 120}
    if not param:
        param = defult_param

    t1 = param['t1']
    t2 = param['t2']


    SharpeRatio120 = dv.add_formula('SharpeRatio120',
                                    "(Ts_Mean(close/Delay(close,%s)-1,%s)-0.03)/StdDev((close/Delay(close,%s)-1),%s)" % (t1, t2, t1, t2)
                                    , is_quarterly=False, add_data=True)
    return SharpeRatio120




