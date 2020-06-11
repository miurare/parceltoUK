def convertUnits(df):
    def convertUnit(x):
        if x == 'g':
            return 1
        elif x == 'kg':
            return 1000
    
    _tmp = df['重量'].str.extract('(?P<Number>\d*.?\d)(?P<Unit>[a-z]*)(?P<Upto>[ぁ-ん]*)')
    df['重量'] = _tmp.Number.apply(float) * _tmp.Unit.apply(convertUnit)
    
    return df
