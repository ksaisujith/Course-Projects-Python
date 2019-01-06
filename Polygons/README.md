# Drawing polygons recursively using turtle
<br>
This  program  handles  the  general  case  of  drawing  polygons  of decreasing sides, recursively. <br>
When it is run on the command line it requires two arguments (in order):<br>

            1.#sides: The number of sides of the main polygon (an integer). This value is guaranteedto be between3 and 8, inclusively.<br>
            2.[fill|unfill|]: If the string fill is specified, the polygons will be  filled when drawn.Otherwise it is assumed the polygon will be unfilled and just a line drawing.

If the correct number of command line arguments is not supplied, a usage message is displayed and the program will exit:

      $ python3 polygons.py #_sides [fill|unfil]
      
When the program is run, the main polygon that is drawn is the number of sides supplied at run time. As the sides of the main polygon are drawn, recursion is used to draw smaller polygons of decreasing size until the shape is a triangle. When  the  programming   finishes,  the  total  length  of  all  the  sides  of  the  polygons  drawn is also displayed to standard output

Example run:<br><br>
![](http://oi68.tinypic.com/24gopp2.jpg)
