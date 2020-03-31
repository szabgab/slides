package main

import (
	"os"
	"text/template"
)

func main() {
	person := map[string]string{
		"Name": "Joe",
	}
	tmpl, err := template.New("test").Parse("Hello {{.Name}}\n")
	if err != nil {
		panic(err)
	}
	err = tmpl.Execute(os.Stdout, person)
	if err != nil {
		panic(err)
	}
}


