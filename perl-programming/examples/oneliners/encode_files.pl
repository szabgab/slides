use Encode;

foreach $file (@ARGV) {
    copy $file, "$file.bak";
}
while (<>) {
   Encode::from_to($_, 'Windows-1255', 'utf-8');
   print $_;
}
