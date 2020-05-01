package main

import (
	"fmt"
	"log"
	"net/http"
)

func mainPage(w http.ResponseWriter, r *http.Request) {
	text := r.FormValue("text")
	html := `<h1>Echo</h1><form><input type name="text"><input type="submit" value="Echo"></form>`

	if text != "" {
		html += fmt.Sprintf("You said: %v", text)
	}
	fmt.Fprintf(w, html)
}

func main() {
	http.HandleFunc("/", mainPage)
	fmt.Println("Going to listen on http://localhost:5000  Ctr-c to stop the server.")
	log.Fatal(http.ListenAndServe("127.0.0.1:5000", nil))
}
