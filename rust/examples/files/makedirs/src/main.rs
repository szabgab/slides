use std::fs;

fn main() {
    match makedirs() {
        Ok(res) => {
            dbg!(res);
        },
        Err(_) => {
            dbg!("error");
        },
    }
}

fn makedirs() -> std::io::Result<()> {
    fs::create_dir_all("parent/sub")?;
    Ok(())
}
