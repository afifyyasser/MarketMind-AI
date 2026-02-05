from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage
from src.tools.search_tools import get_search_tool
import os
MODEL_NAME = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")  


def researcher_node(state):
    llm = ChatGroq(model=MODEL_NAME)
    search_tool = get_search_tool()
    
   # Linking the tool to artificial intelligence
    llm_with_tools = llm.bind_tools([search_tool])
    
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
                                           
If market data is uncertain or missing:
You MUST use the search tool before answering.

"""
    ))
    
    messages = [system_prompt] + state['messages']
    response = llm_with_tools.invoke(messages)
    
    return {"messages": [response]}