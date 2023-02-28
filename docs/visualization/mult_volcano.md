## 多组差异表达分析火山图合并绘制

我这里有很多差异分析的结果，获取这些结果的完整路径

```R
degr = dir("output/016_hot_cold_tumor/DEG",
           "DESeq2-filtered.csv$",full.names = T,recursive = T)
degr[1:4]
```

```R
MedBioInfoCloud: degr[1:4]
[1] "output/016_hot_cold_tumor/DEG/TCGA-ACC/DESeq2-filtered.csv" 
[2] "output/016_hot_cold_tumor/DEG/TCGA-BLCA/DESeq2-filtered.csv"
[3] "output/016_hot_cold_tumor/DEG/TCGA-BRCA/DESeq2-filtered.csv"
[4] "output/016_hot_cold_tumor/DEG/TCGA-CESC/DESeq2-filtered.csv"
```

读入其中一个：

```R
data = read.csv(degr[1],header = T,
                check.names = F,row.names = 1)
```

查看一下数据：

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302212219415.png)

我这里的差异分析结果文件很多，我选择4个文件读入并合并。

```R
subdeg = degr[1:4]
alldeg = do.call(rbind,lapply(subdeg, function(x){
  data = read.csv(x,header = T,
                  check.names = F,row.names = 1)
  data = data[data$gene_type == "protein_coding",]
  data = data[!duplicated(data[,"gene_name"]),]
  data$cancer = unlist(strsplit(x,"/"))[4]
  data$cancer = unlist(strsplit(data$cancer,"-"))[2]
  return(data)
}))
```

合并后添加了1列cancer。

处理一下数据，并增加一列cluster

```R
head(alldeg)
alldeg2 = alldeg[alldeg$direction != "Ns",]
alldeg2 = arrange(alldeg2,cancer)
alldeg2$cancer = factor(alldeg2$cancer)
alldeg2$cluster = as.numeric(alldeg2$cancer) - 1
```

```R
MedBioInfoCloud: head(alldeg2)[,(ncol(alldeg2)-3):ncol(alldeg2)]
             FDR direction cancer cluster
27  1.164291e-06        Up    ACC       0
33  1.452798e-09      Down    ACC       0
182 9.039400e-04        Up    ACC       0
430 4.099443e-03      Down    ACC       0
447 4.636853e-11      Down    ACC       0
469 8.875275e-05        Up    ACC       0
```

计算每组差异分析中logFC的最大值和最小值

```
minlogfc = alldeg2 %>% group_by(cancer) %>% dplyr::slice(which.min(logFC))
maxlogfc = alldeg2 %>% group_by(cancer) %>% dplyr::slice(which.max(logFC))
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302212229631.png)

根据分组个数，定义用来绘图的数据。

```
dfbar0 <- data.frame(x=c(0:3),
                    y= maxlogfc$logFC )
dfbar1<- data.frame(x=c(0:3),
                    y=minlogfc$logFC)

dfcol<- data.frame(x=c(0:3),
                   y=0,
                   label= unique(alldeg2$cancer))
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302212231426.png)

绘制背景图：

```R
p <- ggplot()+
  geom_col(data = dfbar0,
           mapping = aes(x = x,y = y),
           fill = "#dcdcdc",alpha = 0.6)+
  geom_col(data = dfbar1,
           mapping = aes(x = x,y = y),
           fill = "#dcdcdc",alpha = 0.6) 
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302212235793.png)

添加散点图：

```R
p1 = p +   geom_jitter(data = alldeg2,
                       aes(x = cluster, y = logFC, color = direction),
                       size = 0.85,
                       width =0.4)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302212236703.png)

修改点的颜色：

```R
p2 = p1+ scale_color_manual(name=NULL,
                           values = c("blue","red"))
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302212238622.png)

添加注释框：

```R
p3 = p2 + geom_tile(data = dfcol,
                    aes(x=x,y=y),
                    height=2,
                    color = "black",
                    fill = mycol,
                    alpha = 0.6,
                    show.legend = F)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302212240021.png)

添加文本和坐标标题：

```R
p4 = p3 + 
  labs(x="Cancer",y="log2FC") + #添加坐标标题
  ##给注释框添加文本
  geom_text(data=dfcol,
            aes(x=x,y=y,label=label),
            size =6,
            color ="black")
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302212247340.png)

修改主题，需要把横坐标的数值去掉，因为它没有任何意义。

```R
p4 + theme_minimal()+
  theme(
    axis.title = element_text(size = 13,
                              color = "black",
                              face = "bold"),
    axis.line.y = element_line(color = "black",
                               size = 1),
    axis.line.x = element_blank(),
    axis.text.x = element_blank(),
    axis.text.y = element_text(size = 15,face = "bold", colour = "#1A1A1A"),
    panel.grid = element_blank(),
    legend.direction = "vertical",
    legend.text = element_text(size = 15)
  )
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302212246195.png)

完整代码：

```R
ggplot()+
  geom_col(data = dfbar0,
           mapping = aes(x = x,y = y),
           fill = "#dcdcdc",alpha = 0.6)+
  geom_col(data = dfbar1,
           mapping = aes(x = x,y = y),
           fill = "#dcdcdc",alpha = 0.6)+
  geom_jitter(data = alldeg2,
              aes(x = cluster, y = logFC, color = direction),
              size = 1.5,
              width =0.4)+
  scale_color_manual(name=NULL,
                     values = c("blue","red"))+
  geom_tile(data = dfcol,
            aes(x=x,y=y),
            height=2,
            color = "black",
            fill = mycol,
            alpha = 0.6,
            show.legend = F)+
  
  labs(x="Cancer",y="log2FC") + #添加坐标标题
  ##给注释框添加文本
  geom_text(data=dfcol,
            aes(x=x,y=y,label=label),
            size =6,
            color ="black")+
  theme_minimal()+
  theme(
    axis.title = element_text(size = 13,
                              color = "black",
                              face = "bold"),
    axis.line.y = element_line(color = "black",
                               size = 1),
    axis.line.x = element_blank(),
    axis.text.x = element_blank(),
    axis.text.y = element_text(size = 15,face = "bold", colour = "#1A1A1A"),
    panel.grid = element_blank(),
    legend.direction = "vertical",
    legend.text = element_text(size = 15)
  )
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302212252804.png)

统计所有分组差异基因的频率，找出共同基因并标注出来。

```R
gene_stat = as.data.frame(table(alldeg2$gene_name))
gene_stat = arrange(gene_stat,desc(Freq))
head(gene_stat)
```

```R
MedBioInfoCloud: head(gene_stat)
     Var1 Freq
1    AOAH    4
2 ARHGAP9    4
3    C1QA    4
4    C1QB    4
5    C1QC    4
```

总共4个分组的差异分析，频率为4的基因就是共同的差异表达基因。我们选择3个来显示：

```
gs = gene_stat$Var1[gene_stat$Freq ==4][1:3]
gstab = alldeg2[alldeg2$gene_name %in% gs,]
gstab = arrange(gstab,cancer)
```

```R
library(ggrepel)
fig +
  geom_text_repel(
    data=gstab,
    aes(x=cluster,y=logFC,label=gene_name),
    force = 1.2,
    arrow = arrow(length = unit(0.008, "npc"),
                  type = "open", ends = "last")
  )

```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302212305992.png)