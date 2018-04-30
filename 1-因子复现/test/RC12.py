def run_formula(dv, param=None):
    defult_param = {'t1': 12}
    if not param:
        param = defult_param

    t1 = param['t1']
    RC12 = dv.add_formula('RC12_J',
                          "close/Delay(close,%s)"% (t1),
                          is_quarterly=False, add_data=True)
    return RC12


