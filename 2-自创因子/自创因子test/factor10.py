def run_formula(dv, param=None):
    defult_param = {'t1': 10,'t2':5,'t3':0}
    if not param:
        param = defult_param

    t1 = param['t1']
    t2 = param['t2']
    t3 = param['t3']
    return_create = dv.add_formula('return_create', 'close/Delay(close,%s)'% (t1), is_quarterly=False, add_data=True)


    factor10 = dv.add_formula('factor10', '-Ts_Sum(Max(return_create,%s),%s)*VOL5'% (t3,t2), is_quarterly=False, add_data=True)

    return factor10


