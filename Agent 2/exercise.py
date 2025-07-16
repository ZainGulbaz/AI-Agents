from langgraph.graph import START,END,StateGraph;
from typing import TypedDict,List,Literal;
import math;

class AgentState(TypedDict):
    name:str;
    values:List[int];
    results:str;
    operation: Literal["*","+"]


def calculate_node(state:AgentState)->AgentState:
    
    operation=state["operation"]
    
        
    if operation is None:
        state["results"]="Please provide an operator * or +";
    elif operation == "+":
        state["results"]="Hi "+state["name"]+", Your results are "+str(sum(state["values"]));
    elif operation == "*":
        state["results"]="Hi "+state["name"]+", Your results are "+str(math.prod((state["values"])));
    
    return state;

graph=StateGraph(AgentState);

graph.add_node("calculate_node",calculate_node);

graph.add_edge(START,"calculate_node");
graph.add_edge("calculate_node",END);

app=graph.compile();

with open("graph2.png","wb") as f:
    f.write(app.get_graph().draw_mermaid_png());
    
initial_state=AgentState(values=[1,2],name="Zain Gulbaz");

results=app.invoke(initial_state);

print(results);
    