a = 1
b = 3
c = 5
x1 = (-b)/(2*a)
x2 = ((b**2-4*a*c)**(1/2))/(2*a)
if b**2-4*a*c > 0 : #実数解の場合
     print('x=',x1,'±',x2)
elif b**2-4*a*c < 0 :#虚数解の場合
      x2 = ((4*a*c-b**2)**(1/2))/(2*a)
      print('x=',x1,'±',x2,'i')
else: #重解の場合
      print('x=',x1)
