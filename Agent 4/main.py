from langgraph.graph import START,END,StateGraph;
from typing import TypedDict,Literal,List;
import math;

class AgentState(TypedDict):
    operation:Literal["*","+"]
    values:List[int]
    result:int


    
def multiply(state:AgentState)->AgentState:
    state["result"]= math.prod(state["values"]);
    return state;
def add(state:AgentState)->AgentState:
    state["result"]=sum(state["values"]);
    return state;

def operation_condition(state:AgentState) -> Literal["multiply_op","addition_op"]:
    print(state);
    if state["operation"]=="*":
        return "multiply_op";
    elif state["operation"]=="+":
        return "addition_op";

graph=StateGraph(AgentState);
graph.add_node("multiply",multiply);
graph.add_node("addition",add);
graph.add_node("router",lambda state:state);

graph.add_edge(START,"router");
graph.add_conditional_edges("router",operation_condition,{
    "multiply_op":"multiply",
    "addition_op":"addition"
});
graph.add_edge("addition",END);
graph.add_edge("multiply",END);
app=graph.compile();

with open("graph.png","wb") as f:
    f.write(app.get_graph().draw_mermaid_png());
    
results=app.invoke({"values":[1,2],"operation":"+"});

print(results);