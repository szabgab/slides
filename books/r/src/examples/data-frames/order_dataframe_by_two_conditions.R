df = data.frame(A=c(2, 1, 1, 3), B=c(2, 4, 3, 1))
df
df[order(df$A),]
df[order(df$B),]
df[order(df$A, df$B),]

