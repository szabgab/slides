package main

import (
	"fmt"
	"regexp"

	"github.com/gocolly/colly"
)

func main() {
	listID := "PLQVvvaa0QuDeF3hP0wQoSxpkqgRcgxMqX"
	playlistURL := "https://www.youtube.com/watch?list=" + listID

	// log.Print(playlistURL)
	// resp, err := http.Get(playlistURL)
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// log.Print(resp)

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
		//fmt.Println(h.Attr("href"))
		match, _ := regexp.MatchString(`list=`, h.Attr("href"))
		fmt.Println(match)
		//t := h.ChildAttr("a", "href")
		//c.Visit(t)
	})
	c.Visit(playlistURL)
}
