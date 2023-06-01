from functions import hello_who, sallary

def test_hello_who_max():
    assert hello_who('Max') == 'Hello, Max!'

def test_hello_who_other():
    assert hello_who('Leo') == 'Hello, Leo!'
    assert hello_who('Kate') == 'Hello, Kate!'

def test_sallary():
    assert sallary(42, 200) == 16800
    assert sallary(2, 100) == 400