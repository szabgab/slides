$mock->add(get => sub {
    die 'Something went wrong'; 
});
is_deeply $w->count_strings('Beyonce', 'Miley Cyrus'), 
    {
        Beyonce => 0,
        'Miley Cyrus' => 0,
    };
