# RideLink - 拼车软件系统

RideLink是一个基于Vue.js和Flask的私家车拼车软件系统，提供简单的拼车服务管理功能。

## 技术栈

前端

- Vue.js 3
- Axios

后端

- Flask
- SQLite
- SQLAlchemy

## 项目结构

```
RideLink/
├── frontend/          # Vue.js前端项目
└── backend/           # Flask后端项目
```

## 快速开始

安装依赖：

```bash
# 前端依赖(如果已经有vue环境可以跳过)
# 检查 Node.js 和 npm 版本
node -v
npm -v
# 安装 Vue CLI
npm install -g @vue/cli
# 安装 axios
npm install axios

# 后端依赖
# 方法1：使用 requirements.txt
pip install -r requirements.txt

# 方法2：如果方法1失败，可以手动安装核心依赖
# 安装 Flask 相关依赖
pip install flask
pip install flask_sqlalchemy
pip install flask_cors
```

启动 Flask 后端：

```bash
cd backend
python app.py
```

启动 Vue 前端：

```bash
cd frontend
npm run serve
```

前端应用将通过 http://localhost:8080 访问，后端 Flask API 可通过 http://localhost:5000 访问。

## 功能特性

- 查看所有拼车信息
- 添加新的拼车信息
- 实时数据更新

## API接口

- GET /rides - 获取所有拼车信息
- POST /rides - 添加新的拼车信息
