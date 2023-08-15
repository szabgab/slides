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

    #[arg(long)]
    nice: bool,

    #[arg(long, default_value = ".")]
    path: std::path::PathBuf,
}


fn main() {
    let args = Cli::parse();
    dbg!(&args.host);
    dbg!(&args);
}
