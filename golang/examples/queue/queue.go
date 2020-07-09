package main

import (
	"container/list"
	"fmt"
)

func main() {
	queue := list.New()

	queue.PushBack("Joe")
	queue.PushBack("Jane")
	queue.PushBack("Mary")
	queue.PushBack("Joe")

	for {
		if queue.Len() == 0 {
			break
		}
		item := queue.Front()
		fmt.Println(item.Value)
		queue.Remove(item)
	}
}
