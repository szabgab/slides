package main

import (
   "fmt"
   "bufio"
   "os"
)

func main() {
   reader := bufio.NewReader(os.Stdin)
   fmt.Print("Enter Your name: ")
   name, err := reader.ReadString('\n')
   if err != nil {
       fmt.Println(err)
   } else {
       fmt.Println("Hello", name)
   }
}

