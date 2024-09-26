package main

import (
    "bufio"
    "os"
    "fmt"
    "math"
    "strconv"
    "strings"
)

func main() {
	myscanner := bufio.NewScanner(os.Stdin)
	myscanner.Scan()
	line := myscanner.Text()
	sli := strings.Fields(line)
	a, _ := strconv.ParseFloat(sli[0], 64)
	b, _ := strconv.ParseFloat(sli[1], 64)
	c, _ := strconv.ParseFloat(sli[2], 64)

	discr := math.Pow(b, 2) - 4*a*c
	if discr > 0 {
		x1 := (-b + math.Sqrt(discr)) / (2 * a)
		x2 := (-b - math.Sqrt(discr)) / (2 * a)
		fmt.Println("2")
		fmt.Println(fmt.Sprintf("%f %f", x2, x1))
	} else if discr == 0 {
		x := -b / (2 * a)
		fmt.Println("1")
		fmt.Println(fmt.Sprintf("%f", x))
	} else {
		fmt.Println("0")
	}

}
