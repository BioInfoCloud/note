文章：[https://mp.weixin.qq.com/s/OL6HU2RigA4CDZqD0YgUEw](https://mp.weixin.qq.com/s/OL6HU2RigA4CDZqD0YgUEw)

```R

data(diabetes, package = "mclust")
diabetesTib <- as.data.frame(diabetes)
summary(diabetesTib)
head(diabetesTib)

#scale. = TRUE表示分析前对数据进行归一化；
com1 <- prcomp(diabetesTib[,2:4], center = TRUE,scale. = TRUE)
#提取PC score；
df1<-com1$x
#将iris数据集的第5列数据合并进来；
df1 <- data.frame(df1,diabetesTib$class)
head(df1)

#提取主成分的方差贡献率，生成坐标轴标题；
summ<-summary(com1)
xlab<-paste0("PC1(",round(summ$importance[2,1]*100,2),"%)")
ylab<-paste0("PC2(",round(summ$importance[2,2]*100,2),"%)")
#计算质心，也就是“中心点”，centroid (average) position for each group；
centroid <- aggregate(df1[,1:3],by=list(diabetesTib$class), FUN = mean)
centroid
#合并两个数据框；
data <- merge(df1, centroid,
                by.x = "diabetesTib.class",
                by.y ="Group.1",
                all.x = T,
                suffixes = c("",".centroid"),)
head(data)


```

```r



#载入ggplot2;
library(ggplot2)
#使用ggplot2绘制散点图；
ggplot(data = data, aes(x = PC1, y = PC2))+
  labs(x = xlab, y = ylab)+
  geom_hline(yintercept = 0,lty="dashed",colour="grey60",size=0.4)+
  geom_vline(xintercept = 0,lty="dashed",colour="grey60",size=0.4)+
  stat_ellipse(aes(fill=diabetesTib.class),
               type = "norm", geom ="polygon",
               alpha=0.0,color=NA,show.legend = F)+
  #绘制射向“质心”发散的短线（spider segments）；
  geom_segment(aes(xend= PC1.centroid, yend= PC2.centroid, 
                   colour = diabetesTib.class),
               alpha=0.6,size = 0.5,show.legend = FALSE)+
  #
  geom_point(aes(fill = diabetesTib.class),
             colour="white",shape = 21, size = 2,
             show.legend = T) +
  ##添加质心标签
  geom_label(data = centroid, aes(label = Group.1, fill = Group.1),
             size = 4,hjust=0.5, color="white",show.legend = FALSE)+
  theme_bw()+
  theme(axis.ticks=element_line(colour="gray50"),
        axis.text= element_text(colour="black", size=12),
        axis.title = element_text(colour="black", size=12),
        axis.title.x = element_text(hjust = 0.5,vjust = 0.8),
        axis.title.y = element_text(hjust = 0.5,vjust = 0.2),
        panel.grid = element_blank(),
        plot.title = element_text(hjust=0.5, size=15))
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202212212213259.png)

```R
ggplot(data = data, aes(x = PC1, y = PC2))+
  labs(x = xlab, y = ylab)+
  geom_hline(yintercept = 0,lty="dashed",colour="grey60",size=0.4)+
  geom_vline(xintercept = 0,lty="dashed",colour="grey60",size=0.4)+
  stat_ellipse(aes(fill=diabetesTib.class),
               type = "norm", geom ="polygon",
               alpha=0.0,color=NA,show.legend = F)+
  #绘制射向“质心”发散的短线（spider segments）；
  geom_segment(aes(xend= PC1.centroid, yend= PC2.centroid, 
                   colour = diabetesTib.class),
               alpha=0.6,size = 0.5,show.legend = FALSE)+
  #
  geom_point(aes(fill = diabetesTib.class),
             colour="white",shape = 21, size = 2,
             show.legend = T)+
  #
  scale_fill_manual(values = c("#98d98e","#4d5aaf","#80aba9"),name="Group")+
  scale_colour_manual(values = c("#98d98e","#4d5aaf","#80aba9"),guide=F)+
  #绘制射向“质心”发散的曲线（spider segments）；
  #angle参数的范围为[0,180],数值接近0，弯曲处偏向起点；接近180，弯曲处偏向终点；
  #curvature调整曲率；
  geom_curve(aes(xend= PC1.centroid, yend= PC2.centroid, 
                 colour = diabetesTib.class),
             angle=150,curvature = -0.5,show.legend = FALSE)+
  geom_point(aes(fill = diabetesTib.class),
              colour="white",shape = 21, size = 2.5,
              show.legend = FALSE)+
  ##添加质心标签
  geom_label(data = centroid, aes(label = Group.1, fill = Group.1),
              size = 4,hjust=0.5, color="white",show.legend = FALSE)+
  theme_bw()+
  theme(axis.ticks=element_line(colour="gray50"),
        axis.text= element_text(colour="black", size=12),
        axis.title = element_text(colour="black", size=12),
        axis.title.x = element_text(hjust = 0.5,vjust = 0.8),
        axis.title.y = element_text(hjust = 0.5,vjust = 0.2),
        panel.grid = element_blank(),
        plot.title = element_text(hjust=0.5, size=15))
```



![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202212212214383.png)