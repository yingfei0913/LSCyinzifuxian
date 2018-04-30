def run_formula(dv, param=None):
    defult_param = {'t1': 120}
    if not param:
        param = defult_param

    t1 = param['t1']

    factor7 = dv.add_formula('factor7', '-(close_adj/Ts_Sum(close_adj,%s)*120-1)*100'% (t1),
                              is_quarterly=False, add_data=True)
    return factor7



