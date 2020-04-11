package main

import (
	"fmt"
	"log"
	"net/url"
)

func main() {
	myURL := "https://code-maven.com/page/action?name=foo&age=42&name=bar"
	fmt.Println(myURL)
	parsedURL, err := url.Parse(myURL)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(parsedURL.Path)
	fmt.Println(parsedURL.RequestURI())
	fmt.Println(parsedURL.Hostname())
	fmt.Println(parsedURL.Host)

	fmt.Println()
	query := parsedURL.Query()
	fmt.Println(query)

	fmt.Println()
	for k, vals := range query {
		fmt.Printf("%v: ", k)
		for _, v := range vals {
			fmt.Printf("'%v' ", v)
		}
		fmt.Println()
	}
	//fmt.Println(parsedURL.String())
}
