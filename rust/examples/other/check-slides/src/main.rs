use std::fs::File;
use std::io::{BufRead, BufReader};
use std::iter::FromIterator;
use std::path::Path;
use std::path::PathBuf;
use std::process::exit;
use std::process::Command;

// use regex::Regex;

// from all the md files extract the list of included files
// from the examples/ directory list all the files
// make sure each file is included and is only included once

// Run every rs file, if there is an out file compare the results.
//
const ROOT: &str = "../../..";

fn main() {
    let verbose = false;
    std::env::set_current_dir(ROOT).unwrap();
    let md_files = get_md_files();
    let imported_files = get_imported_files(md_files);
    let examples = get_all_the_examples();

    let mut count = 0;
    for filename in examples {
        if !imported_files.contains(&filename) {
            println!("ERROR Unused file: `{}`", filename);
            count += 1;
        }
    }

    println!("\nget_crates");
    let crates = get_crates(Path::new("examples"));

    println!("\ncheck_crates");
    let root_folder = std::env::current_dir().unwrap();
    let mut clippy_error = 0;
    let number_of_crates = crates.len();
    for (ix, crate_folder) in crates.iter().enumerate() {
        if verbose {
            println!("crate: {}/{}, {:?}", ix, number_of_crates, crate_folder);
        }
        let folder = crate_folder.clone().into_os_string().into_string().unwrap();
        if folder == "examples/intro/formatting-required" {
            continue;
        }
        if folder == "examples/intro/print" {
            continue;
        }
        if folder == "examples/functions/declare-twice" {
            continue;
        }

        std::env::set_current_dir(crate_folder).unwrap();
        //let result = Command::new("cargo")
        //    .arg("fmt")
        //    .arg("--check")
        //    .output()
        //    .expect("failed to execute process");
        //println!("{}", std::str::from_utf8(&result.stdout).unwrap());
        //println!("{}", std::str::from_utf8(&result.stderr).unwrap());
        //println!("{}", result.status);

        let result = Command::new("cargo")
            .arg("clippy")
            .arg("--")
            .arg("--deny")
            .arg("warnings")
            .output()
            .expect("failed to execute process");
        if !result.status.success() {
            //println!("{}", result.status);
            println!("ERROR in crate: {:?}", crate_folder);
            clippy_error += 1;
            //println!("{}", std::str::from_utf8(&result.stdout).unwrap());
            //println!("{}", std::str::from_utf8(&result.stderr).unwrap());
            //std::process::exit(1);
        }
        std::env::set_current_dir(&root_folder).unwrap();
    }
    println!("checked all the crates");

    if clippy_error > 0 {
        eprintln!("There are {clippy_error} examples with clippy errors.");
        exit(1);
    }

    if count > 0 {
        eprintln!("There are {count} unused examples");
        exit(1);
    }
}

fn get_crates(path: &Path) -> Vec<PathBuf> {
    let mut crates: Vec<PathBuf> = vec![];
    for entry in path.read_dir().expect("read_dir call failed").flatten() {
        if entry.path().ends_with("target") {
            continue;
        }
        //println!("{:?}", entry);
        if entry.path().ends_with("Cargo.toml") {
            //println!("cargo: {:?}", entry.path().parent());
            crates.push(entry.path().parent().unwrap().to_path_buf());
        }
        if entry.path().is_dir() {
            crates.extend(get_crates(entry.path().as_path()));
        }
    }
    crates
}

// TODO: go deeper than 2 levels to also handle examples/*/src/main.rs
// TODO: but exclude examples/*/target/
fn get_all_the_examples() -> Vec<String> {
    println!("\nget_all_the_examples");

    let exclude: Vec<String> = [
        "examples/image/create-image/image.png",
        "examples/other/multi_counter_with_manual_csv/counter.csv",
    ]
    .iter()
    .map(|path| path.to_string())
    .collect();
    let pathes = get_examples(Path::new("examples"));
    let pathes: Vec<String> = pathes
        .iter()
        .filter(|path| !exclude.contains(path))
        .cloned()
        .collect();
    pathes
}

fn get_examples(path: &Path) -> Vec<String> {
    let mut examples: Vec<String> = vec![];
    for entry in path.read_dir().expect("read_dir call failed").flatten() {
        if entry.path().ends_with("Cargo.lock") {
            continue;
        }
        if entry.path().ends_with("Cargo.toml") {
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
    examples
    //return Vec::from_iter( examples.iter().map(|s| s.clone().into_os_string().into_string().expect("Bad") ) );
}

fn get_imported_files(md_files: Vec<PathBuf>) -> Vec<String> {
    println!("\nget_imported_files");
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
                    if line.starts_with("![](") && line.ends_with(')') {
                        //println!("{}", &line[4..line.len()-1])
                        imported_files.push((line[4..line.len() - 1]).to_string());
                    }
                }
            }
            Err(error) => {
                println!("Error opening file {:?}: {}", filename, error);
            }
        }
    }
    return Vec::from_iter(imported_files.iter().map(|s| s.to_string()));
}

fn get_md_files() -> Vec<PathBuf> {
    println!("\nget_md_files");
    let mut md_files = vec![];
    let path = Path::new(".");
    for entry in path.read_dir().expect("read_dir call failed").flatten() {
        let filename = entry.path();
        //println!("{:?}", filename); //.as_path());
        let extension = filename.extension();
        if let Some(value) = extension {
            if value == "md" {
                // println!("{:?}", filename);
                //println!("{}", filename);
                md_files.push(filename);
            }
        }
        //println!("{:?}", extension.unwrap())
    }
    md_files
}
