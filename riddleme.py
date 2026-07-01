from logic import *

# suspect variables
low_level, joker, penguin, riddler = vars("low_level", "joker", "penguin", "riddler")

# clue variables
acid_burn, playing_cards, joy_buzzer, umbrella_mark, riddle, puzzle, word_game = vars("acid_burns", "playing_cards", "joy_buzzer", "umbrella_mark", "riddle", "puzzle", "word_game")


premises = [
    # at least one of these suspects
    low_level | joker | penguin | riddler,

    # based on crime clue and type
    joker >> (acid_burn | playing_cards | joy_buzzer),
    penguin >> umbrella_mark,
    riddler >> (riddle | puzzle | word_game),

    # was do we know is NOT true; Batman found whole that can be from umbrella or acid
    ~acid_burn,
    ~umbrella_mark,
    ~playing_cards,
    ~joy_buzzer,
    ~riddle,
    ~puzzle,
    ~word_game
]



suspects = {
    "A low-level criminal" : low_level,
    "The Joker" : joker,
    "The Penguin" : penguin,
    "The Riddler" : riddler
}


print("Who definitely committed this crime:")
for name, symbol in suspects.items():
    argument = ArgumentForm(*premises, conclusion=symbol)
    print(f"{name}: {argument.is_valid()}")