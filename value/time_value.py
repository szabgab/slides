#!/usr/bin/env python
import svgwrite


width = 440
year  = width-80
height = 240
coord_width = 2

# the location of the (0, 0) point
zero_x = 20
zero_y = 20

def many_releases(dwg, width, height):
    line = svgwrite.shapes.Polyline( fill='white', stroke='black', stroke_width=5 )
    line.points.append( (20,       height-24) )
    steps = 5
    for n in range(1, steps):
        line.points.append( (20 + n*65,   height-24-n*40+40) )
        line.points.append( (20 + n*65,   height-24-n*40) )
    line.points.append( (year, height-24-steps*40+40) )
    line.points.append( (year, 20) )
    line.points.append( (year+60, 20) )

    zz = 2
    box = svgwrite.shapes.Polygon( fill=svgwrite.rgb(66, 244, 86) )
    for n in range(1, steps):
        box.points.append( ( 20 + n*65 + zz, height-24-n*40+40 + zz) )
        box.points.append( ( 20 + n*65 + zz, height-24-n*40 + zz) )
    box.points.append( ( year + zz,    height-24-steps*40+40 + zz) )
    box.points.append( ( year + zz,    height-24-steps*40 + zz + 4) )
    box.points.append( ( year+60 + zz, height-24-steps*40 + zz + 4) )
    box.points.append( ( year+60 + zz, height-24 + zz) )
    dwg.add( line )
    dwg.add( box )


def one_release(dwg, width, height):
    line = svgwrite.shapes.Polyline( fill='white', stroke='black', stroke_width=5 )
    line.points.append( (zero_x,  height-24) )
    line.points.append( (year,    height-24) )
    line.points.append( (year,    20) )
    line.points.append( (year+60, 20) )

    box = svgwrite.shapes.Rect( insert=(width-75, 24), size=(55, height-48), fill=svgwrite.rgb(66, 244, 86))
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
    x_arrow = svgwrite.shapes.Polyline( fill='white', stroke='black', stroke_width=2 )
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


