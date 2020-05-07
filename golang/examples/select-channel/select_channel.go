package main

import (
	"fmt"
	"time"
)

func main() {
	ch1 := make(chan string)
	ch2 := make(chan string)

	go count("one", 500, ch1)
	go count("two", 2000, ch2)

	var text string
	// for {
	// 	text = <-ch1
	// 	fmt.Println(text)
	// 	text = <-ch2
	// 	fmt.Println(text)
	// }

	for {
		select {
		case text = <-ch1:
			fmt.Println(text)
		case text = <-ch2:
			fmt.Println(text)
		}
	}

}

func count(name string, ms int, out chan<- string) {
	i := 0
	for {
		i++
		out <- fmt.Sprintf("%v %v", name, i)
		time.Sleep(time.Duration(1000000 * ms))
	}
}
