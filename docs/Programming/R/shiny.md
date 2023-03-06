

## 1.Shiny APP结构


## 2.UI

Shiny 提供的 HTML 输入和输出。这使您能够捕获多种类型的数据并显示多种类型的 R 输出。在这里，我将主要坚持 Shiny 本身内置的输入和输出。 但是，有一个丰富而充满活力的扩展包社区，如[shinyWidgets](https://github.com/dreamRs/shinyWidgets)，[colorpicker](https://github.com/daattali/colourpicker)和[sorttable](https://rstudio.github.io/sortable/)。 您可以在 https://github.com/nanxstats/awesome-shiny-extensions 上找到由 [Nan Xiao](https://nanx.me/) 维护的其他软件包的全面、积极维护的列表。

像往常一样，我们将从加载shiny包开始：

```R
library(shiny)
```

### 2.1 输入

您可以使用sliderInput()、selectInput()、textInput()、numericInput() 等函数将输入控件插入 UI 规范中。 现在，我们将讨论所有输入函数的通用结构，并快速概述 Shiny 中内置的输入。

#### (1)共同结构

所有输入函数都具有相同的第一个参数：. 。 这是用于连接前端和后端的标识符，如果您的 UI 具有带有 ID 的输入，则服务器函数将使用`inputId "name" input$name` 访问它。

inputId有2个约束。

- 它必须是仅包含字母、数字和下划线的简单字符串（不允许使用空格、破折号、句点或其他特殊字符！ 命名它就像在 R 中命名变量一样。
- 它必须是唯一的。 如果它不是唯一的，您将无法在server函数中引用此控件！

大多数输入函数都有第二个参数，称为`label` 。 这用于为控件创建人类可读的标签。 Shiny 没有对此字符串施加任何限制，但您需要仔细考虑它以确保您的应用程序可供人类使用！ 第三个参数通常是 `value`，在可能的情况下，它允许您设置默认值。 其余参数对于控件是唯一的。

创建输入时，我建议按位置提供 `inputId` `label`参数，并按名称提供所有其他参数：

```R
sliderInput("min", "Limit (minimum)", value = 50, min = 0, max = 100)
```

#### (2) 自由文本

使用 textInput() 收集少量文本，使用 passwordInput()3 收集密码，使用 textAreaInput() 收集文本段落。

```R
ui <- fluidPage(
  textInput("name", "What's your name?"),
  passwordInput("password", "What's your password?"),
  textAreaInput("story", "Tell me about yourself", rows = 3)
)
```

#### (3)数值输入

要收集数值，请使用 `numericInput()` 创建一个受约束的文本框或使用 `sliderInput()` 创建一个滑块。 如果您为 `sliderInput()` 的默认值提供一个长度为 2 的数值向量，您将得到一个具有两端的“范围”滑块。

```R
ui <- fluidPage(
  numericInput("num", "Number one", value = 0, min = 0, max = 100),
  sliderInput("num2", "Number two", value = 50, min = 0, max = 100),
  sliderInput("rng", "Range", value = c(10, 20), min = 0, max = 100)
)
```

#### (4)日期

使用 dateInput() 收集一天或使用 dateRangeInput() 收集两天的范围。 这些提供了一个方便的日历选择器，以及 datesdisabled 和 daysofweekdisabled 等附加参数允许您限制有效输入集

```R
ui <- fluidPage(
  dateInput("dob", "When were you born?"),
  dateRangeInput("holiday", "When do you want to go on vacation next?")
)
```

#### (5)选择有限 

有两种不同的方法允许用户从一组预先指定的选项中进行选择：selectInput() 和 radioButtons()。

```R
animals <- c("dog", "cat", "mouse", "bird", "other", "I hate animals")

ui <- fluidPage(
  selectInput("state", "What's your favourite state?", state.name),
  radioButtons("animal", "What's your favourite animal?", animals)
)
```

使用 selectInput() 创建的下拉列表占用相同数量的空间，无论选项的数量如何，使它们更适合较长的选项。您还可以设置 multiple = TRUE 以允许用户选择多个元素。

```R
ui <- fluidPage(
  selectInput(
    "state", "What's your favourite state?", state.name,
    multiple = TRUE
  )
)
```

如果您有一组非常大的可能选项，您可能需要使用“server-side” `selectInput()`，这样完整的一组可能选项就不会嵌入到UI中（这会导致加载速度变慢），而是根据服务器的需要发送。有关此高级主题的详细信息，请访问https://shiny.rstudio.com/articles/selectize.html#server-侧选择。
无法使用单选按钮选择多个值，但有一个概念上类似的替代方法：`checkboxGroupInput()`。

```R
ui <- fluidPage(
  checkboxGroupInput("animal", "What animals do you like?", animals)
)
```

如果您想要单个复选框用于单个是/否问题，请使用 checkboxInput()：

```R
ui <- fluidPage(
  checkboxInput("cleanup", "Clean up?", value = TRUE),
  checkboxInput("shutdown", "Shutdown?")
)
```

#### (6)上传文件

允许用户使用 fileInput() 上传文件：

```R
ui <- fluidPage(
  fileInput("upload", NULL)
)
```

#### (7)Action buttons

让用户使用 actionButton() 或 actionLink() 执行操作：

```R
ui <- fluidPage(
  actionButton("click", "Click me!"),
  actionButton("drink", "Drink me!", icon = icon("cocktail"))
)
#> This Font Awesome icon ('cocktail') does not exist:
#> * if providing a custom `html_dependency` these `name` checks can 
#>   be deactivated with `verify_fa = FALSE`
```

操作链接和按钮最自然地与服务器函数中的 observeEvent() 或 eventReactive() 配对。 您还没有了解这些重要功能，但我们回过头来讨论它们。

您可以使用“btn-primary”、“btn-success”、“btn-info”、“btn-warning”或“btn-danger”之一使用类参数自定义外观。 您还可以使用“btn-lg”、“btn-sm”、“btn-xs”更改大小。 最后，您可以使用“btn-block”使按钮跨越它们嵌入的元素的整个宽度。

```R
ui <- fluidPage(
  fluidRow(
    actionButton("click", "Click me!", class = "btn-danger"),
    actionButton("drink", "Drink me!", class = "btn-lg btn-success")
  ),
  fluidRow(
    actionButton("eat", "Eat me!", class = "btn-block")
  )
)
```

class 参数通过设置底层 HTML 的 class 属性来工作，这会影响元素的样式。 要查看其他选项，您可以阅读 Bootstrap 的文档，Shiny 使用的 CSS 设计系统：<http://bootstrapdocs.com/v3.3.6/docs/css/#buttons>。

### 2.2 输出

UI 中的输出创建占位符，稍后由服务器函数填充。 与输入一样，输出将唯一 ID 作为其第一个参数：如果您的 UI 规范创建了 ID 为“plot”的输出，您将在server函数中使用 output$plot 访问它。

前端的每个输出函数都与后端的渲染函数耦合。 有三种主要的输出类型，对应于您通常在报告中包含的三种内容：文本、表格和图表。 以下部分向您展示了前端输出函数的基础知识，以及后端相应的渲染函数。

#### (1)文本

使用 textOutput() 输出常规文本，使用 verbatimTextOutput() 输出固定代码和控制台输出。

```R
ui <- fluidPage(
  textOutput("text"),
  verbatimTextOutput("code")
)
server <- function(input, output, session) {
  output$text <- renderText({ 
    "Hello friend!" 
  })
  output$code <- renderPrint({ 
    summary(1:10) 
  })
}
```

请注意，只有在需要运行多行代码时，渲染函数才需要 {}。 正如您很快就会了解到的，您应该在渲染函数中进行尽可能少的计算，这意味着您通常可以忽略它们。 如果写得更紧凑，上面的server函数会是这样的：

```R
server <- function(input, output, session) {
  output$text <- renderText("Hello friend!")
  output$code <- renderPrint(summary(1:10))
}
```

请注意，有两个渲染函数的行为略有不同：

- renderText() 将结果组合成一个字符串，通常与 textOutput() 配对
- renderPrint() 打印结果，就像您在 R 控制台中一样，并且通常与 verbatimTextOutput() 配对。

我们可以看到玩具应用程序的不同之处：

```R
ui <- fluidPage(
  textOutput("text"),
  verbatimTextOutput("print")
)
server <- function(input, output, session) {
  output$text <- renderText("hello!")
  output$print <- renderPrint("hello!")
}
```

这相当于 base R 中 cat() 和 print() 之间的区别。

#### (2)表

在表中显示数据框有两个选项：

- tableOutput() 和 renderTable() 呈现静态数据表，同时显示所有数据。

- dataTableOutput() 和 renderDataTable() 呈现一个动态表，显示固定数量的行以及用于更改哪些行可见的控件。


tableOutput() 对于小型、固定的汇总（例如模型系数）最有用； 如果您想向用户公开完整的数据框，则 dataTableOutput() 是最合适的。 如果你想更好地控制 dataTableOutput() 的输出，我强烈推荐 Greg Lin 的 reactable 包。

```R
ui <- fluidPage(
  tableOutput("static"),
  dataTableOutput("dynamic")
)
server <- function(input, output, session) {
  output$static <- renderTable(head(mtcars))
  output$dynamic <- renderDataTable(mtcars, options = list(pageLength = 5))
}
```

#### (3)图

您可以使用 plotOutput() 和 renderPlot() 显示任何类型的 R 图形（base、ggplot2 或其他）：

```R
ui <- fluidPage(
  plotOutput("plot", width = "400px")
)
server <- function(input, output, session) {
  output$plot <- renderPlot(plot(1:5), res = 96)
}
```

默认情况下，plotOutput() 将占据其容器的整个宽度（稍后会详细介绍），并且高度为 400 像素。 您可以使用高度和宽度参数覆盖这些默认值。 我们建议始终设置 res = 96，因为这将使您的 Shiny 图与您在 RStudio 中看到的尽可能接近。

图很特别，因为它们是输出，也可以作为输入。 plotOutput() 有许多参数，例如 click、dblclick 和 hover。 如果你给它们传递一个字符串，比如 click = "plot_click"，它们将创建一个反应性输入 (input$plot_click)，你可以用它来处理用户在绘图上的交互，例如 点击情节。

#### (4)下载

您可以让用户使用 downloadButton() 或 downloadLink() 下载文件。这些需要server函数中的新技术。后面介绍。

## 3.基础响应

在 Shiny 中，您可以使用反应式编程来表达您的服务器逻辑。 响应式编程是一种优雅而强大的编程范式，但一开始它可能会让人迷惑，因为它与编写脚本的范式截然不同。 反应式编程的关键思想是指定一个依赖关系图，以便当输入发生变化时，所有相关的输出都会自动更新。 这使应用程序的流程变得相当简单，但是您需要花一些时间来了解它们是如何组合在一起的。

本章将简要介绍反应式编程，教你在 Shiny 应用程序中使用的最常见反应式结构的基础知识。 我们将从server函数的调查开始，更详细地讨论输入和输出参数的工作方式。 接下来我们将回顾最简单的反应形式（输入直接连接到输出），然后讨论反应表达式如何让您消除重复的工作。 最后，我们将回顾 Shiny 新用户遇到的一些常见障碍。

### 3.1 server 函数

```R
library(shiny)

ui <- fluidPage(
  # front end interface
)

server <- function(input, output, session) {
  # back end logic
}

shinyApp(ui, server)
```

上一部分涵盖了前端的基础知识，即包含呈现给应用程序每个用户的 HTML 的 ui 对象。 用户界面很简单，因为每个用户都获得相同的 HTML。 server更复杂，因为每个用户都需要获得独立版本的应用程序； 当用户 A 移动滑块时，用户 B 不应该看到他们的输出发生变化。

为了实现这种独立性，Shiny 会在每次新会话启动时调用您的 server() 函数。 就像任何其他 R 函数一样，当服务器函数被调用时，它会创建一个新的本地环境，该环境独立于该函数的所有其他调用。 这允许每个会话都有一个唯一的状态，以及隔离在函数内部创建的变量。 这就是为什么您在 Shiny 中进行的几乎所有响应式编程都将在server函数中进行的原因。

server函数采用三个参数：input, output和 session。 因为您永远不会自己调用server函数，所以您永远不会自己创建这些对象。 相反，它们是由 Shiny 在会话开始时创建的，连接回特定会话。 目前，我们将重点关注输入和输出参数，并将 session留到后面介绍。

### 3.2 输入

输入参数是一个类似列表的对象，包含从浏览器发送的所有输入数据，根据输入 ID 命名。例如，如果您的 UI 包含一个输入 ID 为 count 的数字输入控件，如下所示：

```R
ui <- fluidPage(
  numericInput("count", label = "Number of values", value = 100)
)
```

然后您可以使用 input$count 访问该输入的值。它最初包含值 100，并且会随着用户在浏览器中更改值而自动更新。

与典型的列表不同，输入对象是只读的。如果您尝试修改服务器函数内的输入，您将收到错误消息：

```R
server <- function(input, output, session) {
  input$count <- 10  
}

shinyApp(ui, server)
#> Error: Can't modify read-only reactive value 'count'
```

发生此错误是因为输入反映了浏览器中发生的事情，而浏览器是 Shiny 的“单一事实来源”。 如果你可以修改 R 中的值，你可能会引入不一致，输入滑块在浏览器中说的是一个东西，而 `input$count` 在 R 中说的是不同的东西。这会给编程带来挑战！后面将学习如何使用 updateNumericInput() 等函数修改浏览器中的值，然后 input$count 将相应更新。

关于输入的另一件重要的事情是：它对允许阅读它的人是有选择性的。 要从输入中读取，您必须处于由 renderText() 或 reactive() 等函数创建的反应上下文中。 我们很快就会回到这个想法，但这是一个重要的约束，它允许输出在输入更改时自动更新。 这段代码说明了如果你犯了这个错误你会看到的错误：

```R
server <- function(input, output, session) {
  message("The value of input$count is ", input$count)
}

shinyApp(ui, server)
#> Error: Can't access reactive value 'count' outside of reactive consumer.
#> ℹ Do you need to wrap inside reactive() or observer()?
```

### 3.3 输出

output 与 input 非常相似：它也是一个根据输出 ID 命名的类列表对象。 主要区别在于您使用它来发送输出而不是接收输入。 您始终将输出对象与渲染函数一起使用，如以下简单示例所示：

```R
ui <- fluidPage(
  textOutput("greeting")
)

server <- function(input, output, session) {
  output$greeting <- renderText("Hello human!")
}
```

（请注意，ID 在 UI 中引用，但在server中不引用。）

渲染函数做了两件事： 它设置了一个特殊的反应上下文，自动跟踪输出使用的输入。 它将 R 代码的输出转换为适合在网页上显示的 HTML。

### 3.4 响应式编程

如果一个应用程序只有输入或只有输出，它将会非常无聊。当您同时拥有一个应用程序时，Shiny 的真正魔力就会发生。让我们看一个简单的例子：

```R
ui <- fluidPage(
  textInput("name", "What's your name?"),
  textOutput("greeting")
)

server <- function(input, output, session) {
  output$greeting <- renderText({
    paste0("Hello ", input$name, "!")
  })
}
```

这是 Shiny 的重要思想：您无需告诉输出何时更新，因为 Shiny 会自动为您计算出来。 它是如何工作的？ 函数体中究竟发生了什么？ 让我们更准确地考虑server函数中的代码：

```R
output$greeting <- renderText({
  paste0("Hello ", input$name, "!")
})
```

这很容易理解为“将‘hello’和用户名粘贴在一起，然后将其发送到 `output$greeting`。 但这种心智模式在微妙但重要的方面是错误的。 想一想：使用此模型，您只需发出一次指令。 但是 Shiny 会在我们每次更新 input$name 时执行该操作，所以肯定还有其他事情要做。

该应用程序之所以有效，是因为代码没有告诉 Shiny 创建字符串并将其发送到浏览器，而是通知 Shiny 如果需要如何创建字符串。 什么时候（即使！）代码应该运行取决于 Shiny。 它可能会在应用程序启动后立即运行，也可能会稍晚一些； 它可能会运行多次，也可能永远不会运行！ 这并不是说 Shiny 反复无常，只是说决定代码何时执行是 Shiny 的责任，而不是你的责任。 将您的应用程序视为向 Shiny 提供食谱，而不是向它发出命令。

#### (1) 命令式与声明式编程

commands和recipes之间的这种区别是两种重要的编程风格之间的主要区别之一：

- 在命令式编程中，您发出特定命令并立即执行。 这是您在分析脚本中习惯的编程风格：您命令 R 加载数据、转换数据、可视化数据并将结果保存到磁盘。
- 在声明式编程中，您表达更高层次的目标或描述重要的约束，并依靠其他人来决定如何和/或何时将其转化为行动。这是您在 Shiny 中使用的编程风格。

使用命令式代码，您可以说“给我做个三明治”。 使用声明性代码，您可以说“每当我查看冰箱内部时，确保冰箱里有三明治”。 命令式代码是自信的； 声明性代码是被动攻击的。

大多数时候，声明式编程会极大地解放你：你描述你的总体目标，然后软件会计算出如何在没有进一步干预的情况下实现这些目标。 不利的一面是，有时您确切地知道自己想要什么，但您无法弄清楚如何以声明式系统理解的方式来构建它。 

#### (2) Laziness

Shiny 中声明式编程的优势之一是它允许应用程序非常懒惰。 Shiny 应用程序只会执行更新您当前可以看到的输出控件所需的最少工作量。 然而，这种懒惰会带来一个重要的缺点，您应该意识到这一点。 你能发现下面的server函数有什么问题吗？

```R
server <- function(input, output, session) {
  output$greting <- renderText({
    paste0("Hello ", input$name, "!")
  })
}
```

如果仔细观察，您可能会注意到我写的是 greting 而不是 greeting。 这不会在 Shiny 中产生错误，但它不会做你想要的。 greting 输出不存在，因此 renderText() 中的代码将永远不会运行。

如果你正在开发一个 Shiny 应用程序并且你无法弄清楚为什么你的代码永远不会运行，请仔细检查你的 UI 和服务器功能是否使用相同的标识符。

#### (3) The reactive graph

Shiny的懒惰还有一个重要的特点。在大多数R代码中，您可以通过从上到下阅读代码来理解执行顺序。这在Shiny中不起作用，因为代码只在需要时运行。为了理解执行顺序，您需要查看反应图，该图描述了输入和输出是如何连接的。上述应用程序的反应图非常简单，如图3.2所示。

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303022118190.png)

反应图包含一个符号代表每个输入和输出，只要输出访问输入，我们就将输入连接到输出。 该图告诉您，只要更改 name，就需要重新计算greeting。 我们经常将这种关系描述为 greeting 对 name 具有反应性依赖性。

请注意我们用于输入和输出的图形约定： name输入自然适合greeting输出。 我们可以将它们紧密排列在一起，如图 3.3 所示，以强调它们组合在一起的方式； 我们通常不会这样做，因为它只适用于最简单的应用程序。

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303022121236.png)

反应图是了解应用程序工作方式的强大工具。随着应用程序变得越来越复杂，快速绘制反应图的高级草图，以提醒您所有部分是如何组合在一起的，这通常很有用。在本书中，我们将向您展示反应图，以帮助您理解示例的工作原理。

#### (4) 反应式表达

在反应图中还有一个更重要的组件：反应表达式。我们将很快回到反应式表达式的细节；现在，将它们视为一种工具，通过在反应图中引入额外的节点来减少反应代码中的重复。

```R
server <- function(input, output, session) {
  string <- reactive(paste0("Hello ", input$name, "!"))
  output$greeting <- renderText(string())
}
```

响应式表达式接受输入并产生输出，因此它们具有结合了输入和输出特征的形状。希望这些形状能帮助您记住组件是如何组合在一起的。

#### (5) 执行顺序

理解代码运行的顺序完全由反应图决定是很重要的。这与大多数R代码不同，其中执行顺序由行的顺序决定。例如，我们可以翻转简单server函数中两行的顺序：

```R
server <- function(input, output, session) {
  output$greeting <- renderText(string())
  string <- reactive(paste0("Hello ", input$name, "!"))
}
```

你可能认为这会产生错误，因为 output$greeting 引用了一个尚未创建的反应式表达式 string。 但请记住 Shiny 是惰性的，因此代码仅在会话启动时运行，在创建字符串之后。

相反，此代码生成与上面相同的反应图，因此代码运行的顺序完全相同。 像这样组织你的代码会让人类感到困惑，最好避免。 相反，请确保反应式表达式和输出仅引用上面定义的内容，而不是下面定义的内容。 这将使您的代码更易于理解。

这个概念非常重要并且与大多数其他 R 代码不同，所以我再说一遍：反应代码的运行顺序仅由反应图决定，而不是由它在服务器函数中的布局决定。

### 3.5 反应式表达

我们已经快速浏览了几次响应式表达式，因此您希望对它们可能做什么有所了解。 现在我们将深入了解更多细节，并展示为什么它们在构建真实应用程序时如此重要。

响应式表达式很重要，因为它们为 Shiny 提供了更多信息，因此它可以在输入更改时减少重新计算，从而提高应用程序的效率，并且它们通过简化响应式图使人们更容易理解应用程序。 响应式表达式具有输入和输出两种风格：

与输入一样，您可以在输出中使用反应式表达式的结果。 

与输出一样，反应式表达式依赖于输入并自动知道何时需要更新。

这种二元性意味着我们需要一些新的词汇：我将使用生产者来指代反应性输入和表达式，使用消费者来指代反应性表达式和输出。用维恩图显示了这种关系。

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303022130371.png)

我们将需要一个更复杂的应用程序来了解使用反应式表达式的好处。首先，我们将通过定义一些我们将用于为我们的应用程序提供动力的常规 R 函数来设置阶段。

#### (1) The motivation

想象一下，我想用绘图和假设检验来比较两个模拟数据集。 我做了一些实验并提出了以下函数：freqpoly() 用频率多边形可视化两个分布，t_test() 使用 t 检验比较均值并用字符串总结结果：

```R
library(ggplot2)

freqpoly <- function(x1, x2, binwidth = 0.1, xlim = c(-3, 3)) {
  df <- data.frame(
    x = c(x1, x2),
    g = c(rep("x1", length(x1)), rep("x2", length(x2)))
  )

  ggplot(df, aes(x, colour = g)) +
    geom_freqpoly(binwidth = binwidth, size = 1) +
    coord_cartesian(xlim = xlim)
}

t_test <- function(x1, x2) {
  test <- t.test(x1, x2)
  
  # use sprintf() to format t.test() results compactly
  sprintf(
    "p value: %0.3f\n[%0.2f, %0.2f]",
    test$p.value, test$conf.int[1], test$conf.int[2]
  )
}
```

如果我有一些模拟数据，我可以使用这些函数来比较两个变量：

```R
x1 <- rnorm(100, mean = 0, sd = 0.5)
x2 <- rnorm(200, mean = 0.15, sd = 0.9)

freqpoly(x1, x2)
cat(t_test(x1, x2))
#> p value: 0.005
#> [-0.39, -0.07]
```

在实际分析中，您可能会在使用这些函数之前进行大量的探索。我跳过了这里的探索，以便我们可以尽快进入应用程序。但将命令式代码提取到常规函数中是所有Shiny应用程序的一项重要技术：从应用程序中提取的代码越多，就越容易理解。这是一个很好的软件工程，因为它有助于隔离关注点：应用程序外部的功能专注于计算，因此应用程序内部的代码可以专注于响应用户操作。

#### (2)The app

我想使用这两个工具快速探索一系列模拟。Shiny应用程序是一个很好的方法，因为它可以让你避免冗长的修改和重新运行R代码。下面我将这些片段打包到一个Shiny应用程序中，在那里我可以交互式地调整输入。

让我们从UI界面开始。 我们将在后面回过头来看看 fluidRow() 和 column() 到底做了什么； 但是你可以从他们的名字猜出他们的用途😄。 第一行有三列用于输入控件（Distribution1、Distribution 2 和plot controls）。 第二行的宽列用于绘图，窄列用于假设检验。

```R
ui <- fluidPage(
  fluidRow(
    column(4, 
      "Distribution 1",
      numericInput("n1", label = "n", value = 1000, min = 1),
      numericInput("mean1", label = "µ", value = 0, step = 0.1),
      numericInput("sd1", label = "σ", value = 0.5, min = 0.1, step = 0.1)
    ),
    column(4, 
      "Distribution 2",
      numericInput("n2", label = "n", value = 1000, min = 1),
      numericInput("mean2", label = "µ", value = 0, step = 0.1),
      numericInput("sd2", label = "σ", value = 0.5, min = 0.1, step = 0.1)
    ),
    column(4,
      "Frequency polygon",
      numericInput("binwidth", label = "Bin width", value = 0.1, step = 0.1),
      sliderInput("range", label = "range", value = c(-3, 3), min = -5, max = 5)
    )
  ),
  fluidRow(
    column(9, plotOutput("hist")),
    column(3, verbatimTextOutput("ttest"))
  )
)
```

server函数在从指定的分布中绘制后组合调用 freqpoly() 和 t_test() 函数：

```R
server <- function(input, output, session) {
  output$hist <- renderPlot({
    x1 <- rnorm(input$n1, input$mean1, input$sd1)
    x2 <- rnorm(input$n2, input$mean2, input$sd2)
    
    freqpoly(x1, x2, binwidth = input$binwidth, xlim = input$range)
  }, res = 96)

  output$ttest <- renderText({
    x1 <- rnorm(input$n1, input$mean1, input$sd1)
    x2 <- rnorm(input$n2, input$mean2, input$sd2)
    
    t_test(x1, x2)
  })
}
```

#### (3)反应图

让我们从绘制此应用程序的反应图开始。 Shiny 足够聪明，只有在它所引用的输入发生变化时才更新输出;它不够聪明，只能有选择地在输出中运行代码片段。 换句话说，输出是原子的：它们要么被执行，要么不作为一个整体执行。

```R
x1 <- rnorm(input$n1, input$mean1, input$sd1)
x2 <- rnorm(input$n2, input$mean2, input$sd2)
t_test(x1, x2)
```

#### (4)简化图形

在下面的server函数中，我们重构现有代码，将重复的代码提取到两个新的响应式表达式中，并且模拟来自两个分布的数据。 为了创建一个反应式表达式，我们调用并将结果分配给一个变量。 为了稍后使用该表达式，我们像调用函数一样调用变量。

```
server <- function(input, output, session) {
  x1 <- reactive(rnorm(input$n1, input$mean1, input$sd1))
  x2 <- reactive(rnorm(input$n2, input$mean2, input$sd2))

  output$hist <- renderPlot({
    freqpoly(x1(), x2(), binwidth = input$binwidth, xlim = input$range)
  }, res = 96)

  output$ttest <- renderText({
    t_test(x1(), x2())
  })
}
```

## 4.页面布局

除了fluidPage（）之外，Shiny还提供了一些其他页面函数，这些函数可以在更特殊的情况下派上用场：fixedPage（）和fillPage（）。fixedPage（）的工作方式类似于fluidPage（），但具有固定的最大宽度，这可以防止应用程序在更大的屏幕上变得不合理。fillPage（）填充浏览器的整个高度，如果您想绘制占据整个屏幕的绘图，它非常有用。您可以在他们的文档中找到详细信息。

### 4.1 Page with sidebar

要制作更复杂的布局，您需要在 fluidPage() 中调用布局函数。 例如，要制作左侧输入和右侧输出的两列布局，您可以使用 sidebarLayout()（以及它的朋友 titlePanel()、sidebarPanel() 和 mainPanel()）。

```R
fluidPage(
  titlePanel(
    # app title/description
  ),
  sidebarLayout(
    sidebarPanel(
      # inputs
    ),
    mainPanel(
      # outputs
    )
  )
)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303022218068.png)

为了让它更真实，让我们添加一个输入和输出来创建一个非常简单的应用程序来演示中心极限定理，如图所示。 如果您自己运行这个应用程序，您可以增加样本数量以查看分布变得更加正常。

```R
ui <- fluidPage(
  titlePanel("Central limit theorem"),
  sidebarLayout(
    sidebarPanel(
      numericInput("m", "Number of samples:", 2, min = 1, max = 100)
    ),
    mainPanel(
      plotOutput("hist")
    )
  )
)
server <- function(input, output, session) {
  output$hist <- renderPlot({
    means <- replicate(1e4, mean(runif(input$m)))
    hist(means, breaks = 20)
  }, res = 96)
}
```

### 4.2 Multi-row

在幕后，sidebarLayout() 构建在灵活的多行布局之上，您可以直接使用它来创建视觉上更复杂的应用程序。 像往常一样，您从 fluidPage() 开始。 然后使用 fluidRow() 创建行，使用 column() 创建列。

```R
fluidPage(
  fluidRow(
    column(4, 
      ...
    ),
    column(8, 
      ...
    )
  ),
  fluidRow(
    column(6, 
      ...
    ),
    column(6, 
      ...
    )
  )
)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303030849375.png)

每行由 12 列组成，column() 的第一个参数给出要占用的列数。 12 列布局为您提供了极大的灵活性，因为您可以轻松创建 2、3 或 4 列布局，或使用窄列来创建间隔符。 

如果您想了解有关使用网格系统进行设计的更多信息，我强烈推荐有关该主题的经典文章：Josef Müller-Brockman 撰写的“[Grid systems in graphic design](https://www.amazon.com/dp/3721201450)”。

### 4.3 Multi-page layouts

随着您的应用程序变得越来越复杂，可能无法将所有内容都放在一个页面上。 在本节中，您将了解 tabPanel() 的各种用法，这些用法可以创建多个页面的错觉。 这是一种错觉，因为您仍然会有一个应用程序和一个底层 HTML 文件，但它现在被分解成多个部分并且一次只能看到一个部分。

模块允许您以与划分用户界面相同的方式划分server函数，创建仅通过明确定义的连接进行交互的独立组件。

#### (1)Tabsets

将页面分解成多个部分的简单方法是使用 tabsetPanel() 及其密友 tabPanel()。 正如您在下面的代码中看到的那样，tabsetPanel() 为任意数量的 tabPanels() 创建了一个容器，该容器又可以包含任何其他 HTML 组件。

```R
ui <- fluidPage(
  tabsetPanel(
    tabPanel("Import data", 
      fileInput("file", "Data", buttonLabel = "Upload..."),
      textInput("delim", "Delimiter (leave blank to guess)", ""),
      numericInput("skip", "Rows to skip", 0, min = 0),
      numericInput("rows", "Rows to preview", 10, min = 1)
    ),
    tabPanel("Set parameters"),
    tabPanel("Visualise results")
  )
)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303030855354.png)

如果您想知道用户选择了哪个选项卡，您可以向 tabsetPanel() 提供 id 参数，它成为一个输入。

```R
ui <- fluidPage(
  sidebarLayout(
    sidebarPanel(
      textOutput("panel")
    ),
    mainPanel(
      tabsetPanel(
        id = "tabset",
        tabPanel("panel 1", "one"),
        tabPanel("panel 2", "two"),
        tabPanel("panel 3", "three")
      )
    )
  )
)
server <- function(input, output, session) {
  output$panel <- renderText({
    paste("Current panel: ", input$tabset)
  })
}
```

注意 tabsetPanel() 可以在您应用的任何地方使用；如果需要，将选项卡集嵌套在其他组件（包括选项卡集！）中是完全可以的。

#### (2) Navlists and navbars

由于选项卡是水平显示的，因此您可以使用的选项卡数量存在基本限制，尤其是当它们的标题很长时。 navbarPage() 和 navbarMenu() 提供了两种可供选择的布局，让您可以使用更多带有更长标题的选项卡。

navlistPanel() 与 tabsetPanel() 类似，但它不是水平运行选项卡标题，而是在侧边栏中垂直显示它们。

```R
ui <- fluidPage(
  navlistPanel(
    id = "tabset",
    "Heading 1",
    tabPanel("panel 1", "Panel one contents"),
    "Heading 2",
    tabPanel("panel 2", "Panel two contents"),
    tabPanel("panel 3", "Panel three contents")
  )
)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303030858192.png)

另一种方法是使用 navbarPage()：它仍然水平运行选项卡标题，但您可以使用 navbarMenu() 添加下拉菜单以增加层次结构。

```R
ui <- navbarPage(
  "Page title",   
  tabPanel("panel 1", "one"),
  tabPanel("panel 2", "two"),
  tabPanel("panel 3", "three"),
  navbarMenu("subpanels", 
    tabPanel("panel 4a", "four-a"),
    tabPanel("panel 4b", "four-b"),
    tabPanel("panel 4c", "four-c")
  )
)
```

这些布局为您提供了创建丰富且令人满意的应用程序的强大能力。要走得更远，您需要了解有关底层设计系统的更多信息。

### 4.4 Bootstrap

要继续您的应用定制之旅，您需要更多地了解 Shiny 使用的 Bootstrap 框架。 Bootstrap 是 HTML 约定、CSS 样式和 JS 片段的集合，它们被捆绑成一种方便的形式。 Bootstrap 源自最初为 Twitter 开发的框架，在过去 10 年中已发展成为网络上使用最流行的 CSS 框架之一。 Bootstrap 在 R 中也很流行——你无疑已经看过很多由 rmarkdown::html_document() 生成的文档，并使用过许多由 pkgdown 制作的包网站，它们都使用了 Bootstrap。

作为一个 Shiny 开发者，你不需要过多考虑 Bootstrap，因为 Shiny 函数会自动为你生成 bootstrap 兼容的 HTML。 但很高兴知道 Bootstrap 的存在，因为这样：

您可以使用 bslib::bs_theme() 自定义代码的视觉外观。

您可以使用 class 参数使用 Bootstrap 类名自定义一些布局、输入和输出。

您可以创建自己的函数来生成 Shiny 不提供的 Bootstrap 组件，如“[Utility classes](https://rstudio.github.io/bslib/articles/theming.html#utility-classes)”中所述。

也可以使用完全不同的 CSS 框架。 许多现有的 R 包通过包装 Bootstrap 的流行替代品使这变得容易：

Appsilon 的 shiny.semantic 建立在 formantic UI 之上。

RInterface 的 shinyMobile 建立在框架 7 之上，专为移动应用程序而设计。

Eric Anderson 的 shinymaterial 建立在 Google 的 Material 设计框架之上。

同样由 RStudio 开发的 shinydashboard 提供了一个用于创建仪表板的布局系统。

您可以在 https://github.com/nanxstats/awesome-shiny-extensions 找到更完整且积极维护的列表。

### 4.5 Themes

Bootstrap 在 R 社区中无处不在，很容易产生风格疲劳：一段时间后，每个 Shiny 应用程序和 Rmd 开始看起来都一样。 解决方案是使用 bslib 包进行主题化。 bslib 是一个相对较新的包，它允许您覆盖许多 Bootstrap 默认设置，以创建您独有的外观。 在我写这篇文章时，bslib 主要只适用于 Shiny，但正在努力将其增强的主题功能引入 RMarkdown、pkgdown 等。

如果您正在为您的公司制作应用程序，我强烈建议您花一点时间在主题设计上——根据您的公司风格指南设计您的应用程序主题是让您看起来不错的简单方法。

#### (1) Getting started

使用 bslib::bs_theme() 创建一个主题，然后使用页面布局函数的 theme 参数将其应用于应用程序：

```R
fluidPage(
  theme = bslib::bs_theme(...)
)
```

如果未指定，Shiny 将使用自创建以来基本使用的经典 Bootstrap v3 主题。 默认情况下，bslib::bs_theme() 将使用 Bootstrap v4。 如果您只使用内置组件，使用 Bootstrap v4 而不是 v3 不会导致问题。 如果您使用自定义 HTML，它可能会导致问题，因此您可以强制它与版本 = 3 的 v3 保持一致。

#### (2) Shiny themes

更改应用程序整体外观的最简单方法是使用 bslib::bs_theme() 的 bootswatch 参数选择一个预制的“bootswatch”主题。图显示了以下代码的结果，将“暗”切换为其他主题。

```R
ui <- fluidPage(
  theme = bslib::bs_theme(bootswatch = "darkly"),
  sidebarLayout(
    sidebarPanel(
      textInput("txt", "Text input:", "text here"),
      sliderInput("slider", "Slider input:", 1, 100, 30)
    ),
    mainPanel(
      h1(paste0("Theme: darkly")),
      h2("Header 2"),
      p("Some text")
    )
  )
)
```

或者，您可以使用 bs_theme() 的其他参数构建自己的主题，例如 bg（背景色）、fg（前景色）和 base_font。

```R
theme <- bslib::bs_theme(
  bg = "#0b3d91", 
  fg = "white", 
  base_font = "Source Sans Pro"
)
```

预览和自定义主题的一种简单方法是使用 bslib::bs_theme_preview(theme)。 这将打开一个闪亮的应用程序，显示应用许多标准控件时主题的外观，还为您提供用于自定义最重要参数的交互式控件。

#### (3) Plot themes

如果您大量自定义了应用程序的样式，您可能还想自定义绘图以匹配。 幸运的是，这真的很容易，这要归功于主题包，它自动为 ggplot2、lattice 和 base plots 设置主题。 只需在server函数中调用 thematic_shiny() 即可。

```
library(ggplot2)

ui <- fluidPage(
  theme = bslib::bs_theme(bootswatch = "darkly"),
  titlePanel("A themed plot"),
  plotOutput("plot"),
)

server <- function(input, output, session) {
  thematic::thematic_shiny()
  
  output$plot <- renderPlot({
    ggplot(mtcars, aes(wt, mpg)) +
      geom_point() +
      geom_smooth()
  }, res = 96)
}
```

### 4.6 Under the hood

Shiny 的设计使得作为 R 用户的你不需要了解 HTML 的细节。 但是，如果您了解一些 HTML 和 CSS，则可以进一步自定义 Shiny。 不幸的是，教授 HTML 和 CSS 超出了本书的范围，但是 MDN 的  [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics) 和 [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)基础教程是一个很好的起点。

最重要的是要知道所有输入、输出和布局函数背后并没有魔法：它们只是生成 HTML。 您可以通过直接在控制台中执行 UI 函数来查看该 HTML：

```R
fluidPage(
  textInput("name", "What's your name?")
)
```

```html
<div class="container-fluid">
  <div class="form-group shiny-input-container">
    <label for="name">What's your name?</label>
    <input id="name" type="text" class="form-control" value=""/>
  </div>
</div>
```

请注意，这是 <body> 标签的内容； Shiny 的其他部分负责生成 <head>。 如果你想包含额外的 CSS 或 JS 依赖，你需要学习 htmltools::htmlDependency()。 两个好的起点是 https://blog.r-hub.io/2020/08/25/js-r/#web-dependency-management 和 https://unleash-shiny.rinterface.com/htmltools-dependencies .html。

可以将您自己的 HTML 添加到 ui。 一种方法是通过 HTML() 函数包含文字 HTML。 在下面的示例中，我使用“原始字符常量r"()"，以便更容易地在字符串中包含引号：

```R
ui <- fluidPage(
  HTML(r"(
    <h1>This is a heading</h1>
    <p class="my-class">This is some text!</p>
    <ul>
      <li>First bullet</li>
      <li>Second bullet</li>
    </ul>
  )")
)
```

如果您是 HTML/CSS 专家，您可能有兴趣知道可以完全跳过 fluidPage() 并提供原始 HTML。有关详细信息，请参阅““[Build your entire UI with HTML](https://shiny.rstudio.com/articles/html-ui.html)”。

或者，您可以使用 Shiny 提供的 HTML 帮助器。 最重要的元素有常规函数，如 h1() 和 p()，所有其他元素都可以通过其他标签助手访问。 命名参数成为属性，未命名参数成为子参数，因此我们可以将上面的 HTML 重新创建为：

```R
ui <- fluidPage(
  h1("This is a heading"),
  p("This is some text", class = "my-class"),
  tags$ul(
    tags$li("First bullet"), 
    tags$li("Second bullet")
  )
)
```

使用代码生成 HTML 的一个优点是您可以将现有的 Shiny 组件交织到自定义结构中。例如，下面的代码使一段文本包含两个输出，一个是粗体：

```R
tags$p(
  "You made ", 
  tags$b("$", textOutput("amount", inline = TRUE)),
  " in the last ", 
  textOutput("days", inline = TRUE),
  " days " 
)
```

注意inline=TRUE的用法；textOutput（）默认值是生成一个完整的段落。
要了解更多有关使用HTML、CSS和JavaScript制作引人注目的用户界面的信息，我强烈推荐David Granjon的《 [Outstanding User Interfaces with Shiny](https://unleash-shiny.rinterface.com/index.html)》。

## 5.图形

### 5.1 Interactivity

plotOutput() 最酷的事情之一是，它不仅可以作为显示绘图的输出，还可以作为响应指针事件的输入。 这使您可以创建交互式图形，用户可以在其中直接与绘图上的数据进行交互。 交互式图形是一种功能强大的工具，具有广泛的应用范围。 我没有篇幅向您展示所有可能性，所以在这里我将重点介绍基础知识，然后为您指明资源以了解更多信息。

#### (1) Basics

绘图可以响应四种不同的 mouse事件：click、dblclick（双击）、hover（鼠标在同一位置停留片刻）和 brush（矩形选择工具）。 要将这些事件转换为 Shiny 输入，您需要为相应的 plotOutput() 参数提供一个字符串，例如 `plotOutput("plot", click = "plot_click")`。 这将创建一个 input$plot_click ，您可以使用它来处理鼠标在绘图上的点击。

这是一个处理鼠标点击的非常简单的例子。 我们注册 plot_click 输入，然后用它来更新鼠标点击坐标的输出。 

```R
ui <- fluidPage(
  plotOutput("plot", click = "plot_click"),
  verbatimTextOutput("info")
)

server <- function(input, output) {
  output$plot <- renderPlot({
    plot(mtcars$wt, mtcars$mpg)
  }, res = 96)

  output$info <- renderPrint({
    req(input$plot_click)
    x <- round(input$plot_click$x, 2)
    y <- round(input$plot_click$y, 2)
    cat("[", x, ", ", y, "]", sep = "")
  })
}
```

（注意 req() 的使用，以确保应用程序在第一次点击之前不执行任何操作，并且坐标是根据底层 wt 和 mpg 变量。）

以下部分更详细地描述了这些事件。 我们将从点击事件开始，然后简要讨论密切相关的 dblclick 和 hover。 然后您将了解brush事件，它提供了一个由四个边（xmin、xmax、ymin 和 ymax）定义的矩形“brush”。 然后我将给出几个用动作结果更新情节的例子，然后讨论 Shiny 中交互式图形的一些局限性。

#### (2) Clicking

点事件返回一个包含大量信息的相对丰富的列表。 最重要的组件是 x 和 y，它们给出了事件在数据坐标中的位置。 但我不打算谈论这个数据结构，因为你只会在相对罕见的情况下需要（如果你确实想要细节，请使用 Shiny gallery 中的这个应用程序）。 相反，您将使用 nearPoints() 帮助器，它会返回一个数据框，其中包含单击时 near24 的行，处理一堆繁琐的细节。

这是 nearPoints() 的一个简单示例，显示了有关事件附近点的数据表。

```R
ui <- fluidPage(
  plotOutput("plot", click = "plot_click"),
  tableOutput("data")
)
server <- function(input, output, session) {
  output$plot <- renderPlot({
    plot(mtcars$wt, mtcars$mpg)
  }, res = 96)
  
  output$data <- renderTable({
    nearPoints(mtcars, input$plot_click, xvar = "wt", yvar = "mpg")
  })
}
```

在这里，我们为 nearPoints() 提供了四个参数：作为绘图基础的数据框、输入事件和轴上变量的名称。 如果你使用 ggplot2，你只需要提供前两个参数，因为 xvar 和 yvar 可以自动从绘图数据结构中估算出来。 出于这个原因，我将在本章的其余部分使用 ggplot2。 这是用 ggplot2 重新实现的先前示例：

```R
ui <- fluidPage(
  plotOutput("plot", click = "plot_click"),
  tableOutput("data")
)
server <- function(input, output, session) {
  output$plot <- renderPlot({
    ggplot(mtcars, aes(wt, mpg)) + geom_point()
  }, res = 96)
  
  output$data <- renderTable({
    req(input$plot_click)
    nearPoints(mtcars, input$plot_click)
  })
}
```

您可能想知道 nearPoints() 到底返回了什么。这是使用 browser() 的好地方.

```R
...
  output$data <- renderTable({
    req(input$plot_click)
    browser()
    nearPoints(mtcars, input$plot_click)
  })
...
```

现在，在我启动应用程序并单击一个点后，我进入了交互式调试器，我可以在其中运行 nearPoints() 并查看它返回的内容：

```R
nearPoints(mtcars, input$plot_click)
#>             mpg cyl disp hp drat   wt  qsec vs am gear carb
#> Datsun 710 22.8   4  108 93 3.85 2.32 18.61  1  1    4    1
```

使用 nearPoints() 的另一种方法是使用 allRows = TRUE 和 addDist = TRUE。这将返回带有两个新列的原始数据框：

`dist_` 给出行和事件之间的距离（以像素为单位）。

`selected_` 表示它是否在点击事件附近（即它是否是在 allRows = FALSE 时返回的行）。

#### (3) Other point events

同样的方法同样适用于 click、dblclick 和 hover：只需更改参数的名称。 如果需要，您可以通过提供 clickOpts()、dblclickOpts() 或 hoverOpts() 而不是提供输入 ID 的字符串来获得对事件的额外控制。 这些很少需要，所以我不会在这里讨论它们； 有关详细信息，请参阅文档。

您可以在一个图上使用多种交互类型。 只需确保向用户解释他们可以做什么：使用鼠标事件与应用程序交互的一个缺点是它们不会立即被发现。

#### (4) Brushing

在图上选择点的另一种方法是使用brush，一种由四个边定义的矩形选区。 在 Shiny 中，一旦你掌握了 click 和 nearPoints() ，使用brush就很简单了：你只需切换到 brush 参数和 brushedPoints() 助手。

这是另一个简单的例子，显示了brush选择了哪些点。

```R
ui <- fluidPage(
  plotOutput("plot", brush = "plot_brush"),
  tableOutput("data")
)
server <- function(input, output, session) {
  output$plot <- renderPlot({
    ggplot(mtcars, aes(wt, mpg)) + geom_point()
  }, res = 96)
  
  output$data <- renderTable({
    brushedPoints(mtcars, input$plot_brush)
  })
}
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303031007723.png)

使用 brushOpts() 来控制颜色（填充和描边），或将刷亮`direction = "x"or"y"`的单个维度（例如，对于刷亮时间序列很有用）。

#### (5) Modifying the plot

到目前为止，我们已经在另一个输出中显示了交互的结果。 但是，当您在与之交互的同一个图中显示变化时，交互性的真正美妙之处就在于此。 不幸的是，这需要一种您尚未了解的高级反应性技术：reactiveVal()。

正如您可能从名称中猜到的那样，reactiveVal() 与 reactive() 非常相似。 您可以通过使用其初始值调用 reactiveVal() 来创建反应值，并以与反应式相同的方式检索该值：

```R
val <- reactiveVal(10)
val()
#> [1] 10
```

最大的不同是你也可以更新一个反应值，所有引用它的反应消费者都会重新计算。 反应值使用一种特殊的语法来更新——你可以像调用函数一样调用它，第一个参数是新值：

```R
val(20)
val()
#> [1] 20
```

这意味着使用当前值更新反应值看起来像这样：

```R
val(val() + 1)
val()
#> [1] 21
```

不幸的是，如果你真的尝试在控制台中运行这段代码，你会得到一个错误，因为它必须在反应环境中运行。 这使得实验和调试更具挑战性，因为您需要 browser() 或类似的方法来在对 shinyApp() 的调用中暂停执行。

现在，让我们把学习 reactiveVal() 的挑战放在一边，并告诉你为什么你可能会费心。 想象一下，您想要可视化单击与绘图上的点之间的距离。 在下面的应用程序中，我们首先创建一个反应值来存储这些距离，并使用一个常量对其进行初始化，该常量将在我们单击任何内容之前使用。 然后我们使用 observeEvent() 在单击鼠标时更新反应值，并使用 ggplot 可视化点大小的距离。

```R
set.seed(1014)
df <- data.frame(x = rnorm(100), y = rnorm(100))

ui <- fluidPage(
  plotOutput("plot", click = "plot_click", )
)
server <- function(input, output, session) {
  dist <- reactiveVal(rep(1, nrow(df)))
  observeEvent(input$plot_click,
    dist(nearPoints(df, input$plot_click, allRows = TRUE, addDist = TRUE)$dist_)  
  )
  
  output$plot <- renderPlot({
    df$dist <- dist()
    ggplot(df, aes(x, y, size = dist)) + 
      geom_point() + 
      scale_size_area(limits = c(0, 1000), max_size = 10, guide = NULL)
  }, res = 96)
}
```

这里有两个重要的 ggplot2 技术需要注意：

我在绘图之前将距离添加到数据框。 我认为在可视化之前将相关变量放在数据框中是一种很好的做法。
我将限制设置为 scale_size_area() 以确保大小在点击之间具有可比性。 为了找到正确的范围，我做了一些交互式实验，但如果需要，您可以计算出确切的细节（请参阅本章末尾的练习）。
这是一个更复杂的想法。 我想使用画笔逐步向选区添加点。 在这里，我使用不同的颜色显示选择，但您可以想象许多其他应用程序。 为了完成这项工作，我将 reactiveVal() 初始化为 FALSE 向量，然后使用 brushedPoints() 和 | 将画笔下的任何点添加到选区。 为了给用户一些重新开始的方式，我双击重置选择。 图 7.5 显示了正在运行的应用程序的几个屏幕截图。

```R
ui <- fluidPage(
  plotOutput("plot", brush = "plot_brush", dblclick = "plot_reset")
)
server <- function(input, output, session) {
  selected <- reactiveVal(rep(FALSE, nrow(mtcars)))

  observeEvent(input$plot_brush, {
    brushed <- brushedPoints(mtcars, input$plot_brush, allRows = TRUE)$selected_
    selected(brushed | selected())
  })
  observeEvent(input$plot_reset, {
    selected(rep(FALSE, nrow(mtcars)))
  })

  output$plot <- renderPlot({
    mtcars$sel <- selected()
    ggplot(mtcars, aes(wt, mpg)) + 
      geom_point(aes(colour = sel)) +
      scale_colour_discrete(limits = c("TRUE", "FALSE"))
  }, res = 96)
}
```

同样，我设置了比例限制，以确保图例（和颜色）在第一次点击后不会改变。

#### (6) 交互限制

在我们继续之前，重要的是要了解交互式图中的基本数据流，以便了解它们的局限性。 基本流程是这样的：

JavaScript 捕获鼠标事件。
Shiny 将鼠标事件数据发送回 R，告诉应用程序输入现在已过时。
重新计算所有下游反应性消费者。
plotOutput() 生成一个新的 PNG 并将其发送到浏览器。
对于本地应用程序，瓶颈往往是绘制绘图所花费的时间。 根据情节的复杂程度，这可能需要几分之一秒。 但对于托管应用程序，您还必须考虑将事件从浏览器传输到 R，然后将渲染图从 R 返回到浏览器所需的时间。

一般来说，这意味着不可能创建闪亮的应用程序，其中的动作和响应被认为是即时的（即情节似乎与您的动作同步更新）。 如果您需要那种速度，则必须在 JavaScript 中执行更多计算。 一种方法是使用包含 JavaScript 图形库的 R 包。 现在，在我写这本书的时候，我认为你会得到 plotly 包的最佳体验，正如 Carson Sievert 所著的交互式基于网络的数据可视化与 R，plotly 和 shiny 书中所记录的那样。

### 5.2 动态高度和宽度

本章的其余部分没有交互式图形那么令人兴奋，但包含了在某处涵盖的重要材料。

首先，可以使绘图大小具有反应性，因此宽度和高度会根据用户操作而变化。 为此，请为 renderPlot() 的宽度和高度参数提供零参数函数——这些现在必须在服务器中定义，而不是在 UI 中定义，因为它们可以更改。 这些函数应该没有参数并返回所需的像素大小。 它们在反应性环境中进行评估，因此您可以使绘图的大小动态变化。

以下应用程序说明了基本思想。 它提供了两个直接控制绘图大小的滑块。 图中显示了几个示例屏幕截图。 请注意，当您调整绘图大小时，数据保持不变：您不会获得新的随机数。

```R
ui <- fluidPage(
  sliderInput("height", "height", min = 100, max = 500, value = 250),
  sliderInput("width", "width", min = 100, max = 500, value = 250),
  plotOutput("plot", width = 250, height = 250)
)
server <- function(input, output, session) {
  output$plot <- renderPlot(
    width = function() input$width,
    height = function() input$height,
    res = 96,
    {
      plot(rnorm(20), rnorm(20))
    }
  )
}
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303031105091.png)

在实际应用中，您将在宽度和高度函数中使用更复杂的表达式。例如，如果您在 ggplot2 中使用分面图，您可以使用它来增加图的大小以保持各个分面大小大致相同。

### 5.3 Images

如果要显示现有图像（不是绘图），可以使用 renderImage()。 例如，您可能有一个要向用户显示的照片目录。 以下应用通过显示可爱的小狗照片来说明 renderImage() 的基础知识。 这些照片来自 https://unsplash.com，这是我最喜欢的免版税库存照片来源。

```R
puppies <- tibble::tribble(
  ~breed, ~ id, ~author, 
  "corgi", "eoqnr8ikwFE","alvannee",
  "labrador", "KCdYn0xu2fU", "shaneguymon",
  "spaniel", "TzjMd7i5WQI", "_redo_"
)

ui <- fluidPage(
  selectInput("id", "Pick a breed", choices = setNames(puppies$id, puppies$breed)),
  htmlOutput("source"),
  imageOutput("photo")
)
server <- function(input, output, session) {
  output$photo <- renderImage({
    list(
      src = file.path("puppy-photos", paste0(input$id, ".jpg")),
      contentType = "image/jpeg",
      width = 500,
      height = 650
    )
  }, deleteFile = FALSE)
  
  output$source <- renderUI({
    info <- puppies[puppies$id == input$id, , drop = FALSE]
    HTML(glue::glue("<p>
      <a href='https://unsplash.com/photos/{info$id}'>original</a> by
      <a href='https://unsplash.com/@{info$author}'>{info$author}</a>
    </p>"))
  })
}
```

renderImage() 需要返回一个列表。 唯一关键的参数是 src，图像文件的本地路径。 您还可以提供：

一个 contentType，它定义图像的 MIME 类型。 如果没有提供，Shiny 会根据文件扩展名进行猜测，所以如果您的图像没有扩展名，您只需要提供它。

图像的宽度和高度（如果已知）。

任何其他参数，如 class 或 alt 将作为属性添加到 HTML 中的 <img> 标记。

您还必须提供 deleteFile 参数。 不幸的是 renderImage() 最初设计用于处理临时文件，因此它会在渲染图像后自动删除图像。 这显然非常危险，因此 Shiny 1.5.0 中的行为发生了变化。 现在 shiny 不再删除图像，而是强制您明确选择您想要的行为。

您可以在 https://shiny.rstudio.com/articles/images.html 了解更多关于 renderImage() 的信息，并查看您可能使用它的其他方式。