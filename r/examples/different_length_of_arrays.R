# R starts to reuse the shorter vector if one of the vactors is longer than the other
# gives a warning
# TODO: can we stop running at such warnings?

a = c(TRUE, TRUE, FALSE)
b = c(TRUE, FALSE, TRUE, FALSE)

a & b
a | b
! a

x = c(1, 2, 3)
y = c(10, 20)
x+y

# options(warn=2)  # turn warnings into errors
# options(warn=0)  # ???? turn warnings back to warnings