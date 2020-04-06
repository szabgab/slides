package main

import (
	"fmt"
	"testing"
)

func TestDoors(t *testing.T) {
	cases := make(map[int][]bool)
	cases[0] = []bool{}
	cases[1] = []bool{true}
	cases[2] = []bool{true, false}
	cases[3] = []bool{true, false, false}
	cases[4] = []bool{true, false, false, true}
	cases[5] = []bool{true, false, false, true, false}
	cases[6] = []bool{true, false, false, true, false, false}
	cases[7] = []bool{true, false, false, true, false, false, false}
	cases[8] = []bool{true, false, false, true, false, false, false, false}
	cases[9] = []bool{true, false, false, true, false, false, false, false, true}
	cases[10] = []bool{true, false, false, true, false, false, false, false, true, false}
	for i, expected := range cases {
		actual := doors(i)
		if !compare(actual, expected) {
			t.Error(fmt.Sprintf("Expected '%v', Actual '%v'", expected, actual))
		}
	}
}

func compare(a, b []bool) bool {
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
