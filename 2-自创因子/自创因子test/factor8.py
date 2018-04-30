def run_formula(dv, param=None):
    defult_param = {'t1': 10}
    if not param:
        param = defult_param

    t1 = param['t1']
    return_create = dv.add_formula('return_create', 'close/Delay(close,%s)'% (t1), is_quarterly=False, add_data=True)


    factor8 = dv.add_formula('factor8', '-VOL60*(return_create)', is_quarterly=False, add_data=True)

    return factor8


