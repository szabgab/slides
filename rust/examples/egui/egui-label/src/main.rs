use eframe::egui;

fn main() -> Result<(), eframe::Error> {
    let options = eframe::NativeOptions {
        viewport: egui::ViewportBuilder::default()
        .with_inner_size([320.0, 240.0]),
        ..Default::default()
    };

    eframe::run_simple_native("Rust Maven egui App", options, move |ctx, _frame| {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("Hello World");
            ui.label("A label");
        });
    })
}
