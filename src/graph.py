from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from src.state import AgentState
from src.agents.researcher import researcher_node
from src.agents.analyst import analyst_node
from src.agents.reporter import reporter_node
from src.tools.search_tools import get_search_tool

# Set up tools
tools = [get_search_tool()]
tool_node = ToolNode(tools)

#Maximum number of times a researcher can search for each topic
MAX_RESEARCH_ATTEMPTS = 3

# Decision after the researcher: Do we need tools or should we continue with the analyst?
def decide_after_researcher(state: AgentState):
    last_message = state["messages"][-1]

    # If the researcher requests the use of a tool
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"

    
    return "analyst"

# Decision after the analyst: Should we go back and investigate or release the report?
def decide_after_analyst(state: AgentState):
    last_message = state["messages"][-1].content

    # Reading the researcher's current number of attempts
    attempts = state.get("researcher_attempts", 0)

    if "INCOMPLETE" in last_message:
        if attempts < MAX_RESEARCH_ATTEMPTS:
            state["researcher_attempts"] = attempts + 1
            return "researcher" 
        else:
            print("⚠ تم الوصول للحد الأقصى لمحاولات البحث. سنكمل بالتقرير المتاح.")
            return "reporter" 

    #Complete data View the report
    return "reporter"

# Graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("researcher", researcher_node)
workflow.add_node("tools", tool_node)
workflow.add_node("analyst", analyst_node)
workflow.add_node("reporter", reporter_node)

#Starting point
workflow.set_entry_point("researcher")


workflow.add_conditional_edges(
    "researcher",
    decide_after_researcher,
    {
        "tools": "tools",
        "analyst": "analyst"
    }
)

#The tools belong to the researcher.
workflow.add_edge("tools", "researcher")

#Conditional logic after analysis with a limit on attempts
workflow.add_conditional_edges(
    "analyst",
    decide_after_analyst,
    {
        "researcher": "researcher",
        "reporter": "reporter"
    }
)

# End of the system
workflow.add_edge("reporter", END)

# Compile the application
app = workflow.compile()
