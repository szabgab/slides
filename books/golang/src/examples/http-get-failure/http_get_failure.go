package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	url := "http://invalid.code-maven.com"
	fmt.Println(url)

	resp, err := http.Get(url)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(string(body))
}
