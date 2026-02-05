from typing import Annotated, TypedDict, List
from langgraph.graph.message import add_messages

class AgentState(TypedDict):

#add_messages makes the Graph merge new messages with the original old ones
    messages: Annotated[List, add_messages]
    report_content: str
    researcher_attempts: int  
