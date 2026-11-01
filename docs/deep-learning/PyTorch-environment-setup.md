# pyTorch环境安装

## 1.GPU版本的安装

在安装软件之前，先查看CUDA官网和pyTorch官网的软件版本信息：

先查看目前pyTorch支持的系统以及CUDA和Python的版本：

<https://pytorch.org/get-started/locally/>

![1715310455247-745aebf9-5a15-4170-8f11-4861544b8d46.png](./img/PyTorch-environment-setup/1715310455247-745aebf9-5a15-4170-8f11-4861544b8d46-030420.png)

从上图可以看到，最新的 PyTorch 需要 Python 3.8 或更高版本。CUDA支持11.8和12.1。

然后在CUDA官网查看相关版本，选择12.1的版本进行下载和安装：

<https://developer.nvidia.com/cuda-toolkit-archive>

![1715310385930-a82dea95-276b-4b05-b09b-a8cbf14443fa.png](./img/PyTorch-environment-setup/1715310385930-a82dea95-276b-4b05-b09b-a8cbf14443fa-649080.png)

安装Visual Studio：<https://visualstudio.microsoft.com/zh-hans/vs/older-downloads/>

下载CUDA 12.1版本，还有根据自己的电脑系统版本选择下载，这里的我的系统是Win10。

![1715314178023-9f7f32cd-def5-4dfb-ab52-acf0ae36dd8f.png](./img/PyTorch-environment-setup/1715314178023-9f7f32cd-def5-4dfb-ab52-acf0ae36dd8f-379685.png)

下载后点击安装程序，弹出这个，临时抽取文件放置位置的，直接点击ok、随后进入系统兼容性的检查，就是看你是否下错安装包了。可以修改路径。

![1715314956293-c69539d2-2090-4a5d-a1b3-3770753ccf0e.png](./img/PyTorch-environment-setup/1715314956293-c69539d2-2090-4a5d-a1b3-3770753ccf0e-758498.png)

接下来会弹出下面页面：

![1715315008679-daf60d80-83cc-4384-93e4-256e9bc5c24b.png](./img/PyTorch-environment-setup/1715315008679-daf60d80-83cc-4384-93e4-256e9bc5c24b-369171.png)

点击同意并继续后，选择自定义。

![1715315031724-72a87e5d-3e52-4a9c-9600-37612e2e0341.png](./img/PyTorch-environment-setup/1715315031724-72a87e5d-3e52-4a9c-9600-37612e2e0341-881238.png)

点击下一步后，弹出下面窗口，把CUDA选一下，还需要注意一点，如果 你前面没有安装Visual Studio，直接安装的这个，需要把CUDA里面的Visual Studio Integration取消勾选，否则会安装不成功。

![1715315268433-726933bf-266e-4e01-b2e4-2628dafa4210.png](./img/PyTorch-environment-setup/1715315268433-726933bf-266e-4e01-b2e4-2628dafa4210-277248.png)

点击下一步：

![1715315227155-6363cd65-5851-479b-9d34-3b3c4c58c119.png](./img/PyTorch-environment-setup/1715315227155-6363cd65-5851-479b-9d34-3b3c4c58c119-580669.png)

点击下一步。

![1715315295414-501515e9-d51b-4dff-a3dc-31effdecf699.png](./img/PyTorch-environment-setup/1715315295414-501515e9-d51b-4dff-a3dc-31effdecf699-465270.png)

![1715315641613-b2047b1d-aa0a-498c-8249-a4750fd5be48.png](./img/PyTorch-environment-setup/1715315641613-b2047b1d-aa0a-498c-8249-a4750fd5be48-116839.png)

![1715315663496-683b2857-fff4-44f3-991b-c65e75d2b333.png](./img/PyTorch-environment-setup/1715315663496-683b2857-fff4-44f3-991b-c65e75d2b333-327282.png)

下面测试安装是否成功：

打开DOS窗口，输入`nvcc -V`，如果出现版本信息，证明安装成功。

![1715315797689-a30eecc1-10f5-4d46-bbc5-dc8c6e0f8936.png](./img/PyTorch-environment-setup/1715315797689-a30eecc1-10f5-4d46-bbc5-dc8c6e0f8936-283072.png)

如果提示没有nvcc命令，需要将nvcc路径（`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\bin`）添加至环境变量中。

![1715315976981-f33836b5-1547-49f6-8a88-78983bd99613.png](./img/PyTorch-environment-setup/1715315976981-f33836b5-1547-49f6-8a88-78983bd99613-620466.png)

CUDA里面有个demo_suite文件夹中有些工具，让我们测试，我们一起来试试吧 ，定位安装目录的demo_suite文件夹，我的是`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\extras\demo_suite`。

![1715316093380-810593e2-2600-40b4-9aa2-be8c914aa838.png](./img/PyTorch-environment-setup/1715316093380-810593e2-2600-40b4-9aa2-be8c914aa838-719743.png)

进入该文佳佳，输入<code>deviceQuery</code>，查询一下本机的gpu设备。

![1715316260305-93b47246-4f72-4151-9a96-a6595a5e0981.png](./img/PyTorch-environment-setup/1715316260305-93b47246-4f72-4151-9a96-a6595a5e0981-417517.png)

再来测试一下带宽，输入`bandwidthTest`。

![1715316309643-6d10942a-512a-4565-ae72-ce0379ea7fa7.png](./img/PyTorch-environment-setup/1715316309643-6d10942a-512a-4565-ae72-ce0379ea7fa7-689636.png)

接下来，就可以安装pyTorch。

![1715316407245-a113c518-1b52-4c94-a886-640df7b22362.png](./img/PyTorch-environment-setup/1715316407245-a113c518-1b52-4c94-a886-640df7b22362-626036.png)

安装可以直接复制上面命令直接安装，我们这里先创建一个虚拟环境后再进行安装。

在创建环境时，需要指定好安装的python版本，这里安装的 PyTorch 需要 Python 3.8 或更高版本。Python相关版本：<https://www.python.org/downloads/windows/>

![1715316735004-8d3c1399-8eb5-43c7-a789-99d5af9d2c70.png](./img/PyTorch-environment-setup/1715316735004-8d3c1399-8eb5-43c7-a789-99d5af9d2c70-247945.png)

这里我选择安装11.9的版本。

```plain
conda create -n pyTorchGPU python=3.11.9
conda activate pyTorchGPU
```

```plain
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

![1715321217178-cea05dd3-787a-4c0b-9f01-2b75628de2a4.png](./img/PyTorch-environment-setup/1715321217178-cea05dd3-787a-4c0b-9f01-2b75628de2a4-966999.png)

> 更新: 2024-05-10 14:07:23
> 原文: <https://www.yuque.com/doublehelix/bioinfonotes/cy0ntgkmg02pfsu6>
