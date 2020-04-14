package main

import (
	"flag"
	"fmt"
	"os"

	"github.com/gocolly/colly"
)

func main() {
	var baseURL string
	flag.StringVar(&baseURL, "url", "", "URL where we startr")
	flag.Parse()

	urls := []string{}

	if baseURL == "" {
		fmt.Println("--url reuired")
		os.Exit(1)
	}
	fmt.Println(baseURL)

	c := colly.NewCollector()
	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL)
	})
	// c.OnHTML("#content", func(h *colly.HTMLElement) {
	// 	fmt.Println(h)
	// 	//t := h.ChildAttr("a", "href")
	// 	//c.Visit(t)
	// })
	//c.OnHTML(".ytd-playlist-video-renderer", func(h *colly.HTMLElement) {
	c.OnHTML("a", func(h *colly.HTMLElement) {
		//fmt.Println(h)
		fmt.Println(h.Attr("href"))
		//match, _ := regexp.MatchString(`list=`, h.Attr("href"))
		//fmt.Println(match)
		//t := h.ChildAttr("a", "href")
		//c.Visit(t)
	})
	c.Visit(baseURL)
	c.Wait()
	fmt.Prinln(urls)
}
