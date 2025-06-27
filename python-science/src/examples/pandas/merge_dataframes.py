import pandas as pd
import numpy as np

# s = pd.Series([1,3,5,np.nan,6,8])
# dates = pd.date_range('20130101', periods=6)
# x = pd.date_range('20130101', periods=6, freq='3D')
# df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
# df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
# df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABC'))
# df2 = pd.DataFrame({ 'A' : 1.,
#                      'B' : pd.Timestamp('20130102'),
#                      'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
#                      'D' : np.array([3] * 4,dtype='int32'),
#                      'E' : pd.Categorical(["test","train","test","train"]),
#                      'F' : 'foo' })
a = pd.DataFrame({ 'A' : ['Joe', 'Jane', 'Foo', 'Bar'], 'B' : [1, 23, 12, 5] })
b = pd.DataFrame({ 'A' : ['Joe', 'Jane', 'Foo', 'Bar'], 'B' : [7, 10, 27, 1 ] })
#c = pd.DataFrame({ 'A' : ['Jane', 'Joe', 'Foo', 'Bar'], 'B' : [10, 7, 27, 1 ] })
c = b.sort_values(by = 'A')
print(a)
print(b)
print(c)
print('---')
#print(a+b)
x = pd.merge(a, b, on='A')
z = pd.DataFrame({ 'A' : x.A, 'B' : x.B_x + x.B_y })
print(z)



#sa = a.sort_values(by = 'A')
#sc = c.sort_values(by = 'A')
print('-----')
#print(sa)
#print(sc)
y = pd.merge(a, c, on='A')
#print(x)
q = pd.DataFrame({ 'A' : y.A, 'B' : y.B_x + y.B_y })
print(z)
