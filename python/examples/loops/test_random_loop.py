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
