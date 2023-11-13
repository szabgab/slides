# Threads in Rust
{id: threads}

## Threads in Rust
{id: threads-in-rust}

* [Feerless concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html)
* [std::thread](https://doc.rust-lang.org/std/thread/)

## First example with threads
{id: threads-first-example}
{i: thread}
{i: spawn}
{i: sleep}
{i: join}
{i: current}

* `spawn` will create a new thread. We can use `thread::current().id()` to get the id of the current thread.
* `join` in the main thread will block till the other thread stops.
* We can see "main thread ended" is already printed before the "spwan thread ended", but then the main thread waits.

![](examples/threads/try-threads/src/main.rs)
![](examples/threads/try-threads/out.out)

## Threads with messages
{id: threads-with-messages}
{i: channel}
{i: send}
{i: recv}
{i: move}

* We can faciliate communication between the main thread and the spawned thread.
* In this example the spawned thread is sending a message to the main thread.
* The `move` keyword tells Rust that the variables declared before spawning that are also used in the spawned code need to be moved. (`tx` in this case)
* `recv` is blocking the main thread.

![](examples/threads/threads-messages/src/main.rs)
![](examples/threads/threads-messages/out.out)

## Two threads sending messages
{id: threads-sending-two-messages}
{i: clone}

* Sending messages from more than one spawned threads to the main thread.

![](examples/threads/threads-messages-multiple-sources/src/main.rs)
![](examples/threads/threads-messages-multiple-sources/out.out)


## Testing speed improvements with threads
{id: threads-speed-improvements}

![](examples/threads/threads-load-test/src/main.rs)


TODO: what if there are variables in the main function? Can we read them from the threads? Can we write them?
TODO: How to share workload? e.g. We would like to create 10,000 files with the sequnce number of the file being botht the content and the filename.
TODO: What if we have a vector of 10,000 values and we would like to save each one of them in a separate file?

## Save many files
{id: save-many-files}

* In this example we demonstrate the speed improvement of threading.
* The program will count the number of prime numbes up to a given number. This part is CPU intensive.
* Then it will create many small files. - This part is IO intensive.

![](examples/threads/save-many-files/src/main.rs)

* Compute primes up to 1 (that is, do almost nothing).  Create 100,000 files. This is mostly IO intensive.
* We can see a 35-40% speed imprvement going from no threads to 2 threads, but there is no more speed improvement.

![](examples/threads/save-many-files/100000_1.out)


* Compute primes up to 500 (CPU intensive).  Create 100,000 files. This has both CPU and IO part.
* We can see speed increase by each additional thread, but the improvement diminishes as we add more threads.

![](examples/threads/save-many-files/100000_500.out)


## Rust threads read-only access to shared variables
{id: read-only-access-to-shared-variables}

* See several solutions

## Pass reference of read-only vector to thread
{id: pass-reference-of-read-only-vector-to-thread}
{i: Arc}
{i: clone}

* [Arc](https://doc.rust-lang.org/std/sync/struct.Arc.html) allows us to have reference counting.
* Here the `clone` only copies the reference and not the whole data structure.

![](examples/threads/pass-reference-to-vector/src/main.rs)


## Pass reference of read-only vector to thread improved
{id: pass-reference-of-read-only-vector-to-thread-improved}
{i: Arc}
{i: clone}

* In this solution the external block was moved inside the spawn.

![](examples/threads/pass-vector/src/main.rs)

## Pass and return reference (return ownership)
{id: pass-and-return-reference}

* An alternate way to handle this situation is to return the vector.
* This way we pass the ownership back to the caller.

![](examples/threads/pass-and-return-reference/src/main.rs)


## Thread scope
{id: thread-scrope}

* using [thread::scope](https://doc.rust-lang.org/stable/std/thread/fn.scope.html) there is an even simpler solution.

![](examples/threads/thread-scope/src/main.rs)

## chdir in threads
{id: chdir-in-threads}

* The current working directory is a per process so separate threads cannot have different current working directories
* Use forks.


## map with threads
{id: map-with-threads}

TODO: This is experimental code that needs to be improved

![](examples/threads/map-thread/src/main.rs)

## map with threads with Mutex
{id: map-with-thread-mutex}
{i: Mutex}

![](examples/threads/map-thread-suggested/src/main.rs)

## Counter in a loop in the same process and thread
{id: counter-in-a-loop}


* This simple examples shows how we can change a variable from multiple threads
* This is the example without any threads:

![](examples/threads/counter-loop/src/main.rs)


## Counter with threads (shared variable?)
{id: counter-with-threads}
{i: Mutex}
{i: lock}

* Solution is using Mutex

![](examples/threads/counter-with-mutex/src/main.rs)

## Counter with message passing
{id: counter-with-message-passing}
{i: mpsc}
{i: channel}
{i: send}
{i: drop}

* Solution using messages

![](examples/threads/counter-with-messages/src/main.rs)


