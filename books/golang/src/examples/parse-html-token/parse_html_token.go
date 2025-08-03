package main

import (
	"fmt"
	"io"
	"log"
	"strings"

	"golang.org/x/net/html"
)

func main() {
	body := `<html>
	<body>
		<h1>Main title</h1>
		<a href="https://code-maven.com/">Code Maven</a>
	</body>
	</html>`

	reader := strings.NewReader(body)
	tokenizer := html.NewTokenizer(reader)
	for {
		tt := tokenizer.Next()
		if tt == html.ErrorToken {
			if tokenizer.Err() == io.EOF {
				return
			}
			log.Printf("Error: %v", tokenizer.Err())
			return
		}
		fmt.Printf("Token: %v\n", tokenizer.Token())
	}
}
