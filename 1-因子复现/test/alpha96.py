def run_formula(dv, param = None):
    defult_param = {'t1':9,'t2':3,'t3':1,}
    if not param:
        param = defult_param

    t1 = param['t1']
    t2 = param['t2']
    t3 = param['t3']

    def SMA(A, n, m):
        # 设置alpha的比例
        alpha = m / n
        # 通过ewm计算递归函数
        return A.ewm(alpha=alpha, adjust=False).mean()

    alpha96 = dv.add_formula('alpha96',
                             "SMA(SMA((close-Ts_Min(low,%s))/(Ts_Max(high,%s)-Ts_Min(low,%s))*100,%s,%s),%s,%s)"%(t1,t1,t1,t2,t3,t2,t3)
                             , is_quarterly=False, add_data=True,
                             register_funcs={"SMA": SMA}
                             )
    return alpha96



