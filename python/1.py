Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> min=42
>>> sec=42
>>> res=min*60+sec
>>> res
2562
>>> mile=1.6km
SyntaxError: invalid syntax
>>> km=10
>>> mile=1.6*km
>>> mile
16.0
>>> pace=res/km
>>> pace
256.2
>>> speed=mile/hour
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    speed=mile/hour
NameError: name 'hour' is not defined
>>> hour=res/3600
>>> speed=mile/hour
>>> speed
22.482435597189696
>>> mile=km/1.61
>>> mile
6.211180124223602
>>> speed=mile/hour
>>> speed
8.727653570337614
>>> 
============== RESTART: C:/Users/acer e15/Desktop/python/1.1.py ==============
>>> 
>>> 42
42
>>> timeinsecond
2562
>>> 
============== RESTART: C:/Users/acer e15/Desktop/python/1.1.py ==============
>>> mile
6.211180124223602
>>> 
============== RESTART: C:/Users/acer e15/Desktop/python/1.1.py ==============
>>> pace
412.482
>>> speed
8.727653570337614
>>> 
