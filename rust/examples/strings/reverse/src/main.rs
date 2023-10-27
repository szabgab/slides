fn main() {
    let reversed = reverse("Hello");
    println!("{}", reversed);

    println!("{}", reverse("Abc"));
    println!("{}", reverse("שלום"));
}

fn reverse(text: &str) -> String {
    let reversed: String = text.chars().rev().collect();
    reversed
}
