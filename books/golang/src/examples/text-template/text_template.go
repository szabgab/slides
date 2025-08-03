package main

import (
	"os"
	"text/template"
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
}
