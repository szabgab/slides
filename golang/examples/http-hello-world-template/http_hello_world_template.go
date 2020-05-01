package main

import (
	"html/template"
	"log"
	"net/http"
)

func mainPage(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles("main.html")
	if err != nil {
		panic(err)
	}
	p := pageType{Title: "Joe and Jane"} //, Body: []byte{}}
	//p := make(map[string]string)
	t.Execute(w, p)
}

func main() {
	http.HandleFunc("/", mainPage)
	log.Fatal(http.ListenAndServe(":5000", nil))
}

type pageType struct {
	Title string
	//	Body  []byte
}

// Visit: http://localhost:5000/
