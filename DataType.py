0x03 Data Types

Types
Text Type	str
Numeric Types	int, float, complex
Sequence Types	list, tuple, range
Mapping Type	dict
Set Types	set, frozenset
Boolean Type	bool
Binary Types	bytes, bytearray, memoryview
Reference from W3School



Text Type
Example 1 (str)
x = "Logix Owl"

print(x)
print(type(x))
Output:
Logix Owl
<class 'str'>
Note type() can show the type of any objects


Numeric Types
Example 2 (int)
x = 100

print(x)
print(type(x))
Output:
100
<class 'int'>
Example 3 (float)
x = 99.9

print(x)
print(type(x))
Output:
99.9
<class 'float'>
Example 4 (complex)
x = 2+3j

print(x)
print(type(x))
Output:
(2+3j)
<class 'complex'>

Sequence Types
Example 5 (list)
x = [ "red" , "green" , "blue" ]

print(x)
print(type(x))
Output:
['red', 'green', 'blue']
<class 'list'>
Example 6 (tuple)
x = ( "red" , "green" , "blue" )

print(x)
print(type(x))
Output:
('red', 'green', 'blue')
<class 'tuple'>
Example 7 (range)
x = range(6)

print(x)
print(type(x))
Output:
range(0, 6)
<class 'range'>

Mapping Type
Example 8 (dict)
x = { "name" : "Logix Owl" , "age" : 24 }

print(x)
print(type(x))
Output:
{'name': 'Logix Owl', 'age': 24}
<class 'dict'>

Set Types
Example 9 (set)
x = { "red" , "green" , "blue" }

print(x)
print(type(x))
Output:
{'blue', 'red', 'green'}
<class 'set'>
Example 10 (frozenset)
x = frozenset({ "red" , "green" , "blue" })

print(x)
print(type(x))
Output:
frozenset({'blue', 'red', 'green'})
<class 'frozenset'>

Boolean Type
Example 11 (bool)
x = True

print(x)
print(type(x))
Output:
True
<class 'bool'>

Binary Types
Example 12 (bytes)
x = b"Logix Owl"

print(x)
print(type(x))
Output:
b'Logix Owl'
<class 'bytes'>
Example 13 (bytearray)
x = bytearray(6)

print(x)
print(type(x))
Output:
bytearray(b'\x00\x00\x00\x00\x00\x00')
<class 'bytearray'>
Example 14 (memoryview)
x = memoryview(bytes(6))

print(x)
print(type(x))
Output:
<memory at 0x7fc301562580>
<class 'memoryview'>

Next (Strings)