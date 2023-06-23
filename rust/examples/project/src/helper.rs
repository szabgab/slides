pub fn public_in_helper() {
    println!("public_in_helper");
    private_in_helper();
}

fn private_in_helper() {
    println!("in_helper");
}
