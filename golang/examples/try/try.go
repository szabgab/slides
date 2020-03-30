package main

import (
	"fmt"
	//	"runtime"
	//	"os"
)

func main() {

	//	greet()
	//fmt.Println("Hello World")
	//fmt.Println(os.Executable)

	// filename := os.Args[1]
	// //fmt.Println(filename)
	// var fh *os.File
	// fh, err = os.Open(filename)
	// //fmt.Printf("%T", fh)
	// if err != nil {
	// 	fmt.Printf("Error opening file '%v'\n%v\n", filename, err)
	// 	os.Exit(1)
	// }
	// reader := bufio.NewReader(fh)
	// var line string
	// for true {
	// 	line, err = reader.ReadString('\n')
	// err will be EOF on the last line of the file which is not an error, but it is also not nil
	// 	if err != nil {
	// 		fmt.Printf("Error reading line: %v", err)
	// 		os.Exit(1)
	// 	}
	// 	fmt.Print(line)
	// 	if line == "" {
	// 		break
	// 	}
	// }

}

func greet() {
	fmt.Println("Hello World")
}
