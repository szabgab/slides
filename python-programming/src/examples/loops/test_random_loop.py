import while_break
import while_complex_condition
import while_true

import random
import pytest

@pytest.mark.parametrize('seed', [0, 7, 9, 21])
def test_random_loop(capsys, seed):
    random.seed(seed)
    while_complex_condition.random_loop()
    out_complex, _ = capsys.readouterr()

    random.seed(seed)
    while_break.random_loop()
    out_break, _ = capsys.readouterr()

    assert out_complex == out_break

    random.seed(seed)
    while_true.random_loop()
    out_true, _ = capsys.readouterr()
    assert out_complex == out_true

    print(out_true)

def test_newest_random_loop_0(capsys):
    expected = """0
12
25
26
34
50
65
77
done
"""
    random.seed(0)
    while_true.random_loop()
    out_true, _ = capsys.readouterr()
    assert out_true == expected

def test_newest_random_loop_7(capsys):
    expected = """0
10
14
26
27
29
46
49
60
78
79
95
101
102
104
117
130
132
139
141
158
done
"""
    random.seed(7)
    while_true.random_loop()
    out_true, _ = capsys.readouterr()
    assert out_true == expected


