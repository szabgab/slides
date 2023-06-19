fn main() {
    let str1 = "Hello";
    let str2 = "World";
    let string1 = String::from("Apple");
    let string2 = String::from("Banana");

    {
        //let text = str1 + str2; // cannot add `&str` to `&str`
        let text = str1.to_string() + str2;
        println!("{}", text);
    }

//    {
//        //let text = string1 + string2; // mismatched types
//        let text = string1 + &string2;
//        println!("{}", text);
//    }

    {
        let text = string1 + str2;
        println!("{}", text);
    }

//    {
//        let text = str1 + string2;
//        println!("{}", text);
//    }

}
