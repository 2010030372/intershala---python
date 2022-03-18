def bat(i):
    a = i['runs']
    b = i['balls']
    sc = a // 2
    srate = a / b * 100
    if a >= 50:
        sc = sc + 5
    if a >= 100:
        sc = 10 + sc
    if 80 <= srate <= 100:
        sc = 2 + sc
    if srate > 100:
        sc = 4 + sc
    field = i['field'] * 10
    fours = i['4'] * 1
    six = i['6'] * 2
    sc = sc + fours + six + field
    print("{'name': '%s', 'batscore':'%d' } " % (i['name'], sc))
    return sc

def bowl(i):
    sc = i["wkts"] * 10
    ecrate = i['runs']/i['overs']
    if i['wkts'] >= 3:
        sc = sc + 5
    if i['wkts'] >=5:
        sc = sc + 10
    if 3.5 <= ecrate <= 4.5:
        sc = sc + 4
    if 2 <= ecrate <= 3.5:
        sc = sc + 7
    if ecrate<2:
        sc = sc + 10
    field = i['field'] * 10
    sc = sc + field
    print("{'name': '%s', 'bowlscore':'%d' } " % (i['name'], sc))
    return sc




