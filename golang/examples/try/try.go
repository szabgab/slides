package main

import (
	"fmt"
)

func main() {
	if true {
		fmt.Println("Before")
		defer fmt.Println("Middle")
		fmt.Println("After")	
	}

	fmt.Println("Outside")

	// var dir string
	// dir, _ = os.Getwd()
	// fmt.Printf("Before  %v\n", dir)
	// cd("..", showDir)
	// dir, _ = os.Getwd()
	// fmt.Printf("After %v\n", dir)
}

// func showDir() {
// 	fmt.Println("Hello")
// 	dir, _ := os.Getwd()
// 	fmt.Printf("Inside:  %v\n", dir)
// }

// func cd(path string, f func()) {
// 	//fmt.Println(path)
// 	cwd, err := os.Getwd()
// 	if err != nil {
// 		log.Panic(err)
// 	}
// 	defer os.Chdir(cwd)
// 	err = os.Chdir(path)
// 	f()
// }


// package main

// import (
// 	"fmt"
// 	"path/filepath"
// 	//	"runtime"
// 	//	"os"
// )

// // Defer change directory
// // Defer remove temporary directory

// func main() {
// 	path := filepath.Join("main", "sub", "other")
// 	fmt.Println(path)
// 	strings.HasSuffix("foobar", "bar")
// 	// _, file, _, _ := runtime.Caller(0)
// 	// fmt.Println(file)

// 	//	greet()
// 	//fmt.Println("Hello World")
// 	//fmt.Println(os.Executable)

// 	// filename := os.Args[1]
// 	// //fmt.Println(filename)
// 	// var fh *os.File
// 	// fh, err = os.Open(filename)
// 	// //fmt.Printf("%T", fh)
// 	// if err != nil {
// 	// 	fmt.Printf("Error opening file '%v'\n%v\n", filename, err)
// 	// 	os.Exit(1)
// 	// }
// 	// reader := bufio.NewReader(fh)
// 	// var line string
// 	// for true {
// 	// 	line, err = reader.ReadString('\n')
// 	// err will be EOF on the last line of the file which is not an error, but it is also not nil
// 	// 	if err != nil {
// 	// 		fmt.Printf("Error reading line: %v", err)
// 	// 		os.Exit(1)
// 	// 	}
// 	// 	fmt.Print(line)
// 	// 	if line == "" {
// 	// 		break
// 	// 	}
// 	// }

// }

// func greet() {
// 	fmt.Println("Hello World")
// }
