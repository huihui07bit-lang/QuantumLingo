"""
QuantumLingo - 量子语言核心模块
双层架构：优先使用 lambeq（真实量子NLP），不可用时降级到内置规则解析器
"""

import json

# ---------- 双层容错：尝试导入 lambeq ----------
try:
    from lambeq import BobcatParser
    LAMBEQ_AVAILABLE = True
except Exception:
    LAMBEQ_AVAILABLE = False


# ---------- 内置降级解析器（不依赖任何重型库） ----------
def fallback_parse(sentence: str) -> dict:
    """
    基于规则的轻量语法解析器。
    将句子拆词，按简单主谓宾规则赋予语法类型，
    并映射为一个概念性的量子线路结构。
    """
    words = sentence.strip().rstrip(".").split()
    n = len(words)

    # 简单词性/语法类型标注（教学演示用）
    typed_words = []
    for i, w in enumerate(words):
        if i == 0:
            gtype = "n"          # 名词（主语）
        elif i == n - 1 and n > 2:
            gtype = "n"          # 名词（宾语）
        else:
            gtype = "n.r @ s @ n.l"  # 及物动词
        typed_words.append({"word": w, "type": gtype})

    # 映射为量子线路：每个词一个 qubit，相邻词之间加纠缠门
    qubits = n
    gates = []
    for i in range(n):
        gates.append({"gate": "H", "qubit": i})          # 叠加
        gates.append({"gate": "RY", "qubit": i, "theta": round(0.5 * (i + 1), 3)})
    for i in range(n - 1):
        gates.append({"gate": "CNOT", "control": i, "target": i + 1})  # 纠缠

    return {
        "mode": "fallback",
        "sentence": sentence,
        "words": typed_words,
        "circuit": {
            "qubits": qubits,
            "gates": gates,
        },
    }


def parse_sentence(sentence: str) -> dict:
    """对外统一入口：优先 lambeq，否则降级。"""
    if LAMBEQ_AVAILABLE:
        try:
            parser = BobcatParser(verbose="suppress")
            diagram = parser.sentence2diagram(sentence)
            return {
                "mode": "lambeq",
                "sentence": sentence,
                "diagram_repr": str(diagram),
            }
        except Exception as e:
            result = fallback_parse(sentence)
            result["note"] = f"lambeq failed, used fallback: {e}"
            return result
    else:
        return fallback_parse(sentence)


# ---------- 自测 ----------
if __name__ == "__main__":
    print(f"[QuantumLingo] lambeq available: {LAMBEQ_AVAILABLE}\n")

    test_sentences = [
        "Alice loves Bob",
        "cats chase mice",
    ]

    for s in test_sentences:
        result = parse_sentence(s)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("-" * 50)
