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
    let _res = match expr {
        syn::Expr::Range(_expr) => true, // _expr is the same expression that cannot be printed.
        _ => false,
    };
    //println!("{}", res);

    Ok(())
}

fn cases() {
    assert!(matches!(syn::parse_str::<Expr>("..").unwrap(), syn::Expr::Range(_expr)));


    //let res = syn::parse_str::<Expr>("2 == 3").unwrap();
    //assert!(matches!(res, syn::Expr::Range(_expr)));

    //assert!(matches!(expr, syn::Expr::If(_expr)));
    println!("done");
}
