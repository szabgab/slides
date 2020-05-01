package main

import (
	"os"
	"text/template"
)

func main() {
	tmpl, err := template.ParseFiles("main.txt")
	if err != nil {
		panic(err)
	}

	person := personType{
		Name:  "Jane",
		Email: "jena@code-maven.com",
	}
	err = tmpl.Execute(os.Stdout, person)
	if err != nil {
		panic(err)
	}
}

type personType struct {
	Name  string
	Email string
}
