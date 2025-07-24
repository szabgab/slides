# Debugging prints

```
# Scalar:
print STDERR "Debug: '$a'\n";


# Array:
print STDERR "Debug: @a\n";

print STDERR "Debug: ", join "|", @a, "\n";


# Hash:
print STDERR "Debug: ", join "|", %h, "\n";

print STDERR "Debug: "; 
foreach (keys %h) { print STDERR "$_=>$h{$_}|";
print STDERR "\n";


print STDERR "Debug: "; 
print STDERR "$_=>$h{$_}|" for keys %h;
print STDERR "\n";
```


