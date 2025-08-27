class DFA:
    def __init__(self, states, alphabet, start_state, accept_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

    def accepts(self, input):
        state = self.start_state
        for char in input:
            if (state, char) not in self.transitions:
                return False
            state = self.transitions[(state, char)]
        return state in self.accept_states


dfa1 = DFA(
    states={'a', 'b', '1'},
    alphabet={'0', '1'},
    start_state='a',
    accept_states={'1'},
    transitions={
        ('a', '0'): 'a',
        ('a', '1'): 'b',
        ('b', '0'): '1',
        ('b', '1'): 'a',
        ('1', '0'): 'b',
        ('1', '1'): '1'
    }
)

dfa2 = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    alphabet={'a', 'b'},
    start_state='q0',
    accept_states={'q3', 'q0'},
    transitions={
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q2',
        ('q1', 'a'): 'q0',
        ('q1', 'b'): 'q3',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q0',
        ('q3', 'a'): 'q2',
        ('q3', 'b'): 'q1'
    }
)


print("Automation 1: ")
for s in ["101", "11010", "1000", "1101", "1100", "10101"]:
    print(f"{s} : {'Accepted' if dfa1.accepts(s) else 'Rejected'}")
          

""""
OUTPUT
    101 : Accepted
    11010 : Accepted
    1000 : Accepted
    1101 : Rejected
    1100 : Rejected
    10101 : Rejected
"""

print()

print("Automation 2: ")
for s in ["baba", "babb", "ababba", "aaaab", "bbaba", "abbab"]:
    print(f"{s} : {'Accepted' if dfa2.accepts(s) else 'Rejected'}")


""""
OUTPUT
    baba : Accepted
    babb : Accepted
    ababba : Accepted
    aaaab : Rejected
    bbaba : Rejected
    abbab : Rejected
"""