from langgraph.graph import START,END,StateGraph;
from typing import TypedDict,Literal;

class AgentState(TypedDict):
    name:str;
    counter:int;
    result:str;
    
graph=StateGraph(AgentState);

def grettings_node(state:AgentState)->AgentState:
    state["result"]="Hello "+state["name"];
    return state;

def random_node(state:AgentState)->AgentState:
    state["counter"]+=1;
    return state;

check_condition_literal=Literal["end","random"]
def check_condition(state:AgentState)->check_condition_literal:
    if state["counter"] == 5:
        return "end";
    return "random";

graph=StateGraph(AgentState);

graph.add_node("greetings_node",grettings_node);
graph.add_node("random_node",random_node);

graph.add_edge(START,"greetings_node");
graph.add_edge("greetings_node","random_node");
graph.add_conditional_edges("random_node",check_condition,{
    "end":END,
    "random":"random_node"
})

app=graph.compile();

with open("graph.png","wb") as f:
    f.write(app.get_graph().draw_mermaid_png());

result = app.invoke({"name":"Zain","counter":1})

print(result);
