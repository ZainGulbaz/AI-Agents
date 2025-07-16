from langgraph.graph  import START,END,StateGraph;
from typing import TypedDict;

class AgentState(TypedDict):
    age:str;
    name:str;
    result:str;
    
def first_node(state:AgentState)->AgentState:
    state["result"]=f"Hello "+state["name"];
    return state;

def second_node(state:AgentState) -> AgentState:
    state["result"]+="Your age is "+str(state["age"]);
    return state;

graph=StateGraph(AgentState);

graph.add_node("first_node",first_node);
graph.add_node("second_node",second_node);

graph.add_edge(START,"first_node");
graph.add_edge("first_node","second_node");
graph.add_edge("second_node",END);

app=graph.compile();

result = app.invoke({"name":"Zain","age":27});

print(result);