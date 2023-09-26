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
    let examples = get_all_the_examples();
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
fn get_all_the_examples() -> Vec<String> {
    let exclude: Vec<String> = vec![
        "examples/try-packages/Cargo.toml",
        "examples/try-threads/Cargo.toml",
        "examples/threads-messages/Cargo.toml",
        "examples/threads-messages-multiple-sources/Cargo.toml",
        "examples/threads-messages-multiple-sources/threads-load-test/Cargo.toml",
        "examples/multi_counter_with_manual_csv/Cargo.toml",
        "examples/multi_counter_with_manual_csv/counter.csv",
        "examples/argv-error-handling/Cargo.toml",
        "examples/use-statements/Cargo.toml",
        "examples/liquid-if-else/Cargo.toml",
        "examples/liquid-elsif/Cargo.toml",
        "examples/liquid-hello-world-from-file/Cargo.toml",
        "examples/liquid-hello-world-variables/Cargo.toml",
        "examples/liquid-objects/Cargo.toml",
        "examples/liquid-for-loop/Cargo.toml",
        "examples/liquid-loop-and-if/Cargo.toml",
        "examples/liquid-filters-numbers/Cargo.toml",
    ].iter().map(|path| path.to_string()).collect();
    let pathes = get_examples(Path::new("examples"));
    let pathes: Vec<String> = pathes.iter().filter(|path| !exclude.contains(path)).cloned().collect();
    pathes
}


fn get_examples(path: &Path) -> Vec<String> {
    let mut examples: Vec<String> = vec![];
    for entry in path.read_dir().expect("read_dir call failed") {
        if let Ok(entry) = entry {
            if entry.path().ends_with("Cargo.lock") {
                continue;
            }

            if entry.path().is_dir() {
                if entry.path().ends_with("target") {
                    continue;
                }
                examples.extend(get_examples(entry.path().as_path()));
                continue;
            }
            //dbg!(&entry);

            if entry.path().is_file() {
                examples.push(entry.path().into_os_string().into_string().unwrap());
                continue;
            }
        }
    }
    examples
    //return Vec::from_iter( examples.iter().map(|s| s.clone().into_os_string().into_string().expect("Bad") ) );
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
