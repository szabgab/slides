package main

import "fmt"

func main() {
	doSomething()

}

func doSomething() {
	dir := createTempDir()

	//defer removeTempDir(dir)

	if true {
		removeTempDir(dir)
		return
	}

	removeTempDir(dir)
}

func createTempDir() string {
	return "some/path"
}

func removeTempDir(dir string) {
	fmt.Printf("")
}
