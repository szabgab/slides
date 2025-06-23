fname = ['Graham',          'Eric',            'Terry',
         'Terry',           'John',            'Michael']
lname = ['Chapman',         'Idle',            'Gilliam',
         'Jones',           'Cleese',          'Palin']
born  = ['8 January 1941',  '29 March 1943',   '22 November 1940',
         '1 February 1942', '27 October 1939', '5 May 1943']

for f_name, l_name, b_date in zip(fname, lname, born):
    print(f"{f_name:7} {l_name:7} was born {b_date}")
