fn main() {
    let mut graph = get_graph();
    dbg!(&graph);
    move_graph(&mut graph);
    dbg!(&graph);
}

fn get_graph() -> Vec<Point> {
    vec![
        Point {x: 0, y: 0},
        Point {x: 10, y: 20},
        Point {x: 30, y: 40},
    ]

}

fn move_graph(graph: &mut Vec<Point>) {
    for point in graph {
        point.x += 100;
    }
}


#[derive(Debug)]
#[allow(dead_code)]
struct Point {
    x: i32,
    y: i32,
}

