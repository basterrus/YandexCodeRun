package main

import (
	"fmt"
	"log"
)

func main() {
	var arr = make([]int, 2)
	res := 0
	for i := 0; i < len(arr); i++ {
		_, err := fmt.Scan(&arr[i])
		if err != nil {
			log.Fatal(err)
		}
	}

	for _, v := range arr {
		res += v
	}
	fmt.Println(res)
}
