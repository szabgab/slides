use tempdir::TempDir;
use std::fs::File;
use std::io::Write;
use std::path::Path;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 3 {
        println!("Usage: {} NUMBER_OF_FILES PRIME_LIMIT", args[0]);
        std::process::exit(1);
    }
    let number_of_files = args[1].parse::<i32>().unwrap();
    let limit = args[2].parse::<u32>().unwrap();

    single_thread(number_of_files, limit);
    for threads in 2..=5 {
        multiple_thread(number_of_files, limit, threads);
    }
}

fn multiple_thread(number_of_files: i32, limit: u32, threads: i32) {
    let temp_dir = TempDir::new("demo").unwrap();
    //println!("temp_dir: {:?}", temp_dir);
    let temp_dir_path = temp_dir.into_path();


    let start = std::time::Instant::now();

    let mut handles = vec![];
    for part in 0..threads {
        let temp_dir_path = temp_dir_path.clone();
        let batch_size = number_of_files / threads;
        let start = part * batch_size + 1;
        let end = if part < threads-1 {
            (part + 1) * batch_size
        } else {
            number_of_files
        };
            
        handles.push(std::thread::spawn(move || {
            //println!("In thread {:?}", std::thread::current().id());
            create_files(start, end, limit, &temp_dir_path);
        
        }));    
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Elapsed time for {} threads: {:?}", threads, start.elapsed());
    verify_number_of_created_file(&temp_dir_path, number_of_files);
}


fn single_thread(number_of_files: i32, limit: u32) {
    let temp_dir = TempDir::new("demo").unwrap();
    //println!("temp_dir: {:?}", temp_dir);
    let temp_dir_path = temp_dir.into_path();

    let start_time = std::time::Instant::now();

    let start = 1;
    let end = number_of_files;
    create_files(start, end, limit, &temp_dir_path);
    println!("Elapsed time: {:?}", start_time.elapsed());
    verify_number_of_created_file(&temp_dir_path, number_of_files);
    
}

fn verify_number_of_created_file(temp_dir: &Path, number_of_files: i32) {
    //println!("Number of files: {}", number_of_files);
    let content = temp_dir.read_dir().unwrap().count() as i32;
    std::fs::remove_dir_all(temp_dir).unwrap();
    assert_eq!(number_of_files, content);
}

fn create_files(start: i32, end: i32, limit: u32, temp_dir: &Path) {
    for ix in start..=end {
        let file_path = temp_dir.join(format!("{}.txt", ix));
        //println!("{:?}", file_path);
        let mut file = File::create(file_path).unwrap();
        
        let primes = count_primes(limit);
        writeln!(&mut file, "{} {}.txt", primes, ix).unwrap();
    }
}


fn count_primes(limit: u32) -> u32 {
    let mut count = 0;
    for number in 2..=limit {
        if is_prime(number) {
            count += 1;
        }
    }
    count
}

fn is_prime(number: u32) -> bool {
    for div in 2..number {
        if number % div == 0 {
            return false;
        }
    }
    true
}
