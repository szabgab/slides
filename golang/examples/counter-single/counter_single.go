package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var filename = "counter.txt"
	var cnt = 0
	var fhin, err1 = os.Open(filename)
	if err1 == nil {
		reader := bufio.NewReader(fhin)
		var line, _ = reader.ReadString('\n')
		cnt, _ = strconv.Atoi(line)
	}

	cnt++
	fmt.Println(cnt)

	var fhout, err2 = os.Create(filename)
	if err2 == nil {
		fhout.WriteString(fmt.Sprintf("%d", cnt))
		fhout.Close()
	}
}
