package main

import (
	"fmt"
	"log"
)

func main() {
	var number int
	_, err := fmt.Scan(&number)
	if err != nil {
		log.Fatal(err)
	}
	sum := 0
	for i := 0; i < number+1; i++ {
		sum += fibo(i)
	}
	fmt.Println(sum)
}

func fibo(n int) int {
	if n == 0 {
		return 0
	} else if n == 1 || n == 2 {
		return 1
	} else {
		return fibo(n-1) + fibo(n-2)
	}
}