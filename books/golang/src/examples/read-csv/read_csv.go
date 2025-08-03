package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Printf("Usage: %s FILENAME\n", os.Args[0])
		os.Exit(1)
	}
	var filename = os.Args[1]
	//fmt.Println(filename)
	fh, err := os.Open(filename)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	reader := bufio.NewReader(fh)
	r := csv.NewReader(reader)
	r.Comma = ';'

	records, err := r.ReadAll()
	if err != nil {
		log.Fatal(err)
	}

	//fmt.Printf("%T\n", records)
	var sum = 0
	for _, row := range records {
		val, err := strconv.Atoi(row[2])
		if err != nil {
			fmt.Printf("Error %v converting to int: '%v'", err, row[2])
			continue
		}
		sum += val
	}
	fmt.Println(sum)
}
