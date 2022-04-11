def sendmail(From, To, Subject, Content, **header):
    print('From:', From)
    print('To:', To)
    print('Subject:', Subject)
    for field, value in header.items():
        print(f"X-{field}: {value}")
    print('')
    print(Content)

sendmail(
    Subject = 'self message',
    Content = 'Has some content too',
    From = 'gabor@szabgab.com',
    To = 'szabgab@gmail.com',

    mailer = "Python",
    signature = "My sig",
)
