# 个人网盘及文档管理项目

### 因多次注册某博客未果，决定自己开发，主要功能如下：

#### 前台功能：
- 个人资料
- 在线聊天
- 在线音乐
- 博客查看、搜索、评论、阅读及评论统计
- 简历查看功能

#### 后台功能：
- 仪表板,主要指标图标展示
- 在线聊天
- 在线音乐
- 博客分类增删改查
- 博客增删改查询
- 评论增删改查
- 简历增删改查
- 简历发布
- 简历阅读统计及邮件提醒
- 网盘,目录树
- 主机性能健康
- 主机SSH远程管理
- 动态前后台补丁

### 主要使用如下技术栈：

#### 后端：
Python 3.8 + tornado 6.0.3

#### 前端：
JavaScript + VUE 2.6.10 + chart

#### 数据库：
MySQL + Redis

---
### backend 后端代码实现

### frontend 前端代码实现

### install.txt 是部署参考说明

---
完整目录结构如下：
```
.
|-- README.md
|-- backend   # 后端Python实现
|   |-- README.md
|   `-- blog
|       |-- conf
|       |   |-- __init__.py
|       |   |-- conf.py                     # 生产环境配置文件
|       |   `-- dev_conf.py                 # 开发环境配置文件
|       |-- dao
|       |   |-- __init__.py
|       |   |-- accesslog.py
|       |   |-- base.py
|       |   |-- blog.py
|       |   |-- chat.py
|       |   |-- classify.py
|       |   |-- loginlog.py
|       |   |-- publish.py
|       |   |-- resume.py
|       |   |-- review.py
|       |   `-- setting.py
|       |-- dbinit.py
|       |-- handler
|       |   |-- __init__.py
|       |   |-- admin                      # 后台管理API功能实现
|       |   |   |-- __init__.py
|       |   |   |-- base.py
|       |   |   |-- blog.py
|       |   |   |-- classify.py
|       |   |   |-- dashboard.py
|       |   |   |-- login.py
|       |   |   |-- monitor.py
|       |   |   |-- netdisk.py
|       |   |   |-- publish.py
|       |   |   |-- resume.py
|       |   |   |-- review.py
|       |   |   |-- setting.py
|       |   |   |-- ssh.py
|       |   |   `-- upload.py
|       |   |-- base.py
|       |   `-- open                        # 前台开放API功能实现
|       |       |-- __init__.py
|       |       |-- base.py
|       |       |-- blog.py
|       |       |-- chat.py
|       |       |-- error.py
|       |       |-- home.py
|       |       |-- music.py
|       |       |-- publish.py
|       |       |-- review.py
|       |       |-- verifycode.py
|       |       `-- xsrf.py
|       |-- main.py
|       |-- model
|       |   |-- __init__.py
|       |   |-- base.py
|       |   |-- dbinit.py
|       |   `-- model.py
|       |-- service
|       |   |-- __init__.py
|       |   |-- accesslog.py
|       |   |-- base.py
|       |   |-- blog.py
|       |   |-- chat.py
|       |   |-- classify.py
|       |   |-- dashboard.py
|       |   |-- home.py
|       |   |-- login.py
|       |   |-- loginlog.py
|       |   |-- netdisk.py
|       |   |-- publish.py
|       |   |-- resume.py
|       |   |-- review.py
|       |   |-- setting.py
|       |   `-- ssh.py
|       |-- url.py
|       `-- util
|           |-- __init__.py
|           |-- acl.py
|           |-- actuator.py
|           |-- blogenum.py
|           |-- config.py
|           |-- exception.py
|           |-- font.ttf
|           |-- guard.py
|           |-- logger.py
|           |-- mail.py
|           |-- monitor.py
|           |-- session.py
|           |-- test.py
|           `-- verifycode.py
|-- frontend                            # 前端功能
|   |-- admin                           # 前端后台管理功能
|   |   |-- README.md
|   |   |-- babel.config.js
|   |   |-- package-lock.json
|   |   |-- package.json
|   |   |-- public
|   |   |   |-- favicon.ico
|   |   |   |-- img
|   |   |   |   |-- chat
|   |   |   |   |   |-- admin.png
|   |   |   |   |   |-- g0.ico
|   |   |   |   |   |-- g1.ico
|   |   |   |   |   |-- g10.ico
|   |   |   |   |   |-- g11.ico
|   |   |   |   |   |-- g12.ico
|   |   |   |   |   |-- g13.ico
|   |   |   |   |   |-- g14.ico
|   |   |   |   |   |-- g15.ico
|   |   |   |   |   |-- g16.ico
|   |   |   |   |   |-- g17.ico
|   |   |   |   |   |-- g2.ico
|   |   |   |   |   |-- g3.ico
|   |   |   |   |   |-- g4.ico
|   |   |   |   |   |-- g5.ico
|   |   |   |   |   |-- g6.ico
|   |   |   |   |   |-- g7.ico
|   |   |   |   |   |-- g8.ico
|   |   |   |   |   `-- g9.ico
|   |   |   |   |-- logo.png
|   |   |   |   `-- user.png
|   |   |   |-- index.html
|   |   |   `-- plugins
|   |   |       |-- adminlte
|   |   |       |   |-- css
|   |   |       |   |   |-- adminlte.min.css
|   |   |       |   |   `-- adminlte.min.css.map
|   |   |       |   `-- js
|   |   |       |       |-- adminlte.min.js
|   |   |       |       `-- adminlte.min.js.map
|   |   |       |-- bootstrap
|   |   |       |   `-- js
|   |   |       |       |-- bootstrap.bundle.min.js
|   |   |       |       `-- bootstrap.bundle.min.js.map
|   |   |       |-- chart
|   |   |       |   `-- js
|   |   |       |       |-- chart.min.css
|   |   |       |       `-- chart.min.js
|   |   |       |-- editer
|   |   |       |   `-- js
|   |   |       |       `-- editor.js
|   |   |       |-- fontawesome
|   |   |       |   |-- css
|   |   |       |   |   `-- all.min.css
|   |   |       |   `-- webfonts
|   |   |       |       |-- fa-brands-400.eot
|   |   |       |       |-- fa-brands-400.svg
|   |   |       |       |-- fa-brands-400.ttf
|   |   |       |       |-- fa-brands-400.woff
|   |   |       |       |-- fa-brands-400.woff2
|   |   |       |       |-- fa-regular-400.eot
|   |   |       |       |-- fa-regular-400.svg
|   |   |       |       |-- fa-regular-400.ttf
|   |   |       |       |-- fa-regular-400.woff
|   |   |       |       |-- fa-regular-400.woff2
|   |   |       |       |-- fa-solid-900.eot
|   |   |       |       |-- fa-solid-900.svg
|   |   |       |       |-- fa-solid-900.ttf
|   |   |       |       |-- fa-solid-900.woff
|   |   |       |       `-- fa-solid-900.woff2
|   |   |       `-- jquery
|   |   |           |-- jquery.min.js
|   |   |           `-- jquery.min.map
|   |   |-- src
|   |   |   |-- App.vue
|   |   |   |-- assets
|   |   |   |   `-- logo.png
|   |   |   |-- components
|   |   |   |   |-- Chat.vue
|   |   |   |   `-- Music.vue
|   |   |   |-- main.js
|   |   |   |-- router.js
|   |   |   |-- store.js
|   |   |   `-- views
|   |   |       |-- Home.vue
|   |   |       |-- Login.vue
|   |   |       `-- admin
|   |   |           |-- Blog.vue
|   |   |           |-- Classify.vue
|   |   |           |-- Dashboard.vue
|   |   |           |-- Monitor.vue
|   |   |           |-- Netdisk.vue
|   |   |           |-- Publish.vue
|   |   |           |-- Remote.vue
|   |   |           |-- Resume.vue
|   |   |           |-- Review.vue
|   |   |           `-- Setting.vue
|   |   `-- vue.config.js
|   `-- blog                            # 前端博客功能
|       |-- README.md
|       |-- babel.config.js
|       |-- package-lock.json
|       |-- package.json
|       |-- public
|       |   |-- favicon.ico
|       |   |-- img
|       |   |   |-- chat
|       |   |   |   |-- admin.png
|       |   |   |   |-- g0.ico
|       |   |   |   |-- g1.ico
|       |   |   |   |-- g10.ico
|       |   |   |   |-- g11.ico
|       |   |   |   |-- g12.ico
|       |   |   |   |-- g13.ico
|       |   |   |   |-- g14.ico
|       |   |   |   |-- g15.ico
|       |   |   |   |-- g16.ico
|       |   |   |   |-- g17.ico
|       |   |   |   |-- g2.ico
|       |   |   |   |-- g3.ico
|       |   |   |   |-- g4.ico
|       |   |   |   |-- g5.ico
|       |   |   |   |-- g6.ico
|       |   |   |   |-- g7.ico
|       |   |   |   |-- g8.ico
|       |   |   |   `-- g9.ico
|       |   |   |-- logo.png
|       |   |   `-- user.png
|       |   |-- index.html
|       |   `-- plugins
|       |       |-- adminlte
|       |       |   |-- css
|       |       |   |   |-- adminlte.min.css
|       |       |   |   `-- adminlte.min.css.map
|       |       |   `-- js
|       |       |       |-- adminlte.min.js
|       |       |       `-- adminlte.min.js.map
|       |       |-- bootstrap
|       |       |   `-- js
|       |       |       |-- bootstrap.bundle.min.js
|       |       |       `-- bootstrap.bundle.min.js.map
|       |       |-- chart
|       |       |   `-- js
|       |       |       |-- chart.min.css
|       |       |       `-- chart.min.js
|       |       |-- editer
|       |       |   `-- js
|       |       |       `-- editor.js
|       |       |-- fontawesome
|       |       |   |-- css
|       |       |   |   `-- all.min.css
|       |       |   `-- webfonts
|       |       |       |-- fa-brands-400.eot
|       |       |       |-- fa-brands-400.svg
|       |       |       |-- fa-brands-400.ttf
|       |       |       |-- fa-brands-400.woff
|       |       |       |-- fa-brands-400.woff2
|       |       |       |-- fa-regular-400.eot
|       |       |       |-- fa-regular-400.svg
|       |       |       |-- fa-regular-400.ttf
|       |       |       |-- fa-regular-400.woff
|       |       |       |-- fa-regular-400.woff2
|       |       |       |-- fa-solid-900.eot
|       |       |       |-- fa-solid-900.svg
|       |       |       |-- fa-solid-900.ttf
|       |       |       |-- fa-solid-900.woff
|       |       |       `-- fa-solid-900.woff2
|       |       `-- jquery
|       |           |-- jquery.min.js
|       |           `-- jquery.min.map
|       |-- src
|       |   |-- App.vue
|       |   |-- assets
|       |   |   `-- logo.png
|       |   |-- components
|       |   |   |-- Banner.vue
|       |   |   |-- Chat.vue
|       |   |   `-- Music.vue
|       |   |-- main.js
|       |   |-- router.js
|       |   |-- store.js
|       |   `-- views
|       |       |-- BlogList.vue
|       |       |-- BlogShow.vue
|       |       |-- Home.vue
|       |       `-- Resume.vue
|       `-- vue.config.js
`-- init.sh

```
