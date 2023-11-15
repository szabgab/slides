use syn::{Expr, Result};

fn main() {
    match run() {
        Ok(_val) => println!("ok"),
        Err(err) => println!("err: {}", err),
    }

    cases();
}


fn run() -> Result<()> {
    let code = "..";
    let expr = syn::parse_str::<Expr>(code)?;
    let res = match expr {
        syn::Expr::Range(_expr) => true, // _expr is the same expression that cannot be printed.
        _ => false,
    };
    println!("{}", res);
    Ok(())
}

fn cases() {
    let expr = syn::parse_str::<Expr>("..").unwrap();
    assert!(match expr { syn::Expr::Range(_expr) => true, _ => false, });
}
