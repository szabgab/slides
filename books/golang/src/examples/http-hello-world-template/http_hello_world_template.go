package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
)

func mainPage(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles("main.html")
	if err != nil {
		panic(err)
	}
	p := pageType{Title: "Joe and Jane", Body: "Some long text"}
	t.Execute(w, p)
}

func main() {
	http.HandleFunc("/", mainPage)
	fmt.Println("Going to listen on http://localhost:5000  Ctr-c to stop the server.")
	log.Fatal(http.ListenAndServe("127.0.0.1:5000", nil))
}

type pageType struct {
	Title string
	Body  string
}
