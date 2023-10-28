use std::path::Path;
use std::fs::ReadDir;


//#[derive(Debug)]
//#[allow(dead_code)]
struct Walk {
    rds: Vec<ReadDir>,
}

impl Walk {
    fn new(root: &str) -> Result<Walk, Box<dyn std::error::Error>> {
        let path = Path::new(root);
        match path.read_dir() {
            Ok(rd) => {
                let w = Walk {
                    rds: vec![rd],
                };
                std::result::Result::Ok(w)
            },
            Err(err) => {
                println!("Could not open dir '{}': {}", root, err);
                Err(Box::new(err))
            },
        }
    }
}

impl Iterator for Walk {
    type Item = String;

    fn next(&mut self) -> Option<Self::Item> {
        if self.rds.is_empty() {
            //println!("empty rds");
            return None;
        }
        let count = self.rds.len();
        let entry = self.rds[count - 1].next();
        match entry {
            Some(result) => {
                match result {
                    Ok(dir_entry) => {
                        if dir_entry.path().is_dir() {
                            match dir_entry.path().read_dir() {
                                Ok(rd) => {
                                    self.rds.push(rd);
                                }
                                Err(err) => {
                                    println!("Could not open dir {}", err);
                                }
                            }
                        }
                        return Some(dir_entry.path().to_str().unwrap().to_string());
                    },
                    Err(_err) =>  {
                        None
                    },
                }
            },
            None => {
                self.rds.pop();
                self.next()
            }
        }
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage: {} PATH", args[0]);
        std::process::exit(1);
    }
    let path_from_user = &args[1];
    let tree = match Walk::new(path_from_user) {
        Ok(tree) => tree,
        Err(err) => {
            println!("Error: {}", err);
            std::process::exit(1);
        }
    };
    //println!("{:?}", &tree);
    for entry in tree {
        println!("{:?}", entry);
    }
}

