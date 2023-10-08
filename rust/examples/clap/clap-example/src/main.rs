use clap::Parser;

#[derive(Parser, Debug)]
#[command(version)]
struct Cli {
    #[arg(long, default_value = "127.0.0.1")]
    host: String,

    #[arg(long, default_value = "5000")]
    port: String,

    #[arg(long, default_value = "")]
    indexfile: String,

    #[arg(long, default_value = ".")]
    path: std::path::PathBuf,

    #[arg(long, default_value_t = 0, help = "A number mapped to i32")]
    limit: i32,

    #[arg(long, default_value_t = 0, help = "A number mapped to u8")]
    small: u8,

    #[arg(long, short, default_value_t = false, help = "Turn on debug mode")]
    debug: bool,
}

fn main() {
    let args = Cli::parse();
    dbg!(&args.host);
    dbg!(&args);
    if args.debug {
        println!("In debug mode");
    }
}
