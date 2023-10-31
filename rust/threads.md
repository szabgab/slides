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

![](examples/threads/try-threads/src/main.rs)
![](examples/threads/try-threads/out.out)

## Threads with messages
{id: threads-with-messages}

![](examples/threads/threads-messages/src/main.rs)

## Two threads sending messages
{id: threads-sending-two-messages}

![](examples/threads/threads-messages-multiple-sources/src/main.rs)


## Testing speed improvements with threads
{id: threads-speed-improvements}

![](examples/threads/threads-messages-multiple-sources/threads-load-test/src/main.rs)

