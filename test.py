from payment import calculate as cal

def test(a,b):
    c = cal(a,b)

    test_c = pow(a,b)

    assert c == test_c


test(10,20)
test(1,15)
test(40,150)
