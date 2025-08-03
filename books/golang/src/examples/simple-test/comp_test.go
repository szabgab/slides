package main

import "testing"

func TestAdd(t *testing.T) {
	t.Log("Hello from the test")
	total := add(2, 2)
	if total != 4 {
		t.Error("Sum was incorrect")
	}
}
