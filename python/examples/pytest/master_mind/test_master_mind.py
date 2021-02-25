import master_mind as mm
import random

def test_mm():
    random.sample = lambda a, b: [1,2,3,4]
    input_values = ['1234']
    output = []

    def mock_input():
       #output.append(s)
       return input_values.pop(0)
    mm.input = mock_input
    mm.print = lambda *s : output.append(s)

    mm.main()

    assert output == [
        ("Please enter 4 digits",),
        ('Congrats!',),
    ] 


def test_wrong():
    random.sample = lambda a, b: [1,2,3,4]
    input_values = ['1235', '1234']
    output = []

    def mock_input():
       #output.append(s)
       return input_values.pop(0)
    mm.input = mock_input
    mm.print = lambda *s : output.append(s)

    mm.main()

    assert output == [
        ("Please enter 4 digits",),
        ("bbb",),
        ("Please enter 4 digits",),
        ('Congrats!',),
    ] 


