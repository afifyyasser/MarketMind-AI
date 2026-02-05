from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage
import os
MODEL_NAME = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")  # أو استخدم "llama-3.1-8b-instant" للسرعة


def reporter_node(state):
    llm = ChatGroq(model=MODEL_NAME, temperature=0.7)
    
    system_prompt = SystemMessage(content=( """
You are a professional market research analyst.

Your task:
- Analyze the requested market thoroughly.
- Write the entire report in Arabic only.
- Do NOT use any English in the output.

Report structure:
## نظرة عامة على السوق
## حجم السوق والطلب
## الاتجاهات الحالية
## المشهد التنافسي
## الفرص والتحديات
## التوصيات الاستراتيجية

Style:
- Professional
- Clear
- Well-structured
"""
    ))
    
    messages = [system_prompt] + state['messages']
    response = llm.invoke(messages)
    
    return {
    "messages": state["messages"] + [response],
    "report_content": response.content
}
