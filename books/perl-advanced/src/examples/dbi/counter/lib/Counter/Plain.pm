package Counter::Plain;
use strict;
use warnings;
use 5.010;

my $filename = "counter.txt";

sub create {
    die "File '$filename' already exists\n" if -e $filename;
    open my $fh, '>', $filename or die;
    close $fh or die;
}

sub start {
    my ($name) = @_;
    my $data = _read_file();

    die "Name '$name' already exists\n" if exists $data->{$name};
    $data->{$name} = 0;
    say $data->{$name};

    _save_file($data);
}

sub count {
    my ($name) = @_;
    my $data = _read_file();

    die "Name '$name' does not exist\n" if not exists $data->{$name};
    $data->{$name}++;
    say $data->{$name};

    _save_file($data);
}

sub _read_file {
    open my $fh, '<', $filename or die;
    my %data;
    while (my $line = <$fh>) {
        chomp $line;
        my ($name, $value) = split /:/, $line;
        $data{$name} = $value;
    }
    close $fh;
    return \%data;
}

sub _save_file {
    my ($data) = @_;
    open my $fh, '>', $filename or die;
    foreach my $name (sort keys %$data) {
        print $fh "$name:$data->{$name}\n";
    }
    close $fh;
}

sub delete {
    die "File '$filename' did not exists\n" if not -e $filename;
    unlink $filename or die;
}


1;
