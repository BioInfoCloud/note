
# gsl：https://sourceforge.net/projects/gnu-scientific-library-windows/
Sys.setenv(GSL_LIBS = '"D:/Program Files/R/scripts/gsl-2.2.1_mingw-6.2.0"')

if(!require(devtools)){ install.packages("devtools")}
if("RcppML" %in% rownames(installed.packages())){remove.packages("RcppML")}
devtools::install_github("zdebruine/RcppML",force = TRUE)
devtools::install_github("gambalab/gficf")

library(gficf)
require(ggplot2)