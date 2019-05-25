# extract_frame
if you need README.MD in english, Please pull requset. This is a simple program, it will be have some bug.
you can change it by yourself. 

此程序功能为批量提取视频帧
已测试通过环境：
windows10+Python3.7+cv2
ubuntu18.04+python3.6+cv2


具体使用后面会录制bilibili视频，目前实现的功能有：
批量提取视频中的帧
按照指定帧数间隔提取视频帧

使用方法
安装python3:建议使用python3.7
安装pip,windows10安装python3后会自带，其他系统请查询对应的方法安装pip
安装cv2

下面为windows10在命令行下执行安装cv2
更新pip：python -m pip install --upgrade pip
下载cv2：pip install opencv-python
如果你没有设置pip国内镜像源，会发现下载速度非常慢（我刚开始不知道用镜像源，足足等了30分钟，手动哭脸），
可使用国内镜像下载，以下为使用清华镜像
使用镜像更新pip：python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
使用镜像下载CV2：pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple

环境配置完成

运行程序
打开命令行切换到代码所在路径或者直接在代码所在文件内启动命令行
python extract_frame.py
输入视频所在路径
输入截图保存路径
输入视频后缀名
输入帧数间隔

ubuntu18.04环境配置，以下命令已默认使用镜像源
系统默认已经安装Python3.6
其他安装需要root权限如果觉得输入密码烦，可以直接 sudo su使账户暂时获得root权限

使用镜像更新pip：sudo python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

使用镜像下载CV2：sudo pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple

运行程序：切换到程序所在目录，打开命令行
sudo python extract_frame.py
等待程序运行，个人测试，3小时视频60帧/s的视频大概需10分钟左右

部分代码参考：https://blog.csdn.net/u010167269/article/details/53268686



