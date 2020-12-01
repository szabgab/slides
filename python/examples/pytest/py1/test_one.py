def test_me(request):
    print(request.config.getoption("--demo"))
# pytest -s
# pytest -s --demo Hello
