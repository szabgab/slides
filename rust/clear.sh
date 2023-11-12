
# Remove all the target folders with all the dependencies and compiled code
# Last time I ran `du -hs .` before calling clean it reported 22 Gb, after calling clean it reported 11 Mb.
# After running clean and then running check got us to 7Gb

rm -rf examples/*/*/target
