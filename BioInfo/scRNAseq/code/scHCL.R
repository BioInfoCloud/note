# https://github.com/ggjlab/scHCL

# 一种工具根据单细胞数字表达定义人类细胞类型
#This require devtools  
install.packages('devtools')
library(devtools)
# scHCL requires ggplot2/reshape2/plotly/shiny/shinythemes/shiny
install_github("ggjlab/scHCL")

library(scHCL)

data(hcl_lung)
dim(hcl_lung)

hcl_result <- scHCL(scdata = hcl_lung, numbers_plot = 3)
scHCL_vis(hcl_result)



