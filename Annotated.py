from typing import Annotated;

#Annotation provides extra context to a variable

email=Annotated[str,"This has to be a valid email"];

#Reducer functions: how to merge the new data to the current state

state={"message":"Hello"}
update={"message":"Nice to meet you"}
new_state={"message":"Hello Nice to meet you"}; #Reducer appends