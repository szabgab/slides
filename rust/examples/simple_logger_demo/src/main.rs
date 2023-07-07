use simple_logger::SimpleLogger;

fn main() {
    SimpleLogger::new().init().unwrap();

    log::info!("This is a sample info.");
    log::warn!("This is a sample warn.");
}

