


def run_formula(dv):
    DebtEquityRatio = dv.add_formula('DebtEquityRatio',
               "total_liab/tot_shrhldr_eqy_excl_min_int"
               , is_quarterly=False)
    return  DebtEquityRatio


