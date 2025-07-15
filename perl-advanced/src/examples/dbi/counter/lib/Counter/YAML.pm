package Counter::YAML;
use strict;
use warnings;
use 5.010;

my $filename = "counter.yml";

use YAML qw(DumpFile LoadFile);

sub create {
    die "File '$filename' already exists\n" if -e $filename;
    my %data;
    DumpFile $filename, \%data;
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
    my $data = LoadFile($filename);
    return $data;
}

sub _save_file {
    my ($data) = @_;
    DumpFile $filename, $data;
}

sub delete {
    die "File '$filename' did not exists\n" if not -e $filename;
    unlink $filename or die;
}

1;
