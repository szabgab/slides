package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
)

func main() {

}

func parseIni(filename string) (map[string]map[string]string, error) {
	ini := make(map[string]map[string]string)
	var head string

	fh, err := os.Open(filename)
	if err != nil {
		return ini, fmt.Errorf("Could not open file '%v': %v", filename, err)
	}
	sectionHead := regexp.MustCompile(`^\[([^]]*)\]\s*$`)
	keyValue := regexp.MustCompile(`^(\w*)\s*=\s*(.*?)\s*$`)
	reader := bufio.NewReader(fh)
	for {
		line, _ := reader.ReadString('\n')
		//fmt.Print(line)
		result := sectionHead.FindStringSubmatch(line)
		if len(result) > 0 {
			head = result[1]
			//fmt.Printf("found: %s\n", head)
			ini[head] = make(map[string]string)
			continue
		}

		result = keyValue.FindStringSubmatch(line)
		if len(result) > 0 {
			key, value := result[1], result[2]
			//fmt.Printf("kv: '%q'\n", result)
			ini[head][key] = value
			continue
		}

		if line == "" {
			break
		}
	}

	//ini["foo"] = "bar"

	return ini, nil
}
