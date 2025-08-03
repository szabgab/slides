package main

import (
	"testing"
)

// var expected map[string]

func TestWCa(t *testing.T) {
	files := []string{"one.txt"}
	rows, words, chars := wc(files)
	if rows != 2 {
		t.Errorf("Expected rows: 2, actual rows %v\n", rows)
	}
	if words != 5 {
		t.Errorf("Expected words: 5, actual words %v\n", words)
	}
	if chars != 24 {
		t.Errorf("Expected chars: 24, actual chars %v\n", chars)
	}
}

func TestWCb(t *testing.T) {
	files := []string{"two.txt"}
	rows, words, chars := wc(files)
	if rows != 3 {
		t.Errorf("Expected rows: 3, actual rows %v\n", rows)
	}
	if words != 11 {
		t.Errorf("Expected words: 11, actual words %v\n", words)
	}
	if chars != 100 {
		t.Errorf("Expected chars: 100, actual chars %v\n", chars)
	}
}
