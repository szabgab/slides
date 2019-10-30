def sendmail(From, To, Subject, Content):
    print('From:', From)
    print('To:', To)
    print('Subject:', Subject)
    print('')
    print(Content)

sendmail(
    Subject = 'self message',
    Content = 'Has some content too',
    To = 'szabgab@gmail.com',
    'gabor@szabgab.com',
)
