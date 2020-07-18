def sendmail(From, To, Subject, Content):
    print('From:', From)
    print('To:', To)
    print('Subject:', Subject)
    print('')
    print(Content)

sendmail(
    'gabor@szabgab.com',
    Subject = 'self message',
    Content = 'Has some content too',
    To = 'szabgab@gmail.com',
)
