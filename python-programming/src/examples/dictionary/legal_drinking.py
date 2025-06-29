legal_drinking_age = {
0 : ['Angola', 'Guinea-Bissau', 'Nigeria', 'Togo', 'Western Sahara', 'Haiti', 'Cambodia', 'Macau'],
15 : ['Central African Republic'],
16 : [
'Gambia',
'Morocco',
'Antigua and Barbuda',
'Barbados',
'British Virgin Islands',
'Cuba',
'Dominica',
'Grenada',
'Saint Lucia',
'Saint Vincent and the Grenadines',
'Palestinian Authority',
'Austria',
'Denmark',
'Germany',
'Gibraltar',
'Lichtenstein',
'Luxembourg',
'San Marino',
'Switzerland'
],
17 : ['Malta'],
19 : ['Canada', 'South Korea'],
20 : ['Benin', 'Paraguay', 'Japan', 'Thailand', 'Uzbekistan', 'Iceland', 'Sweden'],
21 : [
'Cameroon',
'Egypt',
'Equatorial Guinea',
'Bahrain', 'Indonesia',
'Kazakhstan',
'Malaysia',
'Mongolia',
'Oman',
'Qatar',
'Sri Lanka',
'Turkmenistan',
'United Arab Emirates',
'American Samoa',
'Northern Mariana Islands',
'Palau',
'Samoa',
'Solomon Islands'
],
25 : ['USA'],
200 : ['Lybia', 'Somalia', 'Sudan', 'Afghanistan', 'Brunei', 'Iran', 'Iraq', 'Kuwait', 'Pakistan', 'Saudi Arabia', 'Yemen'],
}

age = int(input('Please enter your age in number of years: '))
country = input('Please enter the country of your location: ')

for k in legal_drinking_age:
    if country in legal_drinking_age[k]:
        print('The minimum legal drinking age in your location is: {} years'.format(k))
        if age >= k:
            exit('You are allowed to consume alcohol in your location')
        else:
            exit('You are not permitted to consume alcohol currently in your location.')
print('The minimum legal drinking age in your location is: 18 years')
if age >= 18:
    exit('You are allowed to consume alcohol in your location')
else:
    exit('You are not permitted to consume alcohol currently in your location.')
