package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
	"strconv"
)

func main() {
	in_file := "input/day01"
	if len(os.Args) > 1 {
		in_file = os.Args[1]
	}

	in_b, err := ioutil.ReadFile(in_file)
	if err != nil {
		fmt.Println(err)
		return
	}
	in_s := string(in_b)
	in_s = strings.Trim(in_s, "\n ")
	in_ss := strings.Split(in_s, "\n")

	// Now that the file is read and split into a slice of strings,
	// we can actually start processing it.
	
	data := make([]int, len(in_ss))
	for i := range(in_ss) {
		n, _ := strconv.ParseInt(in_ss[i], 10, strconv.IntSize)
		data[i] = int(n)
	}
	// Now we have a slice of ints and can actually start looking for
	// an answer
	// fmt.Println(data)
	fmt.Println(part1(data))
	fmt.Println(part2(data))
}

func part1(nums []int) string {
	sum := 0
	for _, n := range(nums){
		sum += n
	}
	return fmt.Sprintf("Part 1: %v", sum)
}

func part2(nums []int) string {
	sum := 0
	past_sums := make(map[int]bool)
	for i := 0;; i = (i + 1) % len(nums) {
		if past_sums[sum] {
			return fmt.Sprintf("Part 2: %v", sum)
		}
		past_sums[sum] = true
		sum += nums[i]
	}
}
