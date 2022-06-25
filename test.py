def hoge():
    with open('old_elem.txt') as f:
        old = f.read()

    with open('test.txt') as t:
        new = t.read()

    if old == new:
        print('同じ')
    else:
        print('違う')

hoge()