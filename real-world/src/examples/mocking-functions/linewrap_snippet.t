$mock->add(get => sub {
    return 'Beyonce Miley Cyrus Miley
Cyrus';
});
is_deeply $w->count_strings('Beyonce', 'Miley Cyrus'), 
    {
        Beyonce => 1,
        'Miley Cyrus' => 2,
    };
