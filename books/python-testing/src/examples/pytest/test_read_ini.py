import configparser
import os


def test_read_ini(tmpdir):
    print(tmpdir)      # /private/var/folders/ry/z60xxmw0000gn/T/pytest-of-gabor/pytest-14/test_read0
    d = tmpdir.mkdir("subdir")
    fh = d.join("config.ini")
    fh.write("""
[application]
user  =  foo
password = secret
""")

    print(fh.basename) # data.txt
    print(fh.dirname)  # /private/var/folders/ry/z60xxmw0000gn/T/pytest-of-gabor/pytest-14/test_read0/subdir
    filename = os.path.join( fh.dirname, fh.basename )

    config = configparser.ConfigParser()
    config.read(filename)

    assert config.sections() == ['application']
    assert config['application'], {
       "user" : "foo",
       "password" : "secret"
    }

