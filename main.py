from typing import TypedDict;
from langgraph.graph import StateGraph,START,END;
from IPython.display import Image,display;


class AgentState(TypedDict):
    message:str
    

def gretting_node(state:AgentState) -> AgentState:
    """ Simple Node that takes state and appends the message"""
    state["message"]="Hello "+state["message"]+" , how are you? ";
    return state;

    
graph=StateGraph(AgentState);

graph.add_node("gretting_node",gretting_node);

graph.add_edge(START,"gretting_node");
graph.add_edge("gretting_node",END);

app=graph.compile();

# with open("graph.png", "wb") as f:
#     f.write(app.get_graph().draw_mermaid_png())
    
result = app.invoke({"message":"Zain Gulbaz"});


print(result);