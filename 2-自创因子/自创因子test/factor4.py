def run_formula(dv, param=None):
    defult_param = {'t1': 5,'t2':1}
    if not param:
        param = defult_param

    t1 = param['t1']
    t2 = param['t2']

    EMA = dv.get_ts('close').ewm(span=t1, adjust=False).mean()
    EMA2 = EMA.ewm(span=t1, adjust=False).mean()
    EMA3 = EMA2.ewm(span=t1, adjust=False).mean()

    dv.append_df(EMA3, 'EMA3')
    factor4 = dv.add_formula('factor4', '-EMA3/Delay(EMA3,%s)+1'% (t2), is_quarterly=False, add_data=True)

    return factor4


