package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Printf("Usage: %s FILENAME\n", os.Args[0])
		os.Exit(1)
	}

	urls := readFile(os.Args[1])

	for _, url := range urls[0:3] {
		text, err := get(url)
		if err != nil {
			fmt.Println(err)
			return
		}
		fmt.Printf("%-40s %6v\n", url, len(text))
	}
}

func readFile(filename string) []string {
	urls := make([]string, 0, 50)

	log.Println(filename)
	fh, err := os.Open(filename)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	scanner := bufio.NewScanner(fh)
	for scanner.Scan() {
		line := scanner.Text()
		urls = append(urls, line)
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading:", err)
		os.Exit(1)
	}
	return urls
}

func get(url string) (string, error) {
	text := ""
	resp, err := http.Get(url)
	if err != nil {
		return text, err
	}

	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return text, err
	}

	return string(body), nil
}
