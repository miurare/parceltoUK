def convertUnits(df):
    def convertUnit(x):
        if x == 'g':
            return 1
        elif x == 'kg':
            return 1000
    
    _tmp = df['重量'].str.extract('(?P<Number>[0-9]*[.,]?[0-9]*)(?P<Unit>[a-z]*)(?P<Upto>[ぁ-ん]*)')
    df['重量'] = _tmp.Number.str.replace(',','').apply(float) * _tmp.Unit.apply(convertUnitg)
    _tmp = df['料金'].str.extract('(?P<Number>[0-9]*\,?[0-9]*)')
    df['料金'] = _tmp.Number.str.replace(',','').apply(int)
    
    return df
