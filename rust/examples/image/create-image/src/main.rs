
fn main() {
    let width = 800;
    let height = 800;

    let mut imgbuf = image::ImageBuffer::new(width, height);

    // gradient based on the example in the sourcde code
    // for (x, y, pixel) in imgbuf.enumerate_pixels_mut() {
    //     let red = (0.3 * x as f32) as u8;
    //     let green = 0;
    //     let blue = (0.3 * y as f32) as u8;

    //     *pixel = image::Rgb([red, green, blue]);
    // }

    // horizontal red gradient
    // for (x, y, pixel) in imgbuf.enumerate_pixels_mut() {
    //     let red = (0.3 * x as f32) as u8;
    //     let green = 0;
    //     let blue = 0;
    //     *pixel = image::Rgb([red, green, blue]);
    // }

    // vertical red gradient
    // for (x, y, pixel) in imgbuf.enumerate_pixels_mut() {
    //     let red = (0.3 * y as f32) as u8;
    //     let green = 0;
    //     let blue = 0;
    //     *pixel = image::Rgb([red, green, blue]);
    // }

    // horizontal red line
    // for (x, y, pixel) in imgbuf.enumerate_pixels_mut() {
    //     let red = 255 as u8;
    //     let green = 0;
    //     let blue = 0;
    //     if y == 23 {
    //         *pixel = image::Rgb([red, green, blue]);
    //     }
    // }

    // draw a horizontal line
    // let red = 100 as u8;
    // let green = 100;
    // let blue = 0;
    // let y = 200;
    // for x in 0..width {
    //     // let pixel = imgbuf.get_pixel_mut(x, y);
    //     // *pixel = image::Rgb([red, green, blue]);
    //     *imgbuf.get_pixel_mut(x, y) = image::Rgb([red, green, blue]);
    // }

    // draw a vertical line
    let red = 100_u8;
    let green = 100;
    let blue = 0;
    let x = 200;
    for y in 0..height {
        // let pixel = imgbuf.get_pixel_mut(x, y);
        // *pixel = image::Rgb([red, green, blue]);
        *imgbuf.get_pixel_mut(x, y) = image::Rgb([red, green, blue]);
    }


    imgbuf.save("image.png").unwrap();
}
