# Iterators
{id: iterators}

## Iterate over vector of numbers
{id: iterate-over-vector-of-numbers}

![](examples/iterators/iterator_over_vector_of_numbers.rs)
![](examples/iterators/iterator_over_vector_of_numbers.out)


## Alternatively, we could create an iterator using the iter method.
{id: use-the-iter-method}
{i: iter}

![](examples/iterators/iterator_over_vector_of_numbers_using_iter.rs)
![](examples/iterators/iterator_over_vector_of_numbers_using_iter.out)


## Create a simple iterator to count up to a number
{id: create-simple-iterator-to-count}
{i: Iterator}
{i: Item}
{i: next}


![](examples/iterators/iterator_limited_counter.rs)
![](examples/iterators/iterator_limited_counter.out)

## Create a simple iterator to count boundless
{id: create-simple-iterator-to-count-boundless}
{i: break}

![](examples/iterators/iterator_unlimited_counter.rs)
![](examples/iterators/iterator_unlimited_counter.out)


## Iterate over files in current directory
{id: iterate-over-files-in-current-directory}
{i: read_dir}

![](examples/iterators/list_dir.rs)

## Iterate over files in current directory calling next
{id: iterate-over-files-in-current-directory-calling-next}
{i: read_dir}
{i: next}

![](examples/iterators/list_dir_manually.rs)

## Iterator to walk directory tree
{id: walk-directory-tree}

![](examples/iterators/walk_directory_tree_retur_strings.rs)

