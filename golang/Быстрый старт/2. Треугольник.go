package main

import (
    "fmt"
    "log"
)

func main() {
	var arr = make([]uint, 3)
	for i := 0; i < len(arr); i++ {
		_, err := fmt.Scan(&arr[i])
		if err != nil {
			log.Fatal(err)
		}
	}

	a := arr[0]
	b := arr[1]
	c := arr[2]

	if a < b+c && b < c+a && c < a+b {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}