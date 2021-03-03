def test_me(request):
    print(request.config.getoption("--demo"))

