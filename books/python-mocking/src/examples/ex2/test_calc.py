import app

def test_calc():
    input_values = ['19', '23']
    output = []

    def mock_input(s):
       output.append(s)
       return input_values.pop(0)
    app.input = mock_input
    app.print = lambda *s : output.append(s)

    app.calc()

    assert output == [
        'Type in a: ',
        'Type in b: ',
        ('The result is:', 42),
    ] 
