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
	host := "127.0.0.1"  // "0.0.0.0" to host externally as well "" defaults to it
	port := 5000
	fmt.Printf("Going to listen on http://%v:%v  Ctr-c to stop the server.\n", host, port)
	err := http.ListenAndServe(fmt.Sprintf("%v:%v", host, port), nil)
	if err != nil {
		log.Fatal(err)
	}
}
