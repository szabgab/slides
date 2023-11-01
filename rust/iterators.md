# Iterators
{id: iterators}

## Iterate over vector of numbers
{id: iterate-over-vector-of-numbers}
{i: vec!}
{i: for}

![](examples/iterators/iterator-over-vector-of-numbers/src/main.rs)
![](examples/iterators/iterator-over-vector-of-numbers/out.out)


## Alternatively, we could create an iterator using the iter method.
{id: use-the-iter-method}
{i: iter}

![](examples/iterators/iterator-over-vector-of-numbers-using-iter/src/main.rs)
![](examples/iterators/iterator-over-vector-of-numbers-using-iter/out.out)


## Create a simple iterator to count up to a number
{id: create-simple-iterator-to-count}
{i: Iterator}
{i: Item}
{i: next}


![](examples/iterators/iterator-limited-counter/src/main.rs)
![](examples/iterators/iterator-limited-counter/out.out)

## Create a simple iterator to count boundless
{id: create-simple-iterator-to-count-boundless}
{i: break}

![](examples/iterators/iterator-unlimited-counter/src/main.rs)
![](examples/iterators/iterator-unlimited-counter/out.out)


## Iterate over files in current directory
{id: iterate-over-files-in-current-directory}
{i: read_dir}

![](examples/iterators/list-dir/src/main.rs)

## Iterate over files in current directory calling next
{id: iterate-over-files-in-current-directory-calling-next}
{i: read_dir}
{i: next}

![](examples/iterators/list-dir-manually/src/main.rs)

## Iterator to walk directory tree
{id: walk-directory-tree}
{i: ReadDir}

![](examples/iterators/walk-directory-tree-return-strings/src/main.rs)

## Count number of elements of an iterator
{id: count-number-of-elements-of-an-iterator}
{i: count}

![](examples/iterators/count/src/main.rs)
![](examples/iterators/count/out.out)

