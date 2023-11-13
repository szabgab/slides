use sysinfo::{System, SystemExt};

fn main() {
    let sys = System::new_all();

    println!("System name:             {}", sys.name().unwrap());
    println!("System kernel version:   {}", sys.kernel_version().unwrap());
    println!("System OS version:       {}", sys.os_version().unwrap());
    println!("System host name:        {}", sys.host_name().unwrap());
    println!();

    println!("NB CPUs:                 {}", sys.cpus().len());
    println!();

    println!("total memory: {} bytes", sys.total_memory());
    println!("used memory : {} bytes", sys.used_memory());
    println!("total swap  : {} bytes", sys.total_swap());
    println!("used swap   : {} bytes", sys.used_swap());

}
