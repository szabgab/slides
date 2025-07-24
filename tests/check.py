import sys
import os
import subprocess
import time
import tempfile

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
    'python-programming/examples/twisted/web_client.py',
    'python-programming/examples/flask/simple_auth/test_app.py',
])

def _run(cmd):
    proc = subprocess.Popen(cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    out, err = proc.communicate()
    return proc.returncode, out, err

def flake(path):
    #print(path)
    if path in skip_flake:
        return 0
    exit_code, out, err = _run(['flake8', path])

    if exit_code != 0:
        print(path)
        print(exit_code)
        print(out)
        print(err)
    return exit_code


def check_python(root):
    python_root = os.path.join(root, 'python-programming', 'examples')
    cnt = 0
    errors = 0
    for dirname, dirs, files in os.walk(python_root):
        for filename in files:
            if not filename.endswith(".py"):
                continue
            path = os.path.join(dirname, filename)
            #print(path)
            #if path in skip:
            #    continue
            #cnt +=1
            #print(path)
            errors += flake(path[len(root)+1:])
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
    return errors


def generate_book():
    tmpdir = tempfile.mkdtemp()
    try:
        exit_code, out, err = _run([sys.executable, 'combine.py', '--all', '--target', tmpdir])
    except Exception as error:
        print("Exception while generating book")
        print(error)
        return 1
    if exit_code != 0:
        print("Error generating book:")
        print(out)
        print(err)
        return 1

def check_index(root):
    errors = 0
    for dirname in os.listdir(root):
        dirpath = os.path.join(root, dirname)
        if not os.path.isdir(dirpath):
            continue
        for filename in os.listdir( dirpath ):
            if not filename.endswith(".md"):
                continue
            filepath = os.path.join(dirpath, filename)
            #print(filepath)
            with open(filepath) as fh:
                for line in fh:
                    if line.startswith("{id: index}"):
                        print(f"We have an index in {filepath}")
                        errors += 1
    return errors


def main():
    start = time.time()
    root = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
    errors = 0
    errors += check_python(root)
    errors += check_index(root)
    #errors += generate_book()
    end = time.time()
    print(f"Elapsed time: {end-start}")
    exit(errors)


main()
