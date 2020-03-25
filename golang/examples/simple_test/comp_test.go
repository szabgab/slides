package main

import "testing"

func TestSum(t *testing.T) {
    t.Log("Hello from the test")
    total := add(19, 23)
    if total != 42 {
        t.Errorf("Sum was incorrect")
    }
}

