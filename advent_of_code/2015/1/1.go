package main

import (
	"flag"
	"fmt"
    "io/ioutil"
)

func check_basement(seen_basement *bool, floor int, i int) {
	if !*seen_basement && floor == -1 {
		fmt.Printf("Santa entered the basement at character %d\n", i+1)
		*seen_basement = true
	}
}

func main() {
	fptr := flag.String("fpath", "1_input.txt", "file path")
	flag.Parse()
	fmt.Println("value of fpath is:", *fptr)
	data, err := ioutil.ReadFile(*fptr)
	if err != nil {
		fmt.Println("File reading error", err)
		return
	}

	var nframes int = 0

	for _, char := range string(data) {
		if char == '(' || char == ')' {
			nframes += 1
		}
	}

	fmt.Printf("nframes: %d", nframes)

	const (
		whiteIndex = 0
		blackIndex = 1
		size       = 100
		delay      = 8
	)


	var floor int = 0
	var seen_basement bool = false

	for i, char := range string(data) {
		if char == '(' {
			floor += 1
			check_basement(&seen_basement, floor, i)
		} else if char == ')' {
			floor -= 1
			check_basement(&seen_basement, floor, i)
		}

	}
}
