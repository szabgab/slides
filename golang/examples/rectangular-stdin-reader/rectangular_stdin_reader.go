package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Width: ")
	width, _ := reader.ReadString('\n')
	width = strings.TrimSuffix(width, "\n")

	fmt.Print("Height: ")
	height, _ := reader.ReadString('\n')
	height = strings.TrimSuffix(height, "\n")

	// convert to integer
	w, _ := strconv.Atoi(width) // this will convert a string like "abc" or "2x" to 0 and set err
	h, _ := strconv.Atoi(height)
	fmt.Println(w)
	fmt.Println(h)

	fmt.Println("The size of the rectangular is: ", w*h)
}
