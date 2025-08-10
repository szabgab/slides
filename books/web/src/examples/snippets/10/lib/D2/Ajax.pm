post '/api/v2/item' => sub {
        my $text = param('text') // '';
        $text =~ s/^\s+|\s+$//g;
        if ($text eq '') {
            return to_json { error => 'No text provided' };
        }
     
        my $items = _mongodb('items');
        $items->insert({
            text => $text,
            date => DateTime::Tiny->now,
        });
        return to_json { ok => 1, text => $text };
};
