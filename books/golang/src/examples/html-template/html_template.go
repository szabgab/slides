package main

import (
	"html/template"
	"os"
)

func main() {
	tmpl, err := template.New("test").Parse("Hello World!\n")
	if err != nil {
		panic(err)
	}
	err = tmpl.Execute(os.Stdout, nil)
	if err != nil {
		panic(err)
	}

	person := map[string]string{
		"Name": "Joe",
	}
	tmpl, err = template.New("test").Parse("Hello {{.Name}}\n")
	if err != nil {
		panic(err)
	}
	err = tmpl.Execute(os.Stdout, person)
	if err != nil {
		panic(err)
	}

	other := Person{Name: "Jane"}
	err = tmpl.Execute(os.Stdout, other)
	if err != nil {
		panic(err)
	}
}

type Person struct {
	Name string
}
