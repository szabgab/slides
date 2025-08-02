import locale

print(locale.getlocale(locale.LC_CTYPE))
locale.setlocale(locale.LC_CTYPE, 'en_US.UTF-8')
print(locale.getlocale(locale.LC_CTYPE))
locale.setlocale(locale.LC_CTYPE, 'en_IL.UTF-8')
print(locale.getlocale(locale.LC_CTYPE))

##locale.setlocale(locale.LC_CTYPE, 'ZH.UTF-8')
#print(locale.getlocale(locale.LC_CTYPE))

