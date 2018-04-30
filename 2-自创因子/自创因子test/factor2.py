


def run_formula(dv):
    factor2 = dv.add_formula('factor2',
                             "-VOL240-5*VOL5",
                             is_quarterly=False, add_data=True)

    return  factor2