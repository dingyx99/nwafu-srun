# nwafu-srun
西北农林科技大学深澜认证脚本，使用 Python 3 编写。

其中 `main.py` 为交互式脚本，提供登录、查询信息和注销功能； `login.py` 仅提供登录功能，可以用于需要自动认证的环境。

## 使用方法

请先确保 Python 3 已经正常安装。交互式脚本与非交互式脚本用法相同，文件名请自行替换：

`python3 main.py -u <你的认证用户名> -p <你的密码>`

或

`python3 main.py --username=<你的认证用户名> --password=<你的密码>`

测试环境： Python 3.9.7 64-bit on macOS 12.0 Developer Beta 8(21A5534d)

## 致谢

[vincentimba/shenlan_xauat](https://github.com/vincentimba/shenlan_xauat): 项目灵感（其实是不想实现那个加密算法了）

## 许可

MIT License
