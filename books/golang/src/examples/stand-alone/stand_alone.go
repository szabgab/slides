package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"os/exec"
	"runtime"
	"strconv"
	"time"
)

func mainPage(w http.ResponseWriter, r *http.Request) {
	aStr := r.PostFormValue("a")
	bStr := r.PostFormValue("b")
	a, _ := strconv.Atoi(aStr)
	b, _ := strconv.Atoi(bStr)

	result := a + b

	html := fmt.Sprintf(`<h1>Calculator</h1>
	<form method="POST">
	<input name="a">
	<input name="b">
	<input type="submit" value="Add">
	</form>
	Result: %v
	<hr>
	<a href="/exit">exit</a>`, result)

	fmt.Fprintf(w, "%v", html)
}

func exitApp(w http.ResponseWriter, r *http.Request) {
	go func() {
		time.Sleep(1000)
		os.Exit(0)
	}()
	fmt.Fprintf(w, "goodbye")
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

// TODO: Find usable port, but open the browser only to that
// TODO: is there a better way to stop the application than just exit?

func main() {
	http.HandleFunc("/", mainPage)
	http.HandleFunc("/exit", exitApp)

	port := 5000
	connection := fmt.Sprintf("127.0.0.1:%v", port)
	url := fmt.Sprintf("http://%v", connection)
	fmt.Printf("Going to listen on %v  Ctr-c to stop the server.\n", url)
	// TODO: only open once we know the server was started.
	go func() {
		time.Sleep(1000)
		openBrowser(url)
	}()
	err := http.ListenAndServe(connection, nil)
	if err != nil {
		//log.Fatal(err)
		panic(err)
	}
	fmt.Println("OK")
}
