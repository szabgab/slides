package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	fmt.Println(is_anagram("ab", "ba"))
	fmt.Println(is_anagram("hello", "hello"))
	fmt.Println(is_anagram("hell", "ello"))
}

func is_anagram(a, b string) bool {
	aa := strings.Split(a, "")
	sort.Strings(aa)
	aaa := strings.Join(aa, "")

	bb := strings.Split(b, "")
	sort.Strings(bb)
	bbb := strings.Join(bb, "")

	return aaa == bbb
}
