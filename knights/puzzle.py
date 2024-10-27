from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A can only be a knight or a knave, not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # If A is a knight, then A's statement is true: A is both a knight and a knave
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is a knave, then A's statement is false: it is not true that A is both a knight and a knave
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A can only be a knight or a knave, not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # B can only be a knight or a knave, not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # If A is a knight, then A's statement is true: both A and B are knaves
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a knave, then A's statement is false: it is not true that both A and B are knaves
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A can only be a knight or a knave, not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # B can only be a knight or a knave, not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # If A is a knight, then A's statement is true: A and B are the same kind
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If A is a knave, then A's statement is false: it is not true that A and B are the same kind
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # If B is a knight, then B's statement is true: A and B are of different kinds
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    # If B is a knave, then B's statement is false: it is not true that A and B are of different kinds
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A can only be a knight or a knave, not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # B can only be a knight or a knave, not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # C can only be a knight or a knave, not both
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # A's statement (either "I am a knight" or "I am a knave")
    Or(
        # Either A claims to be a knight
        And(Implication(AKnight, AKnight),
            Implication(AKnave, Not(AKnight))),
        # Or A claims to be a knave
        And(Implication(AKnight, AKnave),
            Implication(AKnave, Not(AKnave)))
    ),

    # B's first statement: "A said 'I am a knave'"
    Implication(BKnight, And(Implication(AKnight, AKnave),
                             Implication(AKnave, Not(AKnave)))),
    Implication(BKnave, Not(And(Implication(AKnight, AKnave),
                                Implication(AKnave, Not(AKnave))))),

    # B's second statement: "C is a knave"
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # C's statement: "A is a knight"
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)
"""
knowledge3 = And(
    # 基本规则：每个人只能是骑士或knave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # A的陈述（A说自己是骑士或knave）
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),

    # B的两个陈述
    # 1. 关于A的陈述
    Implication(BKnight, AKnave),
    Implication(BKnave, Not(AKnave)),
    # 2. 关于C的陈述
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # C的陈述
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)
"""


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
