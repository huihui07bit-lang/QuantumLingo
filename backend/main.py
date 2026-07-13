"""
QuantumLingo - FastAPI 后端服务
把 quantum_core 的能力暴露成 HTTP API
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from quantum_core import parse_sentence, LAMBEQ_AVAILABLE

app = FastAPI(title="QuantumLingo API", version="0.1.0")

# 允许前端跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ParseRequest(BaseModel):
    sentence: str


@app.get("/")
def root():
    return {
        "service": "QuantumLingo",
        "status": "running",
        "lambeq_available": LAMBEQ_AVAILABLE,
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/parse")
def parse(req: ParseRequest):
    """接收句子，返回语法结构 + 量子线路"""
    result = parse_sentence(req.sentence)
    return result
