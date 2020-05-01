package main

import (
	"fmt"
	"log"
	"net/http"
)

func mainPage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World")
}

func main() {
	http.HandleFunc("/", mainPage)
	fmt.Println("Going to listen on http://localhost:5000  Ctr-c to stop the server.")
	log.Fatal(http.ListenAndServe(":5000", nil))
}
