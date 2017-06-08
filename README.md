# 天猫淘宝商品评论爬虫说明

一个抓取天猫淘宝评论的Python爬虫。仍然能跑，2017/6。

![](doc/index.jpg)

使用python3.4，爬虫程序已经封装好，支持抓取天猫/淘宝的评论

>更多说明参考pdf

>更多说明参考pdf

>更多说明参考pdf

>更多说明参考pdf

# 一.项目结构

```
-----taobaocomment
	-------source	源代码
	-------excel	你要的结果
	-------run.bat	你要跑的脚本
	-------exe.rar	请解压变成exe
	-------taobao.txt	抓的商品网址
```

# 二.环境准备

安装[python3](https://www.python.org/downloads/)。然后设置环境变量设置。

## 1.安装依赖模块

依赖模块有`pymysql`, `xlswriter`, `bs4`

```
sudo pip3 install pymysql
sudo pip3 install xlsxwriter
sudo pip3 install bs4
```

其实你只要键入这个即可！

```
pip3 install -r requirement.txt

```
## 2.很难找到的模块

从[万能仓库](http://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_freeze) 下载对应版本的打包库,然后:

```
pip3 install cx_Freeze-4.3.4-cp35-none-win_amd64.whl
```

下载图形包`PIL`:

```
Pillow, a replacement for PIL, the Python Image Library, which provides image processing functionality and supports many file formats.
Use `from PIL import Image` instead of `import Image`.

    Pillow-3.3.0-cp27-cp27m-win32.whl
    Pillow-3.3.0-cp27-cp27m-win_amd64.whl
    Pillow-3.3.0-cp34-cp34m-win32.whl
    Pillow-3.3.0-cp34-cp34m-win_amd64.whl
    Pillow-3.3.0-cp35-cp35m-win32.whl
    Pillow-3.3.0-cp35-cp35m-win_amd64.whl

```

将`Pillow‑3.4.2‑cp34‑cp34m‑win32.whl` 改名 `Pillow‑3.4.2‑cp34‑none‑win32.whl` (装不了就改成none)

```
pip3 install Pillow‑3.4.2‑cp34‑none‑win32.whl
```

## 3.打包exe

转到源代码文件夹`source`

执行打包命令！

```
python setup.py build
```

把`exe.win32-3.4`文件夹移到根目录，改名为exe

# 三.开始使用

先往`taobao.txt`中按行写入商品链接

```
网址格式有如下几种(#开头的网址直接被忽视):
https://item.taobao.com/item.htm?spm=a1z10.1-c.w4004-7841214359.4.6lp4CP&id=525842199471
https://detail.tmall.com/item.htm?spm=a230r.1.14.6.o11GZI&id=41389303364&cm_id=140105335569ed55e27b&abbucket=3
https://item.taobao.com/item.htm?id=40066362090
https://rate.tmall.com/list_detail_rate.htm?itemId=45789209181&sellerId=2274061169&order=3&currentPage=2
https://item.taobao.com/item.htm?spm=a230r.1.14.37.B4SrL2&id=45804256292&ns=1&abbucket=3#detail
http://a.m.taobao.com/i44628690678.htm?&abtest=16&sid=ceff9ca9adb294b3459844e3640a76d1
```

执行

```
run.bat

或者
cd source
python taobaocomment.py

或者

pythonrun.bat
```


# 四.演示

![](doc/help.png)
![](doc/excel.png)


Do not understand?contact me.<br/>
author:hunterhug<br/>
2015/11

