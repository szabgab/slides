# Basic Types

* string
* int
* uint
* float
* bool
* byte
* real
* complex
* imag


This is just a list of the basic types in Go. You only need to remember that there are different types. For now you can use the defaults offered by Golang. Later, when you get deeper in the language these types allow you to improve the speed and the memory usage of your application by specifying the size of each variable.



The numbers indicate the number of bits each variable takes. In languages such Python and Perl you would not need to care about this at all, but you would not have control over these aspects either. (In the Numpy library of Python you do have these distinctions.)



As I wrote, don't worry about them for now.


* [basic types](https://tour.golang.org/basics/11)

```
string          (any utf-8 character)

uint            (unsigned integer of 32 or 64 bits - depends on implementation)
uint8           (unsigned integer (0, 255)
uint16          (unsigned integer)
uint32          (unsigned integer)
uint64          (unsigned integer)


int             (signed integer, the same bit-size as uint)
int8            (signed integer (-128, 127))
int16
int32
int64

float32
float64

bool

byte             (alias for uint8)
rune             (alias for int32)

complex64       1 + 2i    or just 3i
complex128
```



