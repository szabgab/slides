
fn main() {
    {
        let random_bool: bool = rand::random();
        println!("random_bool: {random_bool}");

        let random_i8: i8 = rand::random();
        println!("random_i8: {random_i8}");

        let random_f32: f32 = rand::random();
        println!("random_f32: {random_f32}");
    }

    {
        use rand::Rng;
        let random_number = rand::thread_rng().gen_range(1..=100);
        println!("random_number: {random_number}");
    }
}
