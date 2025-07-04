# Other
{id: other}

## Mocking get in LWP::Simple
{id: mocking-get-in-lwp-simple}


![](examples/mock-lwp/t/webapi_mock_lwp_simple.t)

## Read CSV file as array of hashes
{id: read-csv-file-as-array-of-hashes}
{i: csv}

{aside}
The csv function that can be imported from Text::CSV can read a CSV into memory, creating an array of hashes.

Element from the first row will be used as the keys of these hashes and elements from all the other rows will be used as
the values of these hashes.
{/aside}

* [Text::CSV](https://metacpan.org/pod/Text::CSV)

![](examples/other/planets.csv)
![](examples/other/read_csv_as_array_of_hashes.pl)
![](examples/other/read_csv_as_array_of_hashes.out)

## Sort array using sort and sort_by
{id: sort-array-using-sort-and-sort-by}

* [List::UtilsBy](https://metacpan.org/pod/List::UtilsBy)

![](examples/other/sort_by.pl)
![](examples/other/sort_by_complexity.pl)
![](examples/other/sort_by_planets.pl)

## Range iterator
{id: range-iterator}

* [Range::Iter](https://metacpan.org/pod/Range::Iter)

![](examples/other/range.pl)


## Benchmark
{id: benchmark}

* [Benchmark](https://metacpan.org/pod/Benchmark)

![](examples/other/benchmark.pl)

## Bubble sort
{id: bubble-sort}

* [Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort)

![](examples/other/bubble_sort.pl)

## Insert sort
{id: insert-sort}

* [Insert sort](https://en.wikipedia.org/wiki/Insertion_sort)

![](examples/other/insert_sort.pl)


## Merge sort
{id: merge-sort}

* [Merge sort](https://en.wikipedia.org/wiki/Merge_sort)

![](examples/other/merge_sort.pl)

* It can run out of the recursion limit of Perl

## Quicksort
{id: quick-sort}

* [Quciksort](https://en.wikipedia.org/wiki/Quicksort)

![](examples/other/quick_sort.pl)

* The worst-case is if we happen to select the smallest element every time, then the complexity is O(n^2)
* It can run out of the recursion limit of Perl

## Timsort
{id: tim-sort}

* [Timsort](https://en.wikipedia.org/wiki/Timsort)
* Created for Python by Tim Peters

## Traverse directory tree
{id: traverse-directory-tree}

![](examples/other/dirwalk.pl)

## Traverse directory tree with call back
{id: traverse-directory-tree-with-call-back}

![](examples/other/dirwalk_calback.pl)

## Linear search in unorderd array
{id: linear-search-in-unordered-array}

![](examples/other/linear_search.pl)

## Binary search in sorted array
{id: binary-search-in-sorted-array}

![](examples/other/binary_search.pl)

## Convert curl command with -F to LWP::UserAgent
{id: convert-curl-f-to-lwp-useragent}

```
curl -X POST -F field=value -F name=Corion "https://httpbin.org/post" -H  "accept: application/json"
```
![](examples/other/send_f.pl)

## Modify time anomality in two files
{id: modify-time-anomality}

![](examples/other/modify_time_is_the_same.pl)

![](examples/other/modify_time_is_the_same_1.pl)


