#!/usr/bin/env python
import svgwrite


width = 440
height = 240


line = svgwrite.shapes.Polyline( fill='white', stroke='black', stroke_width=5 )
line.points.append( (20,       height-24) )
line.points.append( (width-80, height-24) )
line.points.append( (width-80, 20) )
line.points.append( (width-20, 20) )

box = svgwrite.shapes.Rect( insert=(width-75, 24), size=(55, height-48), fill=svgwrite.rgb(66, 244, 86))

x_coord = svgwrite.shapes.Line(
    start = (0, height-20),
    end   = (width, height-20),
    fill  = 'white',
    stroke='black',
    stroke_width=2,
)
x_arrow = svgwrite.shapes.Polyline( fill='white', stroke='black', stroke_width=2 )
x_arrow.points.append( (width-10, height-10) )
x_arrow.points.append( (width, height-20) )
x_arrow.points.append( (width-10, height-30) )

x_text = svgwrite.text.Text("time", insert=(width-50, height-8))


y_coord = svgwrite.shapes.Line(
    start = (20, height),
    end   = (20, 20),
    fill  = 'white',
    stroke='black',
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

dwg.add( line ) 
dwg.add( box )


with open("value/time_value.svg", "w") as fh:
    fh.write(dwg.tostring())

