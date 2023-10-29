use std::fs;

fn main() {
    match makedir() {
        Ok(res) => {
            dbg!(res);
        },
        Err(err) => {
            dbg!("error: {}", err);
        },
    }
}

fn makedir() -> std::io::Result<()> {
    //fs::create_dir("paren/sub")?;
    fs::create_dir("folder")?;
    Ok(())
}
