import sys
import os
import subprocess

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

def test_run():
    root = 'python/examples'
    cnt = 0
    for dirname, dirs, files in os.walk(root):
        for filename in files:
            if not filename.endswith(".py"):
                continue

            path = os.path.join(dirname, filename)
            if path in skip:
                continue
            cnt +=1
            print(path)
            print(cnt)

            # TODO: python -m py_compile script.py
            # and then move all the code inside a main function
            # and use __name__ == '__main__' to hide it?
            proc = subprocess.Popen([sys.executable, path],
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
            )
            out, err = proc.communicate()
            assert proc.returncode == 0, "for {}".format(path)
