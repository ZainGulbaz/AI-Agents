from langchain_groq import ChatGroq;
from dotenv import load_dotenv;
from langgraph.graph import START,END,StateGraph;
from typing import TypedDict,List;
from langchain_core.messages import HumanMessage,AIMessage;

load_dotenv();
llm=ChatGroq(model="llama-3.1-8b-instant");



class AgentGraph(TypedDict):
    human_messages:List[HumanMessage];
    ai_messages:List[AIMessage];



def process_node(state:AgentGraph)->AgentGraph:    
    result=llm.invoke(state["human_messages"]);
    state["ai_messages"].append(AIMessage(content=result.content));
    return state;


graph=StateGraph(AgentGraph);

graph.add_node("process_node",process_node);

graph.add_edge(START,"process_node");
graph.add_edge("process_node",END);

app=graph.compile();

with open("draw.png","wb") as f:
    f.write(app.get_graph().draw_mermaid_png());

inital_state=AgentGraph(human_messages=[HumanMessage(content="What is 2+2")],ai_messages=[]);
result=app.invoke(inital_state);

print(result);

