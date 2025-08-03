package main

import (
	"os"
	"text/template"
)

func main() {
	tmpl, err := template.New("test").Parse("Hello {{.Name}}\n")
	if err != nil {
		panic(err)
	}

	person := personType{Name: "Jane"}
	err = tmpl.Execute(os.Stdout, person)
	if err != nil {
		panic(err)
	}
}

type personType struct {
	Name string
}
