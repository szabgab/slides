package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func main() {
	tempDir, err := ioutil.TempDir("", "demo")
	if err != nil {
		log.Fatal(err)
	}

	defer os.RemoveAll(tempDir)

	fmt.Println(tempDir)
}
