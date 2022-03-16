from tests.flo import Flo


def test_quitter():
    Flo.test("tests/version_1/quitter.sim.txt")


def test_one_and_done():
    Flo.test("tests/version_1/one_and_done.sim.txt")


def test_hot_dice():
    Flo.test("tests/version_1/hot_dice.txt")


def test_bank_one_roll_then_quit():
    Flo.test("tests/version_1/bank_one_roll_then_quit.sim.txt")


def test_bank_first_for_two_rounds():
    Flo.test("tests/version_1/bank_first_for_two_rounds.sim.txt")

