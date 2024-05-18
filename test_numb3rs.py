from numb3rs import validate


def test_valid_ipv4():
    assert validate('192.168.0.1') == True
    assert validate('255.255.255.255') == True
    assert validate('0.0.0.0') == True


def test_invalid_ipv4():
    assert validate('275.3.6.28') == False
    assert validate('192.168.1') == False
    assert validate('256.255.255.255') == False
    assert validate('192.168.0.256') == False
    assert validate('192.168.0.-1') == False
    assert validate('192.168.0.1.1') == False
    assert validate('abc.def.ghi.jkl') == False
    assert validate('192.168.0.01') == False  # Leading zeros are not allowed
