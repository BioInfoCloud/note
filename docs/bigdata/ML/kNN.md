## 1.什么是kNN算法？

KNN是英文k-nearest neighbor的缩写。是一个基本的分类和回归的算法，它是属于**监督学习**中分类方法的一种。事实上，kNN可以说是最简单的机器学习算法。尽管kNN很简单，但它可以提供令人惊讶的良好分类性能，并且其简单性使其易于解释。

我们可以用两个阶段来描述 kNN 算法（和其他机器学习算法）：

- **训练阶段**
- **预测阶段**

kNN 算法的训练阶段仅包括存储数据。

在预测阶段，kNN 算法计算每个新的、未标记的事例与所有标记事例之间的*距离*。当我说“距离”时，我指的是它们在攻击性和体长变量方面的接近程度，而不是你在树林里发现它们有多远！这个距离度量通常被称为*欧几里得*距离，在二维甚至三维中很容易在你的脑海中可视化为图上两点之间的直线距离。这是在数据中存在的维度中计算的。



## 2.R语言实现

### 2.1 包的安装

```R
# INSTALLING AND LOADING PACKAGES ----
install.packages("mlr", dependencies = TRUE) # could take several minutes
# only needed once on any R installation
library(mlr)
library(tidyverse)
```

### 2.2 案例数据

医院从糖尿病患者那里收集几个月的诊断数据，并记录他们是否被诊断为健康、化学糖尿病或显性糖尿病。这里使用 kNN 算法来训练一个模型，该模型可以预测新患者将属于哪些类别，以便改进诊断。这是一个三类分类问题。

现在，让我们加载一些内置到 mclust 包中的数据，将其转换为 tibble，并对其进行一些探索:

```R
# LOADING DIABETES DATA ----
data(diabetes, package = "mclust")
diabetesTib <- as_tibble(diabetes)
summary(diabetesTib)
diabetesTib
```

```R
MedBioInfoCloud: summary(diabetesTib)
      class       glucose       insulin            sspg      
 Chemical:36   Min.   : 70   Min.   :  45.0   Min.   : 10.0  
 Normal  :76   1st Qu.: 90   1st Qu.: 352.0   1st Qu.:118.0  
 Overt   :33   Median : 97   Median : 403.0   Median :156.0  
               Mean   :122   Mean   : 540.8   Mean   :186.1  
               3rd Qu.:112   3rd Qu.: 558.0   3rd Qu.:221.0  
               Max.   :353   Max.   :1568.0   Max.   :748.0  
MedBioInfoCloud: 
MedBioInfoCloud: diabetesTib
# A tibble: 145 x 4
   class  glucose insulin  sspg
   <fct>    <dbl>   <dbl> <dbl>
 1 Normal      80     356   124
 2 Normal      97     289   117
 3 Normal     105     319   143
 4 Normal      90     356   199
 5 Normal      90     323   240
 6 Normal      86     381   157
 7 Normal     100     350   221
 8 Normal      85     301   186
 9 Normal      97     379   142
10 Normal      97     296   131
# ... with 135 more rows
# i Use `print(n = ...)` to see more rows
MedBioInfoCloud: 
```

该数据集包含 145 个案例和 4 个变量。其中76例为正常，36例为化学糖尿病，33例为显性糖尿病。其他三个变量是葡萄糖耐量试验后血糖和胰岛素水平的连续测量和稳态血糖水平。

简单探索变量之间的关系

```R
# PLOT THE RELATIONSHIPS IN THE DATA ----
p1 <- ggplot(diabetesTib, aes(glucose, insulin, col = class)) + 
  geom_point()  +
  theme_bw()

p2 <- ggplot(diabetesTib, aes(sspg, insulin, col = class)) + 
  geom_point() +
  theme_bw()

p3 <- ggplot(diabetesTib, aes(sspg, glucose, col = class)) + 
  geom_point() +
  theme_bw()
library(Rmisc)
multiplot(p1,p2,p3, cols = 3)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202211261555828.png)

我们将从构建 kNN 模型的简单、朴素的方式开始。

### 2.3 构建模型

我们试图解决的问题是将新患者分为三类之一，现在我们需要训练 kNN 算法来构建一个可以解决这个问题的模型。mlr 包构建机器学习模型有三个主要阶段：

- **定义任务：**该任务由数据以及我们想要用它做什么组成。在这种情况下，数据是，我们希望使用变量作为目标变量对数据进行分类。diabetesTibclass
- **定义学习器：**学习器只是我们计划使用的算法的名称，以及算法接受的任何其他参数。
- **训练模型：**这个阶段听起来像：您将任务传递给学习者，学习者生成一个可用于进行未来预测的模型。

<img src="https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202211261604073.png" style="zoom:200%;" />

#### （1）定义任务

可以通过`makeClassifTask()`函数定义分类任务来构建分类模型。

```R
makeClassifTask(
  id = deparse(substitute(data)),
  data,
  target,
  weights = NULL,
  blocking = NULL,
  coordinates = NULL,
  positive = NA_character_,
  fixup.data = "warn",
  check.data = TRUE
)
```

- id:默认值是传递给data的R变量的名称。

- data:包含特征和目标变量的data.frame

- target:目标变量的名称。对于生存分析，这些是生存时间和事件列的名称，因此其长度为2。对于多标签分类，它包含编码标签是否存在的逻辑列名称，其长度对应于类的数量。

- weights:(numeric)在拟合过程中使用的可选非负大小写权重向量。无法为cost-sensitive learning设置。默认值为NULL，这意味着没有（等于）权重。

- blocking:(factor)与观测次数长度相同的可选因子。具有相同blocking水平的观测结果“属于同一个”。具体来说，在重新采样迭代期间，它们要么全部放入训练集，要么放入测试集。默认值为NULL，表示没有blocking。

- coordinates:(data.frame)空间数据集的坐标，将用于空间交叉验证重采样设置中数据的空间分区。坐标必须是数值。提供的data.fram需要具有与data相同的行数，并且至少包含两个维度。

- 
  positive:二进制分类的阳性类(否则忽略并设置为NA)。Default是目标属性的第一个因子级别。

- 
  fixup.data:是否应该进行一些基本的数据清理？目前，这意味着删除列的空因子级别。可能的选择是：“no”=不做。“warn”=做但要警告。“quiet”=做但保持沉默。默认值为“warn”。

- check.data:逻辑值，是否应该在任务创建时首先检查数据的完整性?你应该有很好的理由关闭它(一个可能是速度)。默认为TRUE。

```R
# DEFINING THE DIABETES TASK ----
diabetesTask <- makeClassifTask(data = diabetesTib, target = "class")

diabetesTask
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202211261625540.png)

#### （2）定义学习器

**就是告诉mlr使用哪种算法？？**

<img src="https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202211261630895.png" style="zoom:150%;" />

我们使用的算法类别：

- "classif."用于分类
- "regr."用于回归
- "cluster."用于聚类
- "surv."以及预测生存和多标签分类

下面使用`makeLearner()`函数来定义学习器。`makeLearner()`第一个参数是用于训练模型的算法。`par.vals`参数代表参数值，它允许我们指定我们希望算法使用的 k 最近邻的数量。现在，我们只将其设置为 2，后面会讨论如何选择k：

```R
# DEFINING THE KNN LEARNER ----
knn <- makeLearner("classif.knn", par.vals = list("k" = 2))
```

mlr包有大量的机器学习算法，可以将这些算法提供给`makeLearner()`函数。

```R
# LISTING ALL OF MLR'S LEARNERS ----
listLearners()$class
```

```R
  [1] "classif.ada"                    "classif.adaboostm1"            
  [3] "classif.bartMachine"            "classif.binomial"              
  [5] "classif.boosting"               "classif.bst"                   
  [7] "classif.C50"                    "classif.cforest"               
  [9] "classif.clusterSVM"             "classif.ctree"                 
 [11] "classif.cvglmnet"               "classif.dbnDNN"                
 [13] "classif.dcSVM"                  "classif.earth"                 
 [15] "classif.evtree"                 "classif.fdausc.glm"            
 [17] "classif.fdausc.kernel"          "classif.fdausc.knn"            
 [19] "classif.fdausc.np"              "classif.FDboost"               
 [21] "classif.featureless"            "classif.fgam"                  
 [23] "classif.fnn"                    "classif.gamboost"              
 [25] "classif.gaterSVM"               "classif.gausspr"               
 [27] "classif.gbm"                    "classif.glmboost"              
 [29] "classif.glmnet"                 "classif.h2o.deeplearning"      
 [31] "classif.h2o.gbm"                "classif.h2o.glm"               
 [33] "classif.h2o.randomForest"       "classif.IBk"                   
 [35] "classif.J48"                    "classif.JRip"                  
 [37] "classif.kknn"                   "classif.knn"                   
 [39] "classif.ksvm"                   "classif.lda"                   
 [41] "classif.LiblineaRL1L2SVC"       "classif.LiblineaRL1LogReg"     
 [43] "classif.LiblineaRL2L1SVC"       "classif.LiblineaRL2LogReg"     
 [45] "classif.LiblineaRL2SVC"         "classif.LiblineaRMultiClassSVC"
 [47] "classif.logreg"                 "classif.lssvm"                 
 [49] "classif.lvq1"                   "classif.mda"                   
 [51] "classif.mlp"                    "classif.multinom"              
 [53] "classif.naiveBayes"             "classif.neuralnet"             
 [55] "classif.nnet"                   "classif.nnTrain"               
 [57] "classif.OneR"                   "classif.pamr"                  
 [59] "classif.PART"                   "classif.penalized"             
 [61] "classif.plr"                    "classif.plsdaCaret"            
 [63] "classif.probit"                 "classif.qda"                   
 [65] "classif.randomForest"           "classif.ranger"                
 [67] "classif.rda"                    "classif.rFerns"                
 [69] "classif.rotationForest"         "classif.rpart"                 
 [71] "classif.RRF"                    "classif.saeDNN"                
 [73] "classif.sda"                    "classif.sparseLDA"             
 [75] "classif.svm"                    "classif.xgboost"               
 [77] "cluster.cmeans"                 "cluster.Cobweb"                
 [79] "cluster.dbscan"                 "cluster.EM"                    
 [81] "cluster.FarthestFirst"          "cluster.kkmeans"               
 [83] "cluster.kmeans"                 "cluster.MiniBatchKmeans"       
 [85] "cluster.SimpleKMeans"           "cluster.XMeans"                
 [87] "multilabel.cforest"             "multilabel.rFerns"             
 [89] "regr.bartMachine"               "regr.bcart"                    
 [91] "regr.bgp"                       "regr.bgpllm"                   
 [93] "regr.blm"                       "regr.brnn"                     
 [95] "regr.bst"                       "regr.btgp"                     
 [97] "regr.btgpllm"                   "regr.btlm"                     
 [99] "regr.cforest"                   "regr.crs"                      
[101] "regr.ctree"                     "regr.cubist"                   
[103] "regr.cvglmnet"                  "regr.earth"                    
[105] "regr.evtree"                    "regr.FDboost"                  
[107] "regr.featureless"               "regr.fgam"                     
[109] "regr.fnn"                       "regr.frbs"                     
[111] "regr.gamboost"                  "regr.gausspr"                  
[113] "regr.gbm"                       "regr.glm"                      
[115] "regr.glmboost"                  "regr.glmnet"                   
[117] "regr.GPfit"                     "regr.h2o.deeplearning"         
[119] "regr.h2o.gbm"                   "regr.h2o.glm"                  
[121] "regr.h2o.randomForest"          "regr.IBk"                      
[123] "regr.kknn"                      "regr.km"                       
[125] "regr.ksvm"                      "regr.laGP"                     
[127] "regr.LiblineaRL2L1SVR"          "regr.LiblineaRL2L2SVR"         
[129] "regr.lm"                        "regr.mars"                     
[131] "regr.mob"                       "regr.nnet"                     
[133] "regr.pcr"                       "regr.penalized"                
[135] "regr.plsr"                      "regr.randomForest"             
[137] "regr.ranger"                    "regr.rpart"                    
[139] "regr.RRF"                       "regr.rsm"                      
[141] "regr.rvm"                       "regr.svm"                      
[143] "regr.xgboost"                   "surv.cforest"                  
[145] "surv.coxph"                     "surv.cvglmnet"                 
[147] "surv.gamboost"                  "surv.gbm"                      
[149] "surv.glmboost"                  "surv.glmnet"                   
[151] "surv.ranger"                    "surv.rpart"  
```

可以按功能列出：

```R
# or list them by function:
listLearners("classif")$class
listLearners("regr")$class
listLearners("cluster")$class
```

#### （3）训练模型

训练模型所需的组件是我们之前定义的学习器和任务。定义任务和学习器并将它们组合以训练模型的整个过程：

<img src="https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202211271539707.png" style="zoom:150%;" />

这是通过`train()`函数实现的，该函数将学习器作为第一个参数，将任务作为其第二个参数。

```R
# DEFINE MODEL ----
knnModel <- train(knn, diabetesTask)
```

建好的模型后，所以让数据传递给模型，并观察如何执行。`predict()`函数的作用是获取未标记的数据，并将其传递到模型中以获取预测的类。`predict()`函数第一个参数是模型，想要传递给模型的数据可作为newdata参数给出。

```R
# TESTING PERFORMANCE ON TRAINING DATA (VERY BAD PRACTICE) ----
knnPred <- predict(knnModel, newdata = diabetesTib)
```

我们可以将这些预测作为`performance()`函数的第一个参数传递。此函数将模型预测的类与 true 类进行比较，并返回预测值和 true 值相互匹配程度的性能指标。

<img src="https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202211271550805.png" style="zoom:150%;" />

我们通过将它们作为列表提供给参数来指定我们希望函数返回的性能指标。我要求的两个度量是平均误分类误差（MMCE）和或准确率（acc）。MMCE表示模型错分样本的比例。准确性与MMCE相反，acc表示模型正确分类样本的比例。两者的总和为 1.00。

```R
performance(knnPred, measures = list(mmce, acc))
```

```R
MedBioInfoCloud: performance(knnPred, measures = list(mmce, acc))
      mmce        acc 
0.06206897 0.93793103 
```

我们的模型正确分类了 93.8% 的案例！这是否意味着它将在未来患者中表现出良好的预测？事实是我们不知道。通过要求模型对你最初用于训练它的数据进行预测来评估模型性能，这几乎不会告诉你模型在对完全看不见的数据进行预测时将如何执行。因此，切勿以这种方式评估模型性能。在我们讨论原因之前，我想介绍一个重要的概念，称为偏差-方差权衡。

#### （4）偏差-方差权衡

欠拟合和过拟合是模型构建中误差的两个重要来源。在欠拟合中，我们包含的预测因子太少或模型太简单，无法充分描述数据中的关系/模式。结果是一个据说有*偏差*的模型：一个在我们用来训练它的数据和新数据上表现不佳的模型。

过度拟合与欠拟合相反，它描述了我们包含太多预测因子或太复杂的模型的情况，这样我们不仅要对数据中的关系/模式进行建模，还要对*噪声*进行建模。数据集中的噪声是与我们测量的变量没有系统相关性的变化，而是由于变量测量的固有变异性和/或误差造成的。噪声模式非常特定于单个数据集，因此如果我们开始对噪声进行建模，我们的模型可能会在我们训练它的数据上表现非常好，但对于未来的数据集给出的结果却有很大差异。

泛化误差是模型做出的错误预测的比例，是过度拟合和欠拟合的结果。与过度拟合（模型过于复杂）相关的误差是方差。与欠拟合（模型太简单）相关的误差是偏差。与过度拟合（模型过于复杂）相关的误差是方差。最佳模型可以平衡这种权衡。欠拟合和过度拟合都会引入误差并降低模型的泛化性：模型泛化到未来看不见的数据的能力。它们也是相互对立的：介于欠拟合和有偏差的模型和过度拟合和有方差的模型之间，是平衡偏差-方差权衡的最佳模型。

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202211271610770.png)

两类分类问题的欠拟合、最优拟合和过拟合示例。虚线表示决策边界。

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202211271611740.png)

#### （5）交叉验证

我们使用一部分数据来训练模型：这部分称为训练集。我们使用算法在训练期间从未看到的其余部分来测试模型：这部分是测试集。然后，我们评估模型在测试集上的预测与其真实值的接近程度。衡量训练好的模型在测试集上的表现如何有助于我们确定我们的模型在看不见的数据上是否表现良好，或者我们是否需要进一步改进它。

此过程称为交叉验证 （CV），它是任何监督式机器学习管道中极其重要的方法。一旦我们交叉验证了我们的模型并对其性能感到满意，我们就使用我们拥有的所有数据（包括测试集中的数据）来训练最终模型（因为通常，我们训练模型的数据越多，它的偏差就越小）。

有三种常见的交叉验证方法：

- 留出法交叉验证
- K -折法交叉验证
- 留一法交叉验证

##### 留出法交叉验证

数据随机分为训练集和测试集。训练集用于训练模型，然后用于对测试集进行预测。预测与测试集真实值的相似性用于评估模型性能。

在 MLR 中使用任何交叉验证的第一步是进行重采样描述，这只是一组关于如何将数据拆分为测试和训练集的说明。`makeResampleDesc()`函数的第一个参数是我们将要使用的交叉验证方法。在本例中，留出法（Holdout）交叉验证 ，我们需要告诉函数中有多少比例的数据将用作训练集，因此我们将其提供给`split`参数。另外，还有一个额外的可选参数`stratify = TRUE`。它要求函数确保在将数据拆分为训练集和测试集时，它会尝试保持每组每类患者的比例。

```R
# PERFORMING HOLD-OUT CROSS-VALIDATION ----
holdout <- makeResampleDesc(method = "Holdout", split = 2/3, 
                            stratify = TRUE)
```

定义好如何交叉验证我们的学习器之后，我们可以使用`resample()`函数进行交叉验证了。`resample()`函数提供了创建学习器和任务以及刚才定义的重采样方法。

```R
holdoutCV <- resample(learner = knn, task = diabetesTask, 
                      resampling = holdout,
                      measures = list(mmce, acc))
```

resample()函数在运行时输出性能度量，这些度量可以通过从resampling对象中提取$aggr组建得到。

```R
MedBioInfoCloud: holdoutCV$aggr
mmce.test.mean  acc.test.mean 
    0.06122449     0.93877551
```

为了更好地了解哪些组被正确分类，哪些被错误分类，我们可以构建一个混淆矩阵。*混淆矩阵*只是测试集中每个事例的真实和预测类的表格表示。使用 mlr包种的`calculateConfusionMatrix()`函数计算混淆矩阵。第一个参数是 holdoutCV对象的pred组件，它包含测试集的真实类和预测类。可选参数relative要求函数显示每个类在真实和预测类标签中的比例。

```R
calculateConfusionMatrix(holdoutCV$pred, relative = TRUE)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202211271644035.png)

绝对混淆矩阵更容易解释。行显示真实的类标签，列显示预测的标签。这些数字表示真实类和预测类的每种组合中的样本数。例如，在这个矩阵中，10名患者被正确归类为化学糖尿病，但一名患者被错误地归类为健康，一名患者被错误地归类为显性糖尿病。正确分类的患者位于矩阵的对角线上（其中真实类==预测类）。

##### K -折法交叉验证

在K -折法交叉验证中，我们将数据随机拆分为大约相等大小的子集。然后，我们将其中一个子集保留为测试集，并使用剩余的数据作为训练集（留出法交叉验证一样）。我们通过模型通过测试集，并记录相关的性能指标。在此过程中，数据中的每个样本仅在测试集中出现一次。

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202211271659982.png)

这种方法通常会对模型性能进行更准确的估计，因为每个事例在测试集中出现一次，并且我们正在对多次运行的估计值求平均值。但是我们可以通过使用重复的 k-fold 交叉验证 来稍微改善这一点，在上一个过程之后，我们将数据打乱并再次执行。

例如，对于 k 折法，通常选择的*k*值是 10。同样，这取决于数据的大小等，但对于许多数据集来说，这是一个合理的值。这意味着我们将数据分成 10 个大小几乎相等的块并执行交叉验证。如果我们重复此过程 5 次，那么我们有 10 倍的交叉验证重复 5 次（这与 50 倍的 交叉验证不同），模型性能的估计将是 50 次不同运行的平均值。

因此，如果有计算资源，通常最好使用重复的K -折法交叉验证而不是普通的K -折法交叉验证。

我们执行 K -折法交叉验 的方式与留出法相同。这一次，函数将使用重复的K -折法交叉验证来进行重采样描述，并告诉它我们要将数据拆分为多少个子集。默认k为 10，这通常是一个不错的选择，但我想向您展示如何显式控制拆分。接下来，使用函数参数reps参数重复进行50次的10-折交叉验证。这将提供了 500 次试验来平均性能度量！同样，这里要求在子集中对类别进行分层采样。

```R
# PERFORMING REPEATED K-FOLD CROSS-VALIDATION ----
kFold <- makeResampleDesc(method = "RepCV", folds = 10, reps = 50, 
                          stratify = TRUE)

kFoldCV <- resample(learner = knn, task = diabetesTask, 
                    resampling = kFold, measures = list(mmce, acc))
```

提取平均性能度量：

```R
MedBioInfoCloud: kFoldCV$aggr
mmce.test.mean  acc.test.mean 
     0.1045667      0.8954333 
```

