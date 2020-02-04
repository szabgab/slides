import sys
import os
import subprocess
import time

skip = [
    'python/examples/dictionary/generate_dna.py',
    'python/examples/dictionary/no_such_key.py',
    'python/examples/dictionary/count_words_in_file.py',
    'python/examples/dictionary/apache_access.py',
    'python/examples/dictionary/combine_lists.py',
    'python/examples/dictionary/change_in_loop.py',
    'python/examples/iterators/izip.py',
    'python/examples/iterators/mixer.py',
    'python/examples/iterators/pairwise.py',
    'python/examples/iterators/grouped.py',
    'python/examples/redis/set_get.py',
    'python/examples/redis/incrby.py',
    'python/examples/redis/incr.py',
    'python/examples/redis/setex.py',
    'python/examples/redis/keys.py',
    'python/examples/database/sql_select.py',
    'python/examples/database/sql_insert.py',
    'python/examples/package/3/setup.py',
    'python/examples/package/3/bin/runmymath.py',
    'python/examples/package/3/mymath/test/test_calc.py',
    'python/examples/package/3/mymath/test/test_all.py',
    'python/examples/package/use_project/proj1_2.py',
    'python/examples/package/use_project/proj2_1.py',
]

skip_flake = set([
    'python-programming/examples/sqla/orm_create_db.py',
    'python-programming/examples/decorators/function_assignment.py',
    'python-programming/examples/patterns/replace_print.py',
    'python-programming/examples/xml/sax_coroutine.py',
    'python-programming/examples/classes/abc/no_abc.py',
    'python-programming/examples/classes/only/fibonacci.py',
    'python-programming/examples/classes/limit/fibonacci.py',
    'python-programming/examples/linters/redef.py',
    'python-programming/examples/linters/importer.py',
])


def flake(path):
    if path in skip_flake:
        return 0
    proc = subprocess.Popen(['flake8', path],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    out, err = proc.communicate()
    if proc.returncode != 0:
        print(path)
        print(proc.returncode)
        print(out)
        print(err)
    return proc.returncode


def main():
    start = time.time()
    root = os.path.join('python-programming', 'examples')
    cnt = 0
    errors = 0
    for dirname, dirs, files in os.walk(root):
        for filename in files:
            if not filename.endswith(".py"):
                continue
            path = os.path.join(dirname, filename)
            #if path in skip:
            #    continue
            #cnt +=1
            #print(path)
            errors += flake(path)
            #print(cnt)

            ## TODO: python -m py_compile script.py
            ## and then move all the code inside a main function
            ## and use __name__ == '__main__' to hide it?
            #proc = subprocess.Popen([sys.executable, path],
            #    stdout = subprocess.PIPE,
            #    stderr = subprocess.PIPE,
            #)
            #out, err = proc.communicate()
            #assert proc.returncode == 0, "for {}".format(path)
    end = time.time()
    print(f"Elapsed time: {end-start}")
    exit(errors)

def test_flake8():
    os.walk
#    assert proc.returncode == 1  # I guess because there were issues
#    assert err  == b'' #.decode('utf-8') == ''
#    errors = out.decode('utf-8').split("\n")
#    print("\n")
#    assert len(errors) <= 10, "Errors grew!"
#    print(len(out))

def xtest_combine(tmpdir):
    proc = subprocess.Popen([sys.executable, 'combine.py', '--all', '--target', str(tmpdir)],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    out, err = proc.communicate()
    print(out)
    print(err)
    assert proc.returncode == 0


main()
