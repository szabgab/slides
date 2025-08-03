package main

import (
	"fmt"
	"log"
	"net/http"
)

func mainPage(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.Method)
	text := r.PostFormValue("text")
	html := `<h1>Echo</h1><form method="POST"><input type name="text"><input type="submit" value="Echo"></form>`

	if text != "" {
		html += fmt.Sprintf("You said: %v", text)
	}
	fmt.Fprintf(w, html)
}

func main() {
	http.HandleFunc("/", mainPage)
	host := "127.0.0.1"
	port := 5000
	fmt.Printf("Going to listen on http://%v:%v  Ctr-c to stop the server.\n", host, port)
	err := http.ListenAndServe(fmt.Sprintf("%v:%v", host, port), nil)
	if err != nil {
		log.Fatal(err)
	}
}
