package main

import (
	"fmt"
	"strconv"
	"testing"
)

func TestRegular(t *testing.T) {
	for _, n := range [...]int{1, 2, 4} {
		expected := strconv.Itoa(n)
		actual := fb(n)
		if actual != expected {
			t.Error(fmt.Sprintf("Expected '%v', Actual '%v'", expected, actual))
		}

	}
}

func TestFizz(t *testing.T) {
	expected := "Fizz"
	for _, n := range [...]int{3, 6, 9, 12, 18} {
		actual := fb(n)
		if actual != expected {
			t.Error(fmt.Sprintf("Expected '%v', Actual '%v'", expected, actual))
		}

	}
}

func TestBuzz(t *testing.T) {
	expected := "Buzz"
	for _, n := range [...]int{5, 10, 20, 25} {
		actual := fb(n)
		if actual != expected {
			t.Error(fmt.Sprintf("Expected '%v', Actual '%v'", expected, actual))
		}

	}
}

func TestFizzBuzz(t *testing.T) {
	expected := "FizzBuzz"
	for _, n := range [...]int{15, 30, 60} {
		actual := fb(n)
		if actual != expected {
			t.Error(fmt.Sprintf("Expected '%v', Actual '%v'", expected, actual))
		}

	}
}
