sub = "cat"
txt = "The black cat climbed the green tree"

if sub in txt:
    loc = txt.index(sub)
    print(sub + " is at " + str(loc))

sub = "dog"
if sub in txt:
    loc = txt.index(sub)
    print(sub + " is at " + str(loc))
    
# cat is at 10
