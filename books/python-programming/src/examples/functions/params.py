def sendmail(From, To, Subject, Content):
    print('From:', From)
    print('To:', To)
    print('Subject:', Subject)
    print('')
    print(Content)

sendmail('gabor@szabgab.com',
    'szabgab@gmail.com',
    'self message',
    'Has some content too')
