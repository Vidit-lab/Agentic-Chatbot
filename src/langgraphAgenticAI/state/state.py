from typing_extensions import TypedDict ,List
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
    Represents the structure of the state used in graph
    """
    #This info will be shared with various nodes in the graph
    messages: Annotated[List,add_messages]