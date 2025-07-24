a = c(0, 0)
b = c(3, 4)
distance=function(a, b) {

  xdiff = abs(a[1]-b[0])
  print(xdiff)
  ydiff = abs(a[1]-b[1])
  print((xdiff**2 + ydiff**2)**0.5)
}
distance(a, b)

