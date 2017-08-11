Figure 12:
> setwd("~/Documents")
> read.table('Length.txt')
> read.table('Length.txt',header=TRUE) -> X
> plot(X[,2],X[,3])
> plot(X[,3],X[,2],xlab='GeneLength', ylab='NO.of_variants')
> pos_vector <- rep(3, length(X[,1]))
> pos_vector[X[,1] %in% c('HMCN1', 'BEST1','MAP2K3','ZMAT5')] <- 4
> text(X[,3],X[,2], labels=X[,1], cex=0.7, pos=pos_vector)

Figure 13:
> setwd("~/Documents")
> read.csv('score.txt')
> read.csv('score.txt',header=TRUE) -> X
> plot(X[,3],X[,2],xlab='All_variants', ylab='NO.of_variants')
> pos_vector <- rep(3, length(X[,1]))
> pos_vector[X[,1] %in% c('ZMAT5','TTC3','PRIM2','KCNJ12','MAP2K3')] <- 4
> text(X[,3],X[,2], labels=X[,1], cex=0.7, pos=pos_vector)

Figure 14:
> setwd("~/Documents")
> read.table('canonical_genes.txt',) -> X
> plot(X[,2],X[,3],xlab='All_variants', ylab='NO.C_variants')
> pos_vector <- rep(3, length(X[,1]))
> pos_vector[X[,1] %in% c()] <- 4
> text(X[,3],X[,2], labels=X[,1], cex=0.7, pos=pos_vector)
> plot(X[,2],X[,3],xlab='All_variants', ylab='NO.C_variants')
