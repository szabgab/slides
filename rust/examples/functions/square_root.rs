use std::io;

fn main() {
    let number:f32 = 4.0;
    let r = number.sqrt();
    dbg!(r);
    match square_root(4.0) {
        Ok(res) => {
            dbg!(res)
        },
        Err(_) => {
            println!("Error");
        }
    }
    //square_root(-1.0));
}

fn square_root(number: f64) -> io::Result<()> {
    if number < 0.0 {
        return Err("Negative");
    }
    Ok(number.sqrt())
}
