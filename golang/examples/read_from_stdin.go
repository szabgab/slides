package main

import (
   "fmt"
   "bufio"
   "os"
)

func main() {
   reader := bufio.NewReader(os.Stdin)
   fmt.Print("Enter Your name: ")
   name, _ := reader.ReadString('\n')
   fmt.Println("Hello", name)
}

