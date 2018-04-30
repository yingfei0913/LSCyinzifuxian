
def run_formula(dv, param=None):
    defult_param = {'t1': 1}
    if not param:
        param = defult_param

    t1 = param['t1']



    NetAssetGrowRate = dv.add_formula('NetAssetGrowRate_J',
                                      "tot_shrhldr_eqy_excl_min_int/Delay(tot_shrhldr_eqy_excl_min_int,%s)-1"% (t1)
                                      , is_quarterly=False, add_data=True)

    return NetAssetGrowRate

