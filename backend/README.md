# 博客后端 


### package 信息

```
Package             Version
------------------- -------
asn1crypto          0.24.0 
bcrypt              3.1.7  
cffi                1.11.5 
configobj           5.0.6  
cryptography        2.8    
decorator           4.2.1  
gpg                 1.10.0 
idna                2.5    
iniparse            0.4    
netifaces           0.10.6 
paramiko            2.6.0  
pciutils            2.3.6  
pcp                 4.1    
perf                0.1    
Pillow              6.2.1  
pip                 9.0.3  
ply                 3.9    
psutil              5.6.4  
pycairo             1.16.3 
pycparser           2.14   
pygobject           3.28.3 
PyMySQL             0.9.3  
PyNaCl              1.3.0  
pyOpenSSL           18.0.0 
python-dateutil     2.6.1  
python-dmidecode    3.12.2 
python-linux-procfs 0.6    
pyudev              0.21.0 
redis               3.3.11 
rhnlib              2.8.6  
rpm                 4.14.2 
schedutils          0.6    
sepolicy            1.1    
setools             4.2.0  
setroubleshoot      1.1    
setuptools          39.2.0 
six                 1.11.0 
slip                0.6.4  
slip.dbus           0.6.4  
SQLAlchemy          1.3.10 
syspurpose          1.23.8 
systemd-python      234    
tornado             6.0.3  
```


### * AIP 说明*  
> 以 "/api/open/" 开头的url不需要登陆可以访问   
> 以 "/api/admin/" 开头的url需要登陆认证访问  
***
### 聊天功能
> "/api/open/chat/"
> 支持方法:websock  

***
### XSRF信息获取 
>  "/api/open/xsrf/"
> 支持方法: GET
***
### 获取验证码,(get 获取验证码, post 检查验证码)
> "/api/open/verify_code/"
***
### 前台主页()
> "/api/open/home/"
***
### 查看单个博客，(\d+)是博客ID
> "/api/open/blog/(\d+)/"
***
### 评论处理
> "/api/open/review/"
***
### 简历访问
> "/api/open/resume/"
***
### 音乐功能
> "/api/open/music/"
***

### 后台登陆
> "/api/admin/login/"
***
### 注销登陆
> "/api/admin/logout/"
***
### 后台主页仪表盘
> "/api/admin/dashboard/"
***
### 博客分类管理
> "/api/admin/classify/"
***
### 评论管理
> "/api/admin/review/"
***
### 博客列表
> "/api/admin/blog_list/"
*** 
### 博客增删改查
> "/api/admin/blog/"
***
### 博客标题存在性检查
> "/api/admin/blog_title_check/"
***
### 用户设置控制面板
> "/api/admin/setting/"
***
### 修改账号或密码
> "/api/admin/account/"
***
### 图片上传
> "/api/admin/upload/"
***
### 简历列表
> "/api/admin/resume_list/"
***
### 简历增删改查
> "/api/admin/resume/"
***
### 简历标题存在性检查
> "/api/admin/resume_title_check/"
***
### 简历发布列表
> "/api/admin/publish_list/"
***
### 简历发布增删改查
> "/api/admin/publish/"
***
### 简历访问码存在性检查
> "/api/admin/publish_access_code_check/"
***
### 主机性能监控
> "/api/admin/monitor/"
***
### 网盘(列出目录下的文件及文件夹)
> "/api/admin/dir_list/"
***
### 网盘(列出目录下的文件及文件夹以树形展示)
> "/api/admin/dir_tree/"
***
### 网盘(目录及文件相关操作)
> "/api/admin/net_disk/"
***
### SSH远程
> "/api/admin/web_ssh/"
***
### 404 错误
> ".*"
***

