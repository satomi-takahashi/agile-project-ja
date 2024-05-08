from main import addition, check_choice, check_calculation_input
import io

def test_addition():
    cases = [
        (1,2,3),
        (1.1,2,3.1),
    ]

    for case in cases:
        assert addition(case[0], case[1]) == case[2]

def test_check_choice(monkeypatch):
    choices = ("1","2","3","4","5","6")
    cases = [
        "1\n",#改行\nが必要
        "7\n",#改行\nが必要
    ]

    for case in cases:
        monkeypatch.setattr('sys.stdin', io.StringIO(case))
        res = check_choice("test", choices, test=True)

        if case[:1] in choices:
            assert res == case[:1]
        else:
            assert res == "Invalid input. Input correct choice."

def test_check_calculation_input(monkeypatch):
    pass_cases = [
        (True, True, "10\n"),
        (True, False, "0\n"),
        (False, True, "-10\n"),
        (False, False, "0\n"),
        (False, False, "-10\n"),
    ]

    fail_cases = [
        (True, True, "-10\n", "Negative value is not allowed. Input positive float."),
        (True, True, "0\n", "Zero is not allowed. Input none zero."),
        (True, False, "-10\n", "Negative value is not allowed. Input positive float."),
        (False, True, "0\n", "Zero is not allowed. Input none zero."),
        (True, True, "aaa\n", "Invalid data. Input float."),
    ]

    for case in pass_cases:
        monkeypatch.setattr('sys.stdin', io.StringIO(case[2]))
        res = check_calculation_input(message="test", 
                                      ans=10, 
                                      negative_not_allowed=case[0],
                                      zero_not_allowed=case[1],
                                      test=True)
        assert res == float(case[2][:-1])

    for case in fail_cases:
        monkeypatch.setattr('sys.stdin', io.StringIO(case[2]))
        res = check_calculation_input(message="test", 
                                      ans=10, 
                                      negative_not_allowed=case[0],
                                      zero_not_allowed=case[1],
                                      test=True)
        assert res == case[3]