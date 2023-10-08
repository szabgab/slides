fn main() {
    println!("main");
    root();
    colors::blue();
    // colors::blue_helper(); // error[E0603]: function `blue_helper` is private
    colors::dark::blue();

    use colors::dark;
    dark::green();
}

fn root() {
    println!("root");
}

mod colors {
    pub fn blue() {
        println!("blue");
        blue_helper(); // can be called from here
    }

    fn red() {
        println!("red");
    }


    fn blue_helper() {
        println!("blue_helper");
        crate::root();
        super::root();
    }

    pub mod dark {
        pub fn blue() {
            println!("dark_blue");
            crate::root();        // absolute path
            super::super::root(); // relative path, probably not very good idea
            super::red();
        }
        pub fn green() {
            println!("dark_green");
        }
    }

}

