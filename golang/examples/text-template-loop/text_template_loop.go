package main

import (
	"os"
	"text/template"
)

func main() {
	tmpl, err := template.ParseFiles("loop.txt")
	if err != nil {
		panic(err)
	}

	person := personType{
		Name:     "Jane",
		Children: []string{"Alpha", "Beta", "Gamma"},
	}
	err = tmpl.Execute(os.Stdout, person)
	if err != nil {
		panic(err)
	}
}

type personType struct {
	Name     string
	Children []string
}
