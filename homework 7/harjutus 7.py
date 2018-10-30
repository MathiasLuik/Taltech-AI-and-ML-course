#tuple q st ja teisest osast.
#teha erinvevad listid 
#http://aima.cs.berkeley.edu/python/logic.html 
"""
 a1 & a2 & ... & an -> b      (mingi reegel)
 a1 & ... & an -> false       (tõestatav lause, seda pole meil vaja)
 a2                           (mingi fakt)
 a3                           (mingi teine fakt)
 
"""

print("l")
class KB_Agent(agents.Agent):
    """A generic logical knowledge-based agent. [Fig. 7.1]"""
    def __init__(self, KB):
        t = 0
        def program(percept):
            KB.tell(self.make_percept_sentence(percept, t))
            action = KB.ask(self.make_action_query(t))
            KB.tell(self.make_action_sentence(action, t))
            t = t + 1
            return action
        self.program = program

    def make_percept_sentence(self, percept, t):
        return(Expr("Percept")(percept, t))

    def make_action_query(self, t):
        return(expr("ShouldDo(action, %d)" % t))

    def make_action_sentence(self, action, t):
        return(Expr("Did")(action, t))
def fc_entails(kb, q):
    # kb - teadmusbaas mingil kujul
    # q - loogikamuutuja e. sümbol, mille kohta tahame teada, kas see järeldub kb-st


class PropHornKB(PropKB):
    "A KB of Propositional Horn clauses."

    def tell(self, sentence):
        "Add a Horn Clauses to this KB."
        op = sentence.op
        assert op == '>>' or is_prop_symbol(op), "Must be Horn Clause"
        self.clauses.append(sentence)

    def ask_generator(self, query):
        "Yield the empty substitution if KB implies query; else False"
        if not pl_fc_entails(self.clauses, query):
            return
        yield {}

    def retract(self, sentence):
        "Remove the sentence's clauses from the KB"
        for c in conjuncts(to_cnf(sentence)):
            if c in self.clauses:
                self.clauses.remove(c)

    def clauses_with_premise(self, p):
        """The list of clauses in KB that have p in the premise.
        This could be cached away for O(1) speed, but we'll recompute it."""
        return [c for c in self.clauses
                if c.op == '>>' and p in conjuncts(c.args[0])]

def pl_fc_entails(KB, q):
    """Use forward chaining to see if a HornKB entails symbol q. [Fig. 7.14]
    >>> pl_fc_entails(Fig[7,15], expr('Q'))
    True
    """
    count = dict([(c, len(conjuncts(c.args[0]))) for c in KB.clauses
                                                 if c.op == '>>'])
    inferred = DefaultDict(False)
    agenda = [s for s in KB.clauses if is_prop_symbol(s.op)]
    if q in agenda: return True
    while agenda:
        p = agenda.pop()
        if not inferred[p]:
            inferred[p] = True
            for c in KB.clauses_with_premise(p):
                count[c] -= 1
                if count[c] == 0:
                    if c.args[1] == q: return True
                    agenda.append(c.args[1])
    return False
#Fig[7,13] = expr("(B11 <=> (P12 | P21))  &  ~B11")
base="P>>Q   (L&M)>>P   (B&L)>>M   (A&P)>>L   (A&B)>>L   A   B"
PropHornKB()
#for s in "P>>Q   (L&M)>>P   (B&L)>>M   (A&P)>>L   (A&B)>>L   A   B".split():