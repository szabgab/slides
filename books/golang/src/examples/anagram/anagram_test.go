package main

import "testing"

func TestAnagram(t *testing.T) {
	res := is_anagram("abc", "abd")
	if res != false {
		t.Errorf("No anagram")
	}

	res = is_anagram("abc", "acb")
	if res != true {
		t.Errorf("Is anagram")
	}
}
