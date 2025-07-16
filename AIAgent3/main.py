from typing import TypedDict,Annotated,Sequence;
from langchain_core.messages import BaseMessage,HumanMessage,SystemMessage,AIMessage;
from langgraph.graph import START,END,StateGraph;
from langgraph.graph.message import add_messages;
from langchain.tools import tool;
from langchain_groq import ChatGroq;
from dotenv import load_dotenv;
from langgraph.prebuilt import tools_condition,ToolNode;

load_dotenv();

class AgentState(TypedDict):
    messages:Annotated[Sequence[BaseMessage],add_messages];
    

@tool
def add(a:int,b:int) -> int:
    """This method takes two int, adds them and return the answer"""
    return a+b;

tools=[add];

llm=ChatGroq(model="llama-3.1-8b-instant").bind_tools(tools);

def llm_node(state:AgentState):
    """The function takes the human message and give us a precised response"""
    prompt=input("Prompt: ");
    
    result = llm.invoke(HumanMessage(content=prompt));

    return {"messages":[AIMessage(content=result.content)]};

graph=StateGraph(AgentState);

tool_node=ToolNode(tools=tools);

graph.add_node("tools",tool_node);
graph.add_node("llm_node",llm_node);

graph.add_edge(START,"llm_node");
graph.add_conditional_edges("llm_node",tools_condition);
graph.add_edge("tools","llm_node");

app=graph.compile();

# with open("graph.png","wb") as f:
#     f.write(app.get_graph().draw_mermaid_png());


result=app.invoke({"messages":""});
print(result);