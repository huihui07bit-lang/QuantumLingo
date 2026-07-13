# QuantumLingo 🔮

将自然语言自动转换为量子线路的 **量子自然语言处理（QNLP）** 项目。
输入一句话，QuantumLingo 会基于范畴语法将其解析并编码为量子线路，进行可视化与量子计算模拟。

## ✨ 功能特性

- 🗣️ 输入自然语言句子，自动生成对应的量子线路
- ⚛️ 基于 lambeq 的范畴语法（DisCoCat）建模
- 🔬 使用 PennyLane 进行量子线路模拟
- 🌐 FastAPI 提供 RESTful 接口，浏览器即可访问

## 🛠️ 技术栈

| 层级 | 技术 |
|------|------|
| 后端框架 | FastAPI + Uvicorn |
| QNLP 核心 | lambeq |
| 量子计算 | PennyLane |
| 科学计算 | NumPy |
| 前端 | 原生 HTML |

## 📁 项目结构

```
QuantumLingo/
├── backend/                 # 后端
│   ├── main.py              # FastAPI 入口，提供 API 接口
│   ├── quantum_core.py      # QNLP 核心逻辑（lambeq + PennyLane）
│   └── requirements.txt     # 后端依赖
├── frontend/
│   └── index.html           # 前端界面
├── .gitignore
└── README.md
```

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/huihui07bit-lang/QuantumLingo.git
cd QuantumLingo
```

### 2. 启动后端

```bash
cd backend

# 创建并激活虚拟环境
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 启动服务
uvicorn main:app --reload
```

> 后端默认运行在 `http://127.0.0.1:8000`
> API 文档（自动生成）：`http://127.0.0.1:8000/docs`

### 3. 打开前端

直接用浏览器打开 `frontend/index.html` 即可访问界面。

## 📝 使用示例

在页面输入一句话（如 `Alice loves Bob`），QuantumLingo 会将其解析为量子线路并返回结果。

## 📄 License

MIT
