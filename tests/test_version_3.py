from tests.flo import Flo


def test_cheater():
    Flo.test("tests/version_2/cheat_and_fix.sim.txt")


def test_zilch():
    Flo.test("tests/version_2/zilch.sim.txt")