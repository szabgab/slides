package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"runtime"
)

func main() {
	baseURL := "https://code-maven.com/"
	if len(os.Args) == 2 {
		baseURL = os.Args[1]
	}
	openBrowser(baseURL)
}
func openBrowser(targetURL string) {
	var err error

	switch runtime.GOOS {
	case "linux":
		err = exec.Command("xdg-open", targetURL).Start()
		// TODO: "Windows Subsytem for Linux" is also recognized as "linux", but then we need
		// err = exec.Command("rundll32.exe", "url.dll,FileProtocolHandler", targetURL).Start()
	case "windows":
		err = exec.Command("rundll32.exe", "url.dll,FileProtocolHandler", targetURL).Start()
	case "darwin":
		err = exec.Command("open", targetURL).Start()
	default:
		err = fmt.Errorf("unsupported platform %v", runtime.GOOS)
	}
	if err != nil {
		log.Fatal(err)
	}

}

// Based on: https://gist.github.com/hyg/9c4afcd91fe24316cbf0
