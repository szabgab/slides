use svg::Document;
use svg::node::element::Line;

fn main() {
    let document = Document::new().set("viewBox", (0, 0, 70, 70)).add(
        Line::new()
            .set("x1", 10)
            .set("y1", 10)
            .set("x2", 10)
            .set("y2", 60)
            .set("stroke", "black")
            .set("stroke-width", 3),
    );

    svg::save("line.svg", &document).unwrap();
}
