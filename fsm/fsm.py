from typing import Dict, List
class FSM:

    """
    A simple finite state machine implementation
    params: start_state: the initial state of the FSM
            states: a dictionary of states and their transitions
            accepting_states: a list of states that are accepting
    """
    def __init__(self, start_state: str, states: Dict, accepting_states: List[str]) -> None:
        self.start_state = start_state
        self.state = start_state
        self.accepting_states = accepting_states
        self.states = states



    """
    Transition of FSM to a new state based on given input
    params: input: the input to the FSM 
    returns: None
    """
    def transition(self, input: str) -> None:
        if input in self.states[self.state]:
            self.state = self.states[self.state][input]
        else:
            raise ValueError(f"No transition defined for state {self.state} with input {input}")

    """
    Reset the FSM to the start state
    returns: None
    """    
    def reset(self) -> None:
        self.state = self.start_state

    """
    Check if the FSM is in an accepting state
    returns: True if the FSM is in an accepting state, False otherwise
    """
    def is_accepting(self) -> bool:
        return self.state in self.accepting_states
    
    """
    Run the FSM on the input
    params: input: the input to the FSM
    returns: Final state of the FSM after running on the input
    """
    def run(self, input: str) -> str: 
        for i in input:
            self.transition(i)
        return self.state
    

