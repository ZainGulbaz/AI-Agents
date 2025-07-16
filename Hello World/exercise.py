from langgraph.graph import START,END,StateGraph;
from typing import TypedDict;

class AgentState(TypedDict):
    message:str

def gretting_node(state:AgentState)->AgentState:
    """ It is a simple node that takes the name and appends message state"""
    name= input("Please enter your name: ");
    state["message"]="Hello "+name+" You are doing a great work";
    
    return state;
    

graph=StateGraph(AgentState);

graph.add_node("gretting_node",gretting_node);

graph.add_edge(START,"gretting_node");
graph.add_edge("gretting_node",END);

app=graph.compile();

initial_state=AgentState(message="");
result=app.invoke(initial_state);

print(result);