from utils import (first,Expr, expr,subexpressions
)

from collections import defaultdict
_op_identity = {'&': True, '|': False, '+': 0, '*': 1}
def prop_symbols(x):
    """Return the set of all propositional symbols in x."""
    if not isinstance(x, Expr):
        return set()
    elif is_prop_symbol(x.op):
        return {x}
    else:
        return {symbol for arg in x.args for symbol in prop_symbols(arg)}
def is_variable(x):
    """A variable is an Expr with no args and a lowercase symbol as the op."""
    return isinstance(x, Expr) and not x.args and x.op[0].islower()
def extend(s, var, val):
    """Copy the substitution s and extend it by setting var to val; return copy.
    >>> extend({x: 1}, y, 2) == {x: 1, y: 2}
    True
    """
    s2 = s.copy()
    s2[var] = val
    return s2
def variables(s):
    """Return a set of the variables in expression s.
    >>> variables(expr('F(x, x) & G(x, y) & H(y, z) & R(A, z, 2)')) == {x, y, z}
    True
    """
    return {x for x in subexpressions(s) if is_variable(x)}
def pl_true(exp, model={}):
    """Return True if the propositional logic expression is true in the model,
    and False if it is false. If the model does not specify the value for
    every proposition, this may return None to indicate 'not obvious';
    this may happen even when the expression is tautological.
    >>> pl_true(P, {}) is None
    True
    """
    if exp in (True, False):
        return exp
    op, args = exp.op, exp.args
    if is_prop_symbol(op):
        return model.get(exp)
    elif op == '&':
        result = True
        for arg in args:
            p = pl_true(arg, model)
            if p is False:
                return False
            if p is None:
                result = None
        return result
    p, q = args
    if op == '==>':
        return pl_true(~p | q, model)
    pt = pl_true(p, model)
    if pt is None:
        return None
    qt = pl_true(q, model)
    if qt is None:
        return None

    else:
        raise ValueError("illegal operator in logic expression" + str(exp))
def is_prop_symbol(s):
    """A proposition logic symbol is an initial-uppercase string.
    >>> is_prop_symbol('exe')
    False
    """
    return is_symbol(s) and s[0].isupper()
def tt_check_all(kb, alpha, symbols, model):
    """Auxiliary routine to implement tt_entails."""
    if not symbols:
        if pl_true(kb, model):
            result = pl_true(alpha, model)
            assert result in (True, False)
            return result
        else:
            return True
    else:
        P, rest = symbols[0], symbols[1:]
        return (tt_check_all(kb, alpha, rest, extend(model, P, True)) and
                tt_check_all(kb, alpha, rest, extend(model, P, False)))
def pl_fc_entails(KB, q):
    count = {c: len(conjuncts(c.args[0]))
             for c in KB.clauses
             if c.op == '==>'} # loeb kui palju muutujaid on tuletamiseks vaja ja nimekirja tuletajatest
    inferred = defaultdict(bool)
    agenda = [s for s in KB.clauses if is_prop_symbol(s.op)]
    while agenda:       
        p = agenda.pop()
        if p == q:
            return True
        if not inferred[p]:
            inferred[p] = True
            for c in KB.clauses_with_premise(p):
                count[c] -= 1
                if count[c] == 0:
                    agenda.append(c.args[1])              
    
    return False

def is_symbol(s):
    """A string s is a symbol if it starts with an alphabetic char.
    >>> is_symbol('R2D2')
    True
    """
    return isinstance(s, str) and s[:1].isalpha()
def dissociate(op, args):
    """Given an associative op, return a flattened list result such
    that Expr(op, *result) means the same as Expr(op, *args).
    >>> dissociate('&', [A & B])
    [A, B]
    """
    result = []

    def collect(subargs):
        for arg in subargs:
            if arg.op == op:
                collect(arg.args)
            else:
                result.append(arg)
    collect(args)
    return result
def is_definite_clause(s):
    """Returns True for exprs s of the form A & B & ... & C ==> D,
    where all literals are positive.  In clause form, this is
    ~A | ~B | ... | ~C | D, where exactly one clause is positive.
    >>> is_definite_clause(expr('Farmer(Mac)'))
    True
    """
    #print(s)
    if is_symbol(s.op):
        return True
    elif s.op == '==>':
        antecedent, consequent = s.args
        return (is_symbol(consequent.op) and
                all(is_symbol(arg.op) for arg in conjuncts(antecedent)))
    else:
        return False

def associate(op, args):
    """Given an associative op, return an expression with the same
    meaning as Expr(op, *args), but flattened -- that is, with nested
    instances of the same op promoted to the top level.
    >>> associate('&', [(A&B),(B|C),(B&C)])
    (A & B & (B | C) & B & C)
    >>> associate('|', [A|(B|(C|(A&B)))])
    (A | B | C | (A & B))
    """
    args = dissociate(op, args)
    if len(args) == 0:
        return _op_identity[op]
    elif len(args) == 1:
        return args[0]
    else:
        return Expr(op, *args)
def distribute_and_over_or(s):
    """Given a sentence s consisting of conjunctions and disjunctions
    of literals, return an equivalent sentence in CNF.
    >>> distribute_and_over_or((A & B) | C)
    ((A | C) & (B | C))
    """
    s = expr(s)
    if s.op == '|':
        s = associate('|', s.args)
        if s.op != '|':
            return distribute_and_over_or(s)
        if len(s.args) == 0:
            return False
        if len(s.args) == 1:
            return distribute_and_over_or(s.args[0])
        conj = first(arg for arg in s.args if arg.op == '&')
        if not conj:
            return s
        others = [a for a in s.args if a is not conj]
        rest = associate('|', others)
        return associate('&', [distribute_and_over_or(c | rest)
                               for c in conj.args])
    elif s.op == '&':
        return associate('&', list(map(distribute_and_over_or, s.args)))
    else:
        return s
def move_not_inwards(s):
    """Rewrite sentence s by moving negation sign inward.
    >>> move_not_inwards(~(A | B))
    (~A & ~B)
    """
    s = expr(s)
    if is_symbol(s.op) or not s.args:
        return s
    else:
        return Expr(s.op, *list(map(move_not_inwards, s.args)))

def eliminate_implications(s):
    """Change implications into equivalent form with only &, |, and ~ as logical operators."""
    s = expr(s)
    if not s.args or is_symbol(s.op):
        return s  # Atoms are unchanged.
    args = list(map(eliminate_implications, s.args))
    a, b = args[0], args[-1]
    if s.op == '==>':
        return b | ~a
    else:
        assert s.op in ('&', '|', '~')
        return Expr(s.op, *args)
def to_cnf(s):
    """Convert a propositional logical sentence to conjunctive normal form.
    That is, to the form ((A | ~B | ...) & (B | C | ...) & ...) [p. 253]
    >>> to_cnf('~(B | C)')
    (~B & ~C)
    """
    s = expr(s)
    if isinstance(s, str):
        s = expr(s)
    s = eliminate_implications(s)  # Steps 1, 2 from p. 253
    s = move_not_inwards(s)  # Step 3
    return distribute_and_over_or(s)  # Step 4
def conjuncts(s):
    """Return a list of the conjuncts in the sentence s.
    >>> conjuncts(A & B)
    [A, B]
    >>> conjuncts(A | B)
    [(A | B)]
    """
    return dissociate('&', [s])
class KB:

    """A knowledge base to which you can tell and ask sentences.
    To create a KB, first subclass this class and implement
    tell, ask_generator, and retract.  Why ask_generator instead of ask?
    The book is a bit vague on what ask means --
    For a Propositional Logic KB, ask(P & Q) returns True or False, but for an
    FOL KB, something like ask(Brother(x, y)) might return many substitutions
    such as {x: Cain, y: Abel}, {x: Abel, y: Cain}, {x: George, y: Jeb}, etc.
    So ask_generator generates these one at a time, and ask either returns the
    first one or returns False."""

    def __init__(self, sentence=None):
        raise NotImplementedError

    def tell(self, sentence):
        """Add the sentence to the KB."""
        raise NotImplementedError


    def retract(self, sentence):
        """Remove sentence from the KB."""
        raise NotImplementedError

class PropKB(KB):
    """A KB for propositional logic. Inefficient, with no indexing."""

    def __init__(self, sentence=None):
        #print("ProbKB.__init__")
        self.clauses = []
        if sentence:
            self.tell(sentence)

    def tell(self, sentence):
        print("ProbKB.tell")
        """Add the sentence's clauses to the KB."""
        self.clauses.extend(conjuncts(to_cnf(sentence)))

    def retract(self, sentence):
        print("ProbKB.retract")
        """Remove the sentence's clauses from the KB."""
        for c in conjuncts(to_cnf(sentence)):
            if c in self.clauses:
                self.clauses.remove(c)

class PropDefiniteKB(PropKB):
    """A KB of propositional definite clauses."""

    def tell(self, sentence):
        #print("PropDefiniteKB.tell")
        """Add a definite clause to this KB."""
        assert is_definite_clause(sentence), "Must be definite clause"
        self.clauses.append(sentence)

    def retract(self, sentence):
        #print("PropDefiniteKB.retract")
        self.clauses.remove(sentence)

    def clauses_with_premise(self, p):
        #print("PropDefiniteKB.clauses_with_premise")
        """Return a list of the clauses in KB that have p in their premise.
        This could be cached away for O(1) speed, but we'll recompute it."""
        return [c for c in self.clauses
                if c.op == '==>' and p in conjuncts(c.args[0])]
"""
horn_clauses_KB = PropDefiniteKB()

for s in "P==>Q; (L&M)==>P; (B&L)==>M; (A&P)==>L; (A&B)==>L; A;B".split(';'):
    horn_clauses_KB.tell(expr(s))

horn_clauses_KB = PropDefiniteKB() 
"""

        #print(item)
def checkWhoWon(aiMove,playerMove):
    print("aimove = "+aiMove)
    print("playerMove = "+playerMove)
    if aiMove==playerMove:
        print("Draw")
    elif (aiMove=="Scissors" and playerMove=="Paper") or (aiMove=="Paper" and playerMove=="Rock") or (aiMove=="Rock" and playerMove=="Scissors"):
        print("AI won!!")
    else:
        print("Player won")
def getComputerMove(playerMove):
    if pl_fc_entails(rock_paper_scissors, expr("Scissors")):
        aiMove='Scissors'
        checkWhoWon(aiMove,playerMove)
    elif pl_fc_entails(rock_paper_scissors, expr("Rock")):
        aiMove='Rock'
        checkWhoWon(aiMove,playerMove)
    elif pl_fc_entails(rock_paper_scissors, expr("Paper")):
        aiMove='Paper'
        checkWhoWon(aiMove,playerMove)
    else:
        print("something wrong")
        
rock_paper_scissors= PropDefiniteKB()

rock_paper_scissors.tell(expr("(RockI&RockII)==>Paper"))
rock_paper_scissors.tell(expr("(PaperI&PaperII)==>Scissors"))
rock_paper_scissors.tell(expr("(ScissorsI&ScissorsII)==>Rock"))

rock_paper_scissors.tell(expr("(Rock1&PaperII)==>Scissors"))
rock_paper_scissors.tell(expr("(RockII&PaperI)==>Scissors"))

rock_paper_scissors.tell(expr("(ScissorsI&PaperII)==>Rock"))
rock_paper_scissors.tell(expr("(ScissorsII&PaperI)==>Rock"))

rock_paper_scissors.tell(expr("(RockI&ScissorsII)==>Paper"))
rock_paper_scissors.tell(expr("(RockII&ScissorsI)==>Paper"))


rock_paper_scissors.tell(expr("PaperI"))
rock_paper_scissors.tell(expr("RockII"))
input_list = ["Rock","Paper","Scissors"]
i=0
listOfPreviousMoves=["PaperI","RockII"]
while True:
    if i!=0:
        listOfPreviousMoves.pop(0)
    i+=1
    move = input("Rock,Paper or Scissors? ")
    if i%2==1 and move in input_list:
        player_move=move+"I"
    elif i%2==0 and move in input_list:
        player_move=move+"II"
    else:
        raise Exception("Wrong text")
    getComputerMove(move)
    rock_paper_scissors.retract(expr(listOfPreviousMoves[0]))
    rock_paper_scissors.tell(expr(player_move))
    listOfPreviousMoves.append(player_move)
