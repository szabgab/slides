package main

import "testing"

func TestStats(t *testing.T) {
	numbers := []int{2, 3, 5, -1, 1, 8}
	min, max, total, average := stats(numbers)
	if min != -1 {
		t.Errorf("min is expected to be -1 actual: %v", min)
	}
	if max != 8 {
		t.Errorf("max is expected to be 8 actual: %v", max)
	}
	if total != 18 {
		t.Errorf("total is expected to be 18 actual: %v", total)
	}
	if average != 3 {
		t.Errorf("average is expected to be 3 actual: %v", average)
	}
}

