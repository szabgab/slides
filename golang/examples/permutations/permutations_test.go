package main

import (
	"fmt"
	"testing"
)

func TestPermutations(t *testing.T) {
	cases := make(map[string][]string)
	cases["a"] = []string{"a"}
	cases["ab"] = []string{"ab", "ba"}
	cases["abc"] = []string{"abc", "acb", "bac", "bca", "cab", "cba"}

	for inp, expected := range cases {
		actual := permutations(inp)
		if !compare(expected, actual) {
			t.Error(fmt.Sprintf("Expected '%v', Actual '%v'", expected, actual))
		}
	}
}

func compare(a, b []string) bool {
	//fmt.Println(a)
	//fmt.Println(b)
	if len(a) != len(b) {
		return false
	}
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}
