Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 8*60+15
495
>>> 7*60+12
432
>>> 432*3
1296
>>> 1296+495+495
2286
>>> 2286/60
38.1
>>> print('6:52+38.1')
6:52+38.1
>>> print('7:30:6')
7:30:6
>>> start=6*3600+52*60
>>> easy=8*60+15
>>> tempo=7*60+12
>>> time_spend=2*easy+3*tempo
>>> print(time_spend//3600,':',time_spend%3600//60,':',time_spend%60)
0 : 38 : 6
>>> result=time_spend+start
>>> print(result//3600,':',result%3600//60,':',result%60)
7 : 30 : 6
>>> 5%2
1
>>> 10%7
3
>>> 10//7
1
>>> 10%5
0
>>> result%3600
1806
>>> result/3600
7.501666666666667
>>> 1806/60
30.1
>>> 1806//60
30
>>> result%60
6
>>> 1806%60
6
>>> 
