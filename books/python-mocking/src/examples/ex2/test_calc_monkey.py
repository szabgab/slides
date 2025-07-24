import app

def test_calc(monkeypatch):
    input_values = ['19', '23']
    output = []

    def mock_input(s):
       output.append(s)
       return input_values.pop(0)
    monkeypatch.setattr(app, 'input', mock_input, raising=False)
    monkeypatch.setattr(app, 'print', lambda *s : output.append(s), raising=False)
    
    app.calc()

    assert output == [
        'Type in a: ',
        'Type in b: ',
        ('The result is:', 42),
    ] 
