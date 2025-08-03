package main

import (
	"fmt"
	"regexp"
)

func main() {
	cases := []string{
		"Some free text",
		"! just text after an excalmation point",
		"![title] title but no url",
		"![Code Maven](https://code-maven.com/)",
	}

	//var includeFile = regexp.MustCompile(`^!`)
	//var includeFile = regexp.MustCompile(`^!\[(.*?)\]`)
	var includeFile = regexp.MustCompile(`^!\[(.*?)\]\((.*)\)$`)

	for _, txt := range cases {
		//fmt.Println(txt)
		// fmt.Println(includeFile.MatchString(txt))
		// res := includeFile.Find([]byte(txt))
		// fmt.Printf("%q\n", res)
		subMatches := includeFile.FindStringSubmatch(txt)
		if len(subMatches) != 0 {
			fmt.Printf("%q\n", subMatches)
			fmt.Printf("%q\n", subMatches[1])
			fmt.Printf("%q\n", subMatches[2])
		}
		//fmt.Println()
	}
}
