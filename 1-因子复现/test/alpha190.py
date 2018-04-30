def run_formula(dv, param=None):
    defult_param = {'t1': 1,'t2':19,'t3':20}
    if not param:
        param = defult_param

    t1 = param['t1']
    t2 = param['t2']
    t3 = param['t3']

    a = dv.add_formula('a',
                       'close/Delay(close,%s)-1'% (t1),
                       is_quarterly=False, add_data=True)
    b = dv.add_formula('b',
                       '(close/Delay(close,%s))^(1/20)-1'% (t2),
                       is_quarterly=False, add_data=True)

    alpha190 = dv.add_formula('alpha190',
                              'Log((Ts_Sum(If(a>b,1,0),%s)-1)*Ts_Sum(If(a<b,(a-b)^2,0),%s)/(Ts_Sum(If(a<b,1,0),%s))*Ts_Sum(If(a>b,(a-b)^2,0),%s))'% (t3, t3, t3,t3),
                              is_quarterly=False, add_data=True)
    return alpha190

