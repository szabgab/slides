import os


def test_something(tmpdir):
    print(tmpdir)      # /private/var/folders/ry/z60xxmw0000gn/T/pytest-of-gabor/pytest-14/test_read0

    d = tmpdir.mkdir("subdir")
    fh = d.join("config.ini")
    fh.write("Some text")

    filename = os.path.join( fh.dirname, fh.basename )

    temp_dir = str(tmpdir)

    # ...
