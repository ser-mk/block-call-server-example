package main

import (
	"fmt"
	"testing"
)

func ExampleMult() {
	r := MultMatrix(11)
	fmt.Println(r)
	// Output: -7700
}

func ExampleFastMult() {
	r := FastCMultMatrix(11)
	fmt.Println(r)
	// Output: -7700
}

func TestBoth(t *testing.T) {
	a := MultMatrix(11)
	b := FastCMultMatrix(11)
	println(a, b)
	if int(a) != int(b) {
		t.Error("no equal")
	}
}
