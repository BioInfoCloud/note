# 逻辑回归（Logistic Regression）

以泰坦尼克号乘客数据为例，完整走一遍逻辑回归的流程：数据清洗 → 探索性可视化 → 建模 → 缺失值处理 → 交叉验证 → 优势比解释 → 预测新数据。

本例基于 R 的 [`mlr`](https://mlr.mlr-org.com/) 包。原始脚本：[LOGISTIC_REGRESSION.R](./LOGISTIC_REGRESSION.R)

## 1. 加载包

```r
library(mlr)
library(tidyverse)
```

## 2. 读入数据

```r
install.packages("titanic")

data(titanic_train, package = "titanic")

titanicTib <- as_tibble(titanic_train)

titanicTib
```

## 3. 数据清洗

把 `Survived`、`Sex`、`Pclass` 转成因子，并由 `SibSp`（兄弟姐妹/配偶数）+ `Parch`（父母/子女数）构造家庭规模 `FamSize`。

```r
fctrs <- c("Survived", "Sex", "Pclass")

titanicClean <- titanicTib %>%
  mutate_at(.vars = fctrs, .funs = factor) %>%
  mutate(FamSize = SibSp + Parch) %>%
  select(Survived, Pclass, Sex, Age, Fare, FamSize)

titanicClean
```

## 4. 探索性可视化

连续变量看分布（小提琴图 + 分位数），分类变量看生存率的构成（堆叠比例条形图）。

```r
titanicUntidy <- gather(titanicClean, key = "Variable", value = "Value",
                        -Survived)
titanicUntidy

titanicUntidy %>%
  filter(Variable != "Pclass" & Variable != "Sex") %>%
  ggplot(aes(Survived, as.numeric(Value))) +
  facet_wrap(~ Variable, scales = "free_y") +
  geom_violin(draw_quantiles = c(0.25, 0.5, 0.75)) +
  theme_bw()

titanicUntidy %>%
  filter(Variable == "Pclass" | Variable == "Sex") %>%
  ggplot(aes(Value, fill = Survived)) +
  facet_wrap(~ Variable, scales = "free_x") +
  geom_bar(position = "fill") +
  theme_bw()
```

## 5. 建任务、选学习器并训练

```r
titanicTask <- makeClassifTask(data = titanicClean, target = "Survived")

logReg <- makeLearner("classif.logreg", predict.type = "prob")

logRegModel <- train(logReg, titanicTask)
```

## 6. 处理缺失值

`Age` 有缺失，`mlr` 的 `impute()` 可以直接用均值填补。先看填补前后的缺失个数：

```r
imp <- impute(titanicClean, cols = list(Age = imputeMean()))

sum(is.na(titanicClean$Age))
sum(is.na(imp$data$Age))
```

用填补后的数据重建任务并重新训练：

```r
titanicTask <- makeClassifTask(data = imp$data, target = "Survived")

logRegModel <- train(logReg, titanicTask)
```

更省事的做法是把填补步骤包进学习器，形成「学习器 + 预处理」的 wrapper，后续交叉验证里会自动对每一折做同样的填补，避免信息泄漏：

```r
logRegWrapper <- makeImputeWrapper("classif.logreg",
                                   cols = list(Age = imputeMean()))
logRegWrapper
```

## 7. 交叉验证

用重复 10 折（重复 50 次）的分层交叉验证评估模型，指标取准确率、假正率和假负率。

```r
kFold <- makeResampleDesc(method = "RepCV", folds = 10, reps = 50,
                          stratify = TRUE)

logRegwithImpute <- resample(logRegWrapper, titanicTask, resampling = kFold,
                             measures = list(acc, fpr, fnr))
logRegwithImpute
```

## 8. 解释系数：优势比（Odds Ratio）

对系数取指数即得优势比，同时给出置信区间：

```r
logRegModelData <- getLearnerModel(logRegModel)

coef(logRegModelData)

exp(cbind(Odds_Ratio = coef(logRegModelData), confint(logRegModelData)))
```

## 9. 用模型预测新数据

```r
data(titanic_test, package = "titanic")

titanicNew <- as_tibble(titanic_test)

titanicNewClean <- titanicNew %>%
  mutate_at(.vars = c("Sex", "Pclass"), .funs = factor) %>%
  mutate(FamSize = SibSp + Parch) %>%
  select(Pclass, Sex, Age, Fare, FamSize)

predict(logRegModel, newdata = titanicNewClean)
```

## 10. 课后练习

**（1）** 在小提琴图基础上叠加散点，直接看原始观测点：

```r
titanicUntidy %>%
  filter(Variable != "Pclass" & Variable != "Sex") %>%
  ggplot(aes(Survived, as.numeric(Value))) +
  facet_wrap(~ Variable, scales = "free_y") +
  geom_violin(draw_quantiles = c(0.25, 0.5, 0.75)) +
  geom_point(alpha = 0.05, size = 3) +
  theme_bw()
```

**（2）** 对比 `dodge` 与 `stack` 两种条形图排布：

```r
titanicUntidy %>%
  filter(Variable == "Pclass" | Variable == "Sex") %>%
  ggplot(aes(Value, fill = Survived)) +
  facet_wrap(~ Variable, scales = "free_x") +
  geom_bar(position = "dodge") +
  theme_bw()

titanicUntidy %>%
  filter(Variable == "Pclass" | Variable == "Sex") %>%
  ggplot(aes(Value, fill = Survived)) +
  facet_wrap(~ Variable, scales = "free_x") +
  geom_bar(position = "stack") +
  theme_bw()
```

**（3）** 去掉 `Fare` 再评估，看模型表现掉多少：

```r
titanicNoFare <- select(titanicClean, -Fare)
titanicNoFareTask <- makeClassifTask(data = titanicNoFare,
                                     target = "Survived")
logRegNoFare <- resample(logRegWrapper, titanicNoFareTask,
                         resampling = kFold,
                         measures = list(acc, fpr, fnr))
logRegNoFare
```

**（4）** 从姓名里抽出称谓（Mr / Dr / Master / Miss / Mrs / Rev，其余归为 Other），它往往比年龄更能反映社会地位：

```r
surnames <- map_chr(str_split(titanicTib$Name, "\\."), 1)

salutations <- map_chr(str_split(surnames, ", "), 2)

salutations[!(salutations %in% c("Mr", "Dr", "Master",
                                 "Miss", "Mrs", "Rev"))] <- "Other"
```

**（5）** 把称谓作为新特征加进模型，重新交叉验证：

```r
fctrsInclSals <- c("Survived", "Sex", "Pclass", "Salutation")

titanicWithSals <- titanicTib %>%
  mutate(FamSize = SibSp + Parch, Salutation = salutations) %>%
  mutate_at(.vars = fctrsInclSals, .funs = factor) %>%
  select(Survived, Pclass, Sex, Age, Fare, FamSize, Salutation)

titanicWithSalsTask <- makeClassifTask(data = titanicWithSals,
                                       target = "Survived")

logRegWrapper <- makeImputeWrapper("classif.logreg",
                                   cols = list(Age = imputeMean()))

kFold <- makeResampleDesc(method = "RepCV", folds = 10, reps = 50,
                          stratify = TRUE)

logRegWithSals <- resample(logRegWrapper, titanicWithSalsTask,
                           resampling = kFold,
                           measures = list(acc, fpr, fnr))
logRegWithSals
```
