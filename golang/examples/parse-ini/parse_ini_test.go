package main

import (
	"fmt"
	"testing"
)

func TestParseIni(t *testing.T) {
	actual, err := parseIni("data.ini")
	if err != nil {
		t.Error(fmt.Sprintf("Error in parsing: '%v'", err))
	}
	expected := make(map[string]map[string]string)
	expected["first section"] = make(map[string]string)
	expected["first section"]["a"] = "23"
	expected["first section"]["b"] = "12"
	expected["second section"] = make(map[string]string)
	expected["second section"]["a"] = "42"
	if !compareMapMap(actual, expected) {
		t.Error(fmt.Sprintf("Expected '%v', Actual '%v'", expected, actual))
	}
}

func compareMapMap(a, b map[string]map[string]string) bool {
	//fmt.Println(a)
	//fmt.Println(b)
	if len(a) != len(b) {
		return false
	}
	for key, value := range a {
		if !compareMap(value, b[key]) {
			return false
		}
	}
	for key, value := range b {
		if !compareMap(value, a[key]) {
			return false
		}
	}
	return true
}

func compareMap(a, b map[string]string) bool {
	//fmt.Println(a)
	//fmt.Println(b)
	if len(a) != len(b) {
		return false
	}
	for key, value := range a {
		if value != b[key] {
			return false
		}
	}
	for key, value := range b {
		if value != a[key] {
			return false
		}
	}
	return true
}
