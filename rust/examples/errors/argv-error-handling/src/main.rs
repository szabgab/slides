use std::env;
use std::process::exit;
use std::cmp::Ordering;

fn main() {
    run();

}



// We are expecting the user to provide a command line argument.
// How do we handle if the user does not provide it (or provides too many)?


// In the get_name function call exit if the user did not supply the required parameter
// fn run() {
//     let name = get_name();
//     println!("{}", name);
// }

// fn get_name() -> String {
//     let args: Vec<String> = env::args().collect();
//     if args.len() != 2 {
//         eprintln!("Usage: {} NAME", args[0]);
//         exit(1);
//     }
//     args[1].clone()
// }


// Return the empty string
// This makes the caller need to handle the cases, but more problematic is that in the called
// we can't tell if there were to many or too few (or otherwise incorrect) parameters
// fn run() {
//     let name = get_name();
//     if name == "" {
//         println!("Got empty string")
//     } else {
//         println!("{}", name);
//     }
// }
// fn get_name() -> String {
//     let args: Vec<String> = env::args().collect();
//     if args.len() == 2 { args[1].clone() } else { "".to_string() }
// }


// Return either the Ok() with the value provided by the user or Err with the specific error message
// The caller needs to use match to sepearat the two cases.
// fn run() {
//     let res = get_name();
//     //println!("{:?}", res);
//     match res {
//         Err(error_message) => println!("{error_message}"),
//         Ok(name) => println!("{name}"),
//     }
// }


fn run() {
    let res = get_name();
    //println!("{:?}", res);
    let name = match res {
        Err(error_message) => {
            eprintln!("{error_message}");
            exit(1);
        },
        Ok(name) => name,
    };
    println!("{name}");
}

fn get_name() -> Result<String, String> {
    let args: Vec<String> = env::args().collect();
    match args.len().cmp(&2_usize) {
        Ordering::Less => Err("Not enough parameters".to_string()),
        Ordering::Greater => Err("Too many parameters".to_string()),
        Ordering::Equal => Ok(args[1].clone()),
    }
}
