package s3

import (
	"fmt"
	git "testProject/Mods/Git"
)

func PrintS31(a string) {
	fmt.Println("S31", a)
	printS32("hi")
	git.PrintGit1("hi")
	git.PrintGit2("hi")

}
