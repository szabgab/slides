use fork::{fork, Fork};

fn main() {
    println!("Before {}", std::process::id());

    match fork() {
        Ok(Fork::Parent(child)) => {
            println!("In parent process {}, new child has pid: {}", std::process::id(), child);
        }
        Ok(Fork::Child) => {
            println!("In child process {}", std::process::id());
            std::process::exit(0);
        },
        Err(_) => println!("Fork failed"),
    }
    println!("Launched {}", std::process::id());

    println!("After  {}", std::process::id());

}
