#!/usr/bin/env python
import svgwrite


width = 440
height = 260
# the location of the (0, 0) point
zero_x = 20
zero_y = 20
coord_width = 2

steps = 5
month = 65 #year/steps
year  = 360
hi = int((height - zero_y) / (steps + 1))
swidth = 5


def many_releases(dwg, width, height):
    line = svgwrite.shapes.Polyline( fill='white', stroke='black', stroke_width=swidth )
    line.points.append( (zero_x,       height - zero_y - 4) )
    for n in range(1, steps):
        line.points.append( (zero_x + n*month,   height - zero_y - 4 -n*hi +hi) )
        line.points.append( (zero_x + n*month,   height - zero_y - 4 -n*hi) )
    line.points.append( (year,            height - zero_y - 4 - steps*hi+hi) )
    line.points.append( (year,            zero_y) )
    line.points.append( (year+month, zero_y) )

    zz = 2
    box = svgwrite.shapes.Polygon( fill=svgwrite.rgb(66, 244, 86) )
    for n in range(1, steps):
        box.points.append( ( zero_x + n*month + zz, height - zero_y - 4 -n*hi +hi + zz) )
        box.points.append( ( zero_x + n*month + zz, height - zero_y - 4 -n*hi + zz) )
    box.points.append( ( year + zz,    height - zero_y - 4-steps*hi+hi + zz) )
    box.points.append( ( year + zz,    height - zero_y - 4-steps*hi - 16 + zz) )
    box.points.append( ( year+month , height - zero_y - 4-steps*hi - 16 + zz) )
    box.points.append( ( year+month , height - zero_y - 4 + zz) )
    dwg.add( line )
    dwg.add( box )


def one_release(dwg, width, height):
    line = svgwrite.shapes.Polyline( fill='white', stroke='black', stroke_width=swidth )
    line.points.append( (zero_x,     height - zero_y - 4) )
    line.points.append( (year,       height - zero_y - 4) )
    line.points.append( (year,       zero_y) )
    line.points.append( (year+month, zero_y) )

    box = svgwrite.shapes.Rect( insert=(width-78, 22), size=(63, height-44), fill=svgwrite.rgb(66, 244, 86))
    dwg.add( line )
    dwg.add( box )


def coordinates(width, height) :
    x_coord = svgwrite.shapes.Line(
        start  = (0,     height - zero_y),
        end    = (width, height - zero_x),
        fill   = 'white',
        stroke ='black',
        stroke_width = coord_width,
    )
    x_arrow = svgwrite.shapes.Polyline( fill='white', stroke='black', stroke_width=coord_width )
    x_arrow.points.append( (width-10, height-10) )
    x_arrow.points.append( (width, height-20) )
    x_arrow.points.append( (width-10, height-30) )

    x_text = svgwrite.text.Text("time", insert=(width-50, height-8))


    y_coord = svgwrite.shapes.Line(
        start  = (zero_x, height),
        end    = (zero_x, zero_y),
        fill   = 'white',
        stroke ='black',
        stroke_width=2,
    )
    y_arrow = svgwrite.shapes.Polyline( fill='white', stroke='black', stroke_width=2 )
    y_arrow.points.append( (10, 30) )
    y_arrow.points.append( (20, 20) )
    y_arrow.points.append( (30, 30) )

    y_text = svgwrite.text.Text("value", insert=(17, 70), transform="translate(0) rotate(-90, 17, 70)")

    dwg = svgwrite.Drawing(size=(width, height))
    dwg.add( x_coord )
    dwg.add( x_arrow )
    dwg.add( x_text )

    dwg.add( y_coord )
    dwg.add( y_arrow )
    dwg.add( y_text )

    return dwg


if __name__ == '__main__':
    dwg = coordinates(width, height)
    one_release(dwg, width, height)

    with open("value/time_value.svg", "w") as fh:
        fh.write(dwg.tostring())

    dwg = coordinates(width, height)
    many_releases(dwg, width, height)

    with open("value/time_value_many_releases.svg", "w") as fh:
        fh.write(dwg.tostring())


