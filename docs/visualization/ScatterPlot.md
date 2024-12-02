原文：[https://mp.weixin.qq.com/s/jvkvL8rii1Lz-5VO9B74tQ](https://mp.weixin.qq.com/s/jvkvL8rii1Lz-5VO9B74tQ)

## 1.普通散点图

```R
library(ggplot2)
data(diabetes, package = "mclust")
ggplot(data = diabetes, aes(x = glucose, y = insulin)) + #数据映射
    geom_point(alpha = 0.8,shape = 19,size=3,color="#DC143C") +#散点图，alpha就是点的透明度
    # theme_bw() +#设定主题
    labs(title = "This is a title")+
    theme(axis.title=element_text(size=15,face="plain",color="black"),
          axis.text = element_text(size=12,face="plain",color="black"),
          legend.position =  "none",
          panel.background = element_rect(fill = "transparent",colour = "black"),
          plot.background = element_blank(),
          plot.title = element_text(size=15, lineheight=.8,hjust=0.5, face="plain"),
          legend.margin = margin(t = 0, r = 0, b = 0, l = 0, unit = "pt"))
```

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/markdown/20241202093639.png)

## 2.添加拟合曲线的散点图

```R
# 添加拟合曲线
ggplot(data = diabetes, aes(x = glucose, y = insulin)) + #数据映射
  geom_point(alpha = 0.8,shape = 19,size=3,color="#DC143C") +#散点图，alpha就是点的透明度
  # theme_bw() +#设定主题
  labs(title = "This is a title")+
  geom_smooth(method = lm, aes(colour = "lm"), linewidth = 1.2,se = T)+
  scale_color_manual(values = c("#808080")) + #手动调颜色c("#DC143C","#00008B", "#808080")
  theme(axis.title=element_text(size=15,face="plain",color="black"),
        axis.text = element_text(size=12,face="plain",color="black"),
        legend.position =  "none",
        panel.background = element_rect(fill = "transparent",colour = "black"),
        plot.background = element_blank(),
        plot.title = element_text(size=15, lineheight=.8,hjust=0.5, face="plain"),
        legend.margin = margin(t = 0, r = 0, b = 0, l = 0, unit = "pt"))
```

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/markdown/20241202090849.png)

```R
R = cor(diabetes$glucose,diabetes$insulin)
p.value = cor.test(diabetes$glucose,diabetes$insulin) # <0.01
lable = paste0("R = ",round(R,2),"\np.value < 0.01")
ggplot(data = diabetes, aes(x = glucose, y = insulin)) + #数据映射
  geom_point(alpha = 0.8,shape = 19,size=3,color="#DC143C") +#散点图，alpha就是点的透明度
  # theme_bw() +#设定主题
  labs(title = "This is a title")+
  geom_smooth(method = lm, aes(colour = "lm"), linewidth = 1.2,se = T)+
  scale_color_manual(values = c("#808080")) + #手动调颜色c("#DC143C","#00008B", "#808080")
  theme(axis.title=element_text(size=15,face="plain",color="black"),
        axis.text = element_text(size=12,face="plain",color="black"),
        legend.position =  "none",
        panel.background = element_rect(fill = "transparent",colour = "black"),
        plot.background = element_blank(),
        plot.title = element_text(size=15, lineheight=.8,hjust=0.5, face="plain"),
        legend.margin = margin(t = 0, r = 0, b = 0, l = 0, unit = "pt"))+ 
  annotate('text', x= 250,y= 200,label = lable ,size = 4)

```

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/markdown/20241202184008.png)

## 3.带分组标签的散点图

```R
# 分组散点图
ggplot(data = diabetes, aes(x = glucose, y = sspg, fill = class,shape = class)) + #数据映射
  geom_point(shape= 21,size=3,
             colour="black",
             stroke=0.25)+
  scale_fill_manual(values=c("#36BED9","#FF0000","#FBAD01"))+
  # theme_bw() +#设定主题
  labs(title = "This is a title",
       fill = "Legend Title")+
  theme(axis.title=element_text(size=15,face="plain",color="black"),
        axis.text = element_text(size=12,face="plain",color="black"),
        panel.background = element_rect(fill = "transparent",colour = "black"),
        plot.background = element_blank(),
        plot.title = element_text(size=15, lineheight=.8,hjust=0.5, face="plain"),
        legend.margin = margin(t = 0, r = 0, b = 0, l = 0, unit = "pt"))
```

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/markdown/20241202091003.png)

## 4.火山图

数据样式：

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/markdown/20241202200932.png)

```R
load("DESeq2-filtered-pcDEG.Rdata") # pcDEG
library(ggrepel) # install.packages("ggrepel")
ggplot(data = pcDEG, aes(x = logFC, y = -log10(FDR), colour = direction)) + #数据映射
  geom_point(alpha = 1,size=2) +#散点图，alpha就是点的透明度
  scale_color_manual(values = c("#DC143C","#00008B", "#808080")) + #手动调颜色
  theme_bw() +#设定主题
  geom_text_repel(label = pcDEG$lab,#lab列对应的点的显示文本
                  size = 4,
                  segment.color = "black", #连接线的颜色，就是名字和点之间的线
                  show.legend = FALSE) +
  theme(axis.title=element_text(size=15,face="plain",color="black"),
        axis.text = element_text(size=12,face="plain",color="black"),
        legend.title = element_blank(),
        legend.background = element_blank(),
        panel.background = element_rect(fill = "transparent",colour = "black"),
        plot.background = element_blank(),
        plot.title = element_text(size=15, lineheight=.8,hjust=0.5, face="plain"),
        legend.margin = margin(t = 0, r = 0, b = 0, l = 0, unit = "pt"))+
  labs(title = "Tumor vs. Normal")+ #""
  ylab(expression(-log[10]("FDR"))) +#expression的作用就是让log10的10下标
  xlab(expression(log[2]("Fold Change"))) +
  geom_vline(xintercept = c(-2, 2), #加垂直线，在-2和+2之间划线
             lty = 2,
             col = "black",
             lwd = 0.3) +
  geom_hline(yintercept = -log10(0.05),
             lty = 2,
             col = "black",
             lwd = 0.3)
```

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/markdown/20241202091555.png)

## 5.烟花状散点图

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
ggplot(data = data, aes(x = PC1, y = PC2))+
  labs(x = xlab, y = ylab)+
  geom_hline(yintercept = 0,lty="dashed",colour="grey60",linewidth=0.4)+
  geom_vline(xintercept = 0,lty="dashed",colour="grey60",linewidth=0.4)+
  stat_ellipse(aes(fill=diabetesTib.class),type = "norm", 
               geom ="polygon",alpha=0.0,color=NA,show.legend = F)+
  #绘制射向“质心”发散的短线（spider segments）；
  geom_segment(aes(xend= PC1.centroid, yend= PC2.centroid, colour = diabetesTib.class),
               alpha=0.6,size = 0.5,show.legend = FALSE)+
  geom_point(aes(fill = diabetesTib.class),colour="white",shape = 21, 
             size = 2,show.legend = T)+
  scale_fill_manual(values = c("#98d98e","#4d5aaf","#80aba9"),name="Group")+
  scale_colour_manual(values = c("#98d98e","#4d5aaf","#80aba9"),guide=F)+
  #绘制射向“质心”发散的曲线（spider segments）；
  #angle参数的范围为[0,180],数值接近0，弯曲处偏向起点；接近180，弯曲处偏向终点；
  #curvature调整曲率；
  geom_curve(aes(xend= PC1.centroid, yend= PC2.centroid, colour = diabetesTib.class),
             angle=150,curvature = -0.5,show.legend = FALSE)+
  geom_point(aes(fill = diabetesTib.class),colour="white",shape = 21, 
             size = 2.5,show.legend = FALSE)+
  geom_label(data = centroid, aes(label = Group.1, fill = Group.1),   ##添加质心标签
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

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/markdown/20241202091848.png)

```R
ggplot(data = data, aes(x = PC1, y = PC2))+
  labs(x = xlab, y = ylab)+
  geom_hline(yintercept = 0,lty="dashed",colour="grey60",linewidth=0.4)+
  geom_vline(xintercept = 0,lty="dashed",colour="grey60",linewidth=0.4)+
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
  scale_fill_manual(values = c("#f8d98e","#ad5aaf","#80aba9"),name="Group")+
  scale_colour_manual(values = c("#f8d98e","#ad5aaf","#80aba9"),guide=F)+
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

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/markdown/20241202092227.png)

## 6.配对样本散点图连线图

```R
library(ggplot2)
set.seed(123)# 设置随机种子以便结果可重复
# 生成模拟数据
paried.data <- data.frame(
  exp = c(rnorm(n_samples, mean = 8, sd = 1),rnorm(n_samples, mean = 13, sd = 1.2)),  # 正常组织数据
  Type = rep(c("Normal", "Tumor"), each = 10),
  Sample = rep(paste0("Sample",1:10),2)
)
dat1_paried <- reshape2::dcast(paried.data, Type~Sample) #为了防止配对样本信息错乱，构造配对样本的数据集
# 配对 t 检验，双侧检验
p.value <- t.test(paried.data$exp[paried.data$Type == "Normal"], 
                  paried.data$exp[paried.data$Type == "Tumor"], 
                  paired = TRUE, alternative = 'two.sided', conf.level = 0.95)
pv <- p.value[["p.value"]]
stasig <- ifelse(pv >= 0.001, paste0('p value = ', round(pv, 3)), "p value < 0.01")

# 绘图
ggplot(paried.data, aes(x = Type, y = exp,colour = Type)) +
  geom_point(size = 3) +  #绘制散点表示单个样本的基因表达信息
  geom_line(aes(group = Sample), color = 'black', lwd = 0.05) +  
  scale_colour_manual(values = c('#FE7280', '#AC88FF')) + 
  theme_classic()+ 
  labs(y= paste0("The expression of ***\nlog2(TPM + 1)"),title= "title")+
  theme(panel.background=element_rect(fill="white",colour="black",size=0.25),
        plot.title = element_text(hjust = 0.5),
        axis.line=element_line(colour="black",size=0.25),
        axis.title.x = element_blank(),
        axis.text.x = element_text(face = "plain",colour = "black"),
        axis.text = element_text(size=12,face="plain",color="black"),
        legend.position="none"
  )+ annotate('text', x= 2,y= 5,label = stasig ,size = 4)
```

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/markdown/20241202175946.png)

参考：[https://mp.weixin.qq.com/s/OL6HU2RigA4CDZqD0YgUEw](https://mp.weixin.qq.com/s/OL6HU2RigA4CDZqD0YgUEw)