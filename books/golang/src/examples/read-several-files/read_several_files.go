package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func div(a, b int) (res int, err error) {
	defer func() {
		myerr := recover()
		if myerr != nil {
			// fmt.Printf("%T %v\n", myerr, myerr)
			err = fmt.Errorf("bad")
		}
	}()

	res = a / b
	return
}

func main() {
	files := os.Args[1:]
	if len(files) == 0 {
		fmt.Println("We need at least one file")
		os.Exit(1)
	}
	for _, filename := range files {
		dat, err := ioutil.ReadFile(filename)
		if err != nil {
			fmt.Printf("Could not open file '%v' because: %v\n", filename, err)
			continue
		}

		text := strings.TrimSuffix(string(dat), "\n")
		parts := strings.Split(text, ",")
		a, err := strconv.Atoi(parts[0])
		if err != nil {
			fmt.Printf("Could not convert '%v' to integer: %v", parts[0], err)
			continue
		}
		b, err := strconv.Atoi(parts[1])
		if err != nil {
			fmt.Printf("Could not convert '%v' to integer: %v", parts[1], err)
			continue
		}

		c, err := div(a, b)
		if err != nil {
			fmt.Printf("Could not divide %v / %v Error: %v", a, b, err)
		}
		fmt.Println(c)
	}
}
