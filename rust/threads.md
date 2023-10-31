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


