use std::fs;

fn main() {
    match makedir() {
        Ok(res) => {
            dbg!(res);
        },
        Err(_) => {
            dbg!("error");
        },
    }
}

fn makedir() -> std::io::Result<()> {
    fs::create_dir_all("hello")?;
    Ok(())
}
