# Chinese-relation-extraction
中文关系提取，这个仓库是在[thunlp/Tensorflow-NRE](https://github.com/thunlp/TensorFlow-NRE)基础上改的。原始项目是支持英文的，这个项目对原始代码做了些修改可以支持中文。

## Overview
* Embedding
  * Word embedding
  * Position embedding
* Encoder
  * PCNN
  * CNN
  * RNN
  * Bidirection RNN
* Selector
  * Attention
  * Maximum
  * Average
* Classifier
  * Softmax Loss Function
  * Output

## Requirements
- Python (>=2.7)
- Numpy (>=1.13.3)
- TensorFlow (>=1.4.1)
    - CUDA (>=8.0) if you are using gpu
- Matplotlib (>=2.0.0)
- scikit-learn (>=0.18)

## How to use and data
具体的用法参照原文，原文中数据转换比较麻烦，为了方便大家我将转换完的数据放在了云盘上，大家可自行下载。[nyt](https://pan.baidu.com/s/1F8RaD4UKhbKKXrfoxU--uw)，密码：pkas
[origindata](https://pan.baidu.com/s/1YWi_KBl2cx0Oq3mxKP58_Q)，密码：3uyg

## Reference
* [thunlp/Tensorflow-NRE](https://github.com/thunlp/TensorFlow-NRE)