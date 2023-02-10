filename = "sample.txt"
print(filename)

fh <- file(filename, "w")
cat("TITLE line", "First row", "", "Third row", sep = "\n", file = fh)
cat("One more line\n", file = fh)
close(fh)
