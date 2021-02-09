import app

def test_game():
    app.random.randint = lambda x, y: 70
    game = app.Game()
    print(game.hidden)
    response = game.guess(100)
    assert response == 'too big'

    response = game.guess(50)
    assert response == 'too small'

    response = game.guess(70)
    assert response == 'match'
