

def run_formula(dv):
    factor3 = dv.add_formula('factor3',
               "-TOBT*BullPower",
               is_quarterly = False, add_data = True)
    return  factor3
