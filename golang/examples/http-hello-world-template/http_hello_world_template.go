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
	//p := &Page{Title: "", Body: []byte{}}
	//p := make(map[string]string)
	t.Execute(w, nil)
}

func main() {
	http.HandleFunc("/", mainPage)
	log.Fatal(http.ListenAndServe(":5000", nil))
}

// type Page struct {
// 	Title string
// 	Body  []byte
// }

// Visit: http://localhost:5000/
