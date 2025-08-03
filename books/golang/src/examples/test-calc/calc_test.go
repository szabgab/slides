package main

import "testing"

func TestCalc(t *testing.T) {
	result, err := calc(2, "+", 3)

	if err != nil {
		t.Errorf("Error found where not expected %v", err)
	}
	if result != 5 {
		t.Errorf("Expected 5 received %v", result)
	}
}
