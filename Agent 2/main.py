from langgraph.graph import StateGraph,START,END;
from typing import TypedDict,List;

class AgentState(TypedDict):
    values:List[int];
    name:str;
    results:str;
    

def calculate_value(state:AgentState)->AgentState:
    state["results"]=" Hi "+state["name"]+" Your results are: "+str(sum(state["values"]));
    return state;

graph=StateGraph(AgentState);

graph.add_node("calculate_value",calculate_value);

graph.add_edge(START,"calculate_value");
graph.add_edge("calculate_value",END);

app=graph.compile();

with open("graph.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())

intial_sate=AgentState(values=[1,2],name="Zain")

result = app.invoke(intial_sate);

print(result);