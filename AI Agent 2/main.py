from langgraph.graph import START,END,StateGraph;
from typing import TypedDict,List,Literal;
from langchain_core.messages import HumanMessage,AIMessage;
from langchain_groq import ChatGroq;
from dotenv import load_dotenv;

load_dotenv();
llm=ChatGroq(model="llama-3.1-8b-instant");

# Start -> ai process <- > END

class AgentState(TypedDict):
    ai_messages:List[AIMessage] 
    human_messages:List[HumanMessage]
    
def chat_with_llm(state:AgentState)->AgentState:
    prompt = input("Enter Prompt: ");
    state["human_messages"].append(HumanMessage(content=prompt));
    
    result=llm.invoke(state["human_messages"]);
    
    print(result.content);
    
    state["ai_messages"].append(AIMessage(result.content));
    return state;

LUserWantsToQuit = Literal["Q","C"]
def user_wants_to_quit(state:StateGraph)->LUserWantsToQuit:
    user_command=input("Q to quit and C to continue: ");
    if user_command == "Q":
        return "Q";
    return "C";

graph=StateGraph(AgentState);

graph.add_node("chat_with_llm",chat_with_llm);

graph.add_edge(START,"chat_with_llm");

graph.add_conditional_edges("chat_with_llm",user_wants_to_quit,{
    "Q":END,
    "C":"chat_with_llm"
})

app=graph.compile();

initial_state=AgentState(ai_messages=[],human_messages=[])
result=app.invoke(initial_state);
    