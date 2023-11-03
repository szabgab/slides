use tempdir::TempDir;
use std::fs::File;
use std::io::Write;
use std::path::Path;


fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 2 {
        println!("Usage: {} NUMBER_OF_FILES", args[0]);
        std::process::exit(1);
    }
    let number_of_files = args[1].parse::<i32>().unwrap();

    single_thread(number_of_files);
    for threads in 2..=2 {
        multiple_thread(number_of_files, threads);
    }


}

fn multiple_thread(number_of_files: i32, threads: i32) {
    let temp_dir = TempDir::new("demo").unwrap();
    println!("temp_dir: {:?}", temp_dir);
    let temp_dir_path = temp_dir.into_path();


    let start = std::time::Instant::now();

    let mut handles = vec![];
    for _ in 1..=threads {
        let temp_dir_path = temp_dir_path.clone();
        let start = 1;
        let end = number_of_files;
        handles.push(std::thread::spawn(move || {
            println!("In thread {:?}", std::thread::current().id());
            create_files(start, end, &temp_dir_path);
        
        }));    
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Elapsed time: {:?}", start.elapsed());
    verify_number_of_created_file(&temp_dir_path, number_of_files);
}


fn single_thread(number_of_files: i32) {
    let temp_dir = TempDir::new("demo").unwrap();
    println!("temp_dir: {:?}", temp_dir);
    let temp_dir_path = temp_dir.into_path();

    let start_time = std::time::Instant::now();

    let start = 1;
    let end = number_of_files;
    create_files(start, end, &temp_dir_path);
    println!("Elapsed time: {:?}", start_time.elapsed());
    verify_number_of_created_file(&temp_dir_path, number_of_files);
    
}

fn verify_number_of_created_file(temp_dir: &Path, number_of_files: i32) {
    println!("Number of files: {}", number_of_files);
    let content = temp_dir.read_dir().unwrap().count() as i32;
    std::fs::remove_dir_all(temp_dir).unwrap();
    assert_eq!(number_of_files, content);
}

fn create_files(start: i32, end: i32, temp_dir: &Path) {
    for ix in start..=end {
        let file_path = temp_dir.join(format!("{}.txt", ix));
        //println!("{:?}", file_path);
        let mut file = File::create(file_path).unwrap();
        writeln!(&mut file, "{}.txt", ix).unwrap();
    }
}