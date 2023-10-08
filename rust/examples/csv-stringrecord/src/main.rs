use std::fs::File;


fn main() {
    let filepath = "planets.csv";
    let rows = read_file(filepath);
    for row in &rows {
        println!("{:?}", row);
        println!("{}", &row[0]);
    }
    println!("------");
    for value in &rows[0] {
        println!("{}", value);
    }
    println!("------");

    println!("{}", &rows[3][0]);

}

fn read_file(filepath: &str) -> Vec<csv::StringRecord> {
    let mut rows:Vec<csv::StringRecord> = vec![];
    match File::open(filepath) {
        Ok(file) => {
            let mut rdr = csv::Reader::from_reader(file);
            for result in rdr.records() {
                match result {
                    Ok(row) => {
                        rows.push(row.clone());
                    },
                    Err(err) => panic!("Error {}", err)
                };
            }
        },
        Err(error) => panic!("Error opening file {}: {}", filepath, error),
    }

    rows
}
