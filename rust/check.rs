use std::path::Path;
use std::path::PathBuf;
use std::process::exit;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::iter::FromIterator;

// use regex::Regex;

// from all the md files extract the list of included files
// from the examples/ directory list all the files
// make sure each file is included and is only included once

// Run every rs file, if there is an out file compare the results.

fn main() {
    //get_md_files()
    let md_files = get_md_files();
    // println!("{:?}", md_files);
    let imported_files = get_imported_files(md_files);
    // println!("{:?}", imported_files);
    let examples = get_examples();
    //println!("{:?}", examples);
    let mut count = 0;
    for filename in examples {
        if ! imported_files.contains(&filename) {
            println!("Unused file: `{}`", filename);
            count += 1;
        }
    }
    println!("There are {count} unused examples");
    if count > 0 {
        exit(1);
    }
}

// TODO: go deeper than 2 levels to also handle examples/*/src/main.rs
// TODO: but exclude examples/*/target/
fn get_examples() -> Vec<String> {
    let exclude = vec![
        "examples/try-packages/Cargo.toml",
        ];
    let mut examples = vec![];
    let path = Path::new("examples");
    for entry in path.read_dir().expect("read_dir call failed") {
        if let Ok(entry) = entry {
            let dirname = entry.path();
            if dirname.is_dir() {
                //println!("dir");
                for filepath in dirname.read_dir().expect("read_dir call failed") {
                    if let Ok(filepath) = filepath {
                        //println!("{:?}", filepath);
                        if filepath.path().is_dir() {
                            continue;
                        }
                        if filepath.path().ends_with("Cargo.lock") {
                            continue;
                        }
                        if exclude.contains(&filepath.path().into_os_string().into_string().expect("Bad").as_str()) {
                            // println!("exclude {:?}", filepath.path());
                            continue;
                        }
                        let filename = filepath.path();
                        examples.push(filename);
                    }
                }
            } else {
                println!("'ERROR: {:?}' is not a directory", dirname);
                exit(1);
            }
        }
    }
    return Vec::from_iter( examples.iter().map(|s| s.clone().into_os_string().into_string().expect("Bad") ) );
}

fn get_imported_files(md_files: Vec<PathBuf>) -> Vec<String> {
    // println!("{:?}", md_files);
    // ![](examples/arrays/update_hash.rs)
    // let re = Regex::new(r"^!\[\]]\((.*)\)\s*$").unwrap();
    let mut imported_files = vec![];
    for filename in md_files {
        //println!("{:?}", filename);
        match File::open(filename.as_path()) {
            Ok(file) => {
                let reader = BufReader::new(file);
                for line in reader.lines() {
                    let line = line.unwrap();
                    if line.starts_with("![](") && line.ends_with(")") {
                        //println!("{}", &line[4..line.len()-1])
                        imported_files.push((&line[4..line.len()-1]).to_string());
                    }
                }
            },
            Err(error) => {
                println!("Error opening file {:?}: {}", filename, error);
            },
        }
    }
    return Vec::from_iter( imported_files.iter().map(|s| s.to_string()) );
}

fn get_md_files() -> Vec<PathBuf> {
    let mut md_files = vec![];
    let path = Path::new(".");
    for entry in path.read_dir().expect("read_dir call failed") {
        if let Ok(entry) = entry {
            let filename = entry.path();
            // println!("{:?}", filename); //.as_path());
            let extension = filename.extension();
            if extension != None {
                if extension.unwrap() == "md" {
                    // println!("{:?}", filename);
                    //println!("{}", filename);
                    md_files.push(filename);
                }
                //println!("{:?}", extension.unwrap())
            }
        }
    }
    return md_files
}
