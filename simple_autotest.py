from functions import hello_who, sallary

assert hello_who('Max') == 'Hello, Max!', 'text 1'
assert hello_who('Kate') == 'Hello, Kate!', 'text 1'

assert sallary(42, 200) == 16800, sallary(42, 200)
assert sallary(1, 300) == 600, 'text 2'