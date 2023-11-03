# Date and Time
{id: datetime}


## Measure elapsed time
{id: measure-elapsed-time}
{i: Instant}
{i: now}
{i: elapsed}
{i: std::time::Instant::now}
{i: as_secs}
{i: as_millis}

* [std::time](https://doc.rust-lang.org/std/time/index.html)
* The [Instant](https://doc.rust-lang.org/std/time/struct.Instant.html) type allows us to get snapshots if time that can help us measure elapesd time.

* In this example we have a function to decide if a number is a prime number. We only use it to have some code that can take substantial time.
* We get the timestamp before and after and we calculate the elapsed time.

![](examples/datetime/instant-elapsed/src/main.rs)
![](examples/datetime/instant-elapsed/out.out)


## Duration
{id: duration}
{i: Duration}
{i: std::time::Duration}

* We can use the Duration type to represent a span of time.

* [std::time::Duration](https://doc.rust-lang.org/std/time/struct.Duration.html)

![](examples/datetime/duration/src/main.rs)
![](examples/datetime/duration/out.out)

## Instant sleep Duration
{id: instant-sleep-duration}
{i: Instant}

![](examples/datetime/sleep-duration/src/main.rs)
![](examples/datetime/sleep-duration/out.out)


## Handle time (using the time crate)
{id: handle-time}
{i: time}
{i: Date}
{i: from_calendar_date}

* [std::time](https://doc.rust-lang.org/std/time/index.html)
* [time](https://docs.rs/time/latest/time/)

![](examples/datetime/time-demo/Cargo.toml)
![](examples/datetime/time-demo/src/main.rs)


