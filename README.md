# envx
![](https://img.shields.io/badge/Python-3.8.6-green.svg)

#### 介绍
环境信息的管理模块

#### 软件架构
软件架构说明


#### 安装教程

1.  pip安装
```shell script
pip install envx
```
2.  pip安装（使用淘宝镜像加速）
```shell script
pip install envx -i https://mirrors.aliyun.com/pypi/simple
```

#### 使用说明

1.  demo
```python
import envx
redis_env = envx.read('redis.env')
```