from main import addition, check_choice, check_calculation_input

def test_addition():
    cases = [
        (1,2,3),
        (1.1,2,3.1),
    ]

    for case in cases:
        assert addition(case[0], case[1]) == case[2]

test_addition()