package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"path/filepath"
	"io/ioutil"
	"regexp"
	"log"
)

// TODO: Check if every file in the examples/ directory is being imported in the .md files.

func main() {
	log.Println("Checking Go started")
	root := "golang"

	var imports = make([]string, 0)
	var examples = make([]string, 0)

	errors := 0
	errors += check_file(filepath.Join("tests", "check.go"))
	errors += check_main_dir(root, &imports)
	errors += check_examples_dir(root)
	errors += check_examples(root, &examples)

	//fmt.Println(imports)
	//fmt.Println(examples)
	// TODO check if there is anything in examples that is not in imports
	errors += countMissing(examples, imports)

	log.Println("Checking Go finished")
	if errors > 0 {
		fmt.Printf("%v errors found\n", errors)
		os.Exit(1)
	}
	os.Exit(0)
}

func check_examples(root string, examples *[]string) int {
	validExampleFilename := regexp.MustCompile(`^[a-z0-9_.]+$`)
	// We make sure filenames are unique across the examples.
	names := make(map[string]string)
// TODO: should filename be using underscores intsead of dashes?
	errors := 0
	path := filepath.Join(root, "examples")
	dirs, err := ioutil.ReadDir(path)
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	for _, dir := range dirs {
		if dir.Name() == "numbers.txt" {
			continue
		}
		dirpath := filepath.Join(path, dir.Name())
		//log.Println(dirpath)
		files, err := ioutil.ReadDir(dirpath)
		if err != nil {
			fmt.Printf("Error: %v", err)
			os.Exit(1)
		}
		for _, file := range files {
			//log.Printf("   %v\n", file.Name())
			res := validExampleFilename.MatchString(file.Name())
			if !res {
				fmt.Printf("Invalid character in filename: '%v' '%v'\n", dir.Name(), file.Name())
				errors++
			}

			value, ok := names[file.Name()]
			if ok {
				fmt.Printf("Duplicate: '%s' in both '%s' and '%s'\n", file.Name(), value, dir.Name())
				errors++
			}
			if dir.Name() == "package-example" && file.Name() == "src" {
				continue
			}
			//*examples = append(*examples, dir.Name() + "/" + file.Name())
			*examples = append(*examples, fmt.Sprintf("%q", dir.Name() + "/" + file.Name()))
			names[file.Name()] = dir.Name()
			if strings.HasSuffix(file.Name(), ".go") {
				errors += check_file(filepath.Join(path, dir.Name(), file.Name()))
			}
			// TODO: If there is a .go file and an .out file, run the .go file and compare the output
		}
	}
	return errors
}

// If there is a .go file check if the indentation is always tabs
func check_file(filepath string) int {
	//log.Println(filepath)
	errors := 0
	fh, err := os.Open(filepath)
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	reader := bufio.NewReader(fh)
	for true {
	   line, _ := reader.ReadString('\n')
			if strings.HasSuffix(line, " ") {
				fmt.Printf("Space suffix in file '%v' line: '%v'\n", filepath, line)
				errors++
			}
			if strings.HasPrefix(line, " ") {
				fmt.Printf("Space prefix in file '%v' line: '%v'\n", filepath, line)
				errors++
			}

	   if (line == "") {
		   break
	   }
	}

	return errors
}

func check_examples_dir(root string) int {
	errors := 0
	path := filepath.Join(root, "examples")
	dirs, err := ioutil.ReadDir(path)
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	validExampleDir := regexp.MustCompile(`^[a-z0-9-]+$`)
	//fmt.Println(path)
	for _, dir := range dirs {
		if dir.Name() == "numbers.txt" {
			continue
		}
		res := validExampleDir.MatchString(dir.Name())
		if !res {
			fmt.Printf("Invalid character in dirname: '%v'\n", dir.Name())
			errors++
		}
	}
	return errors
}

func check_main_dir(root string, imports *[]string) int {
	errors := 0
	files, err := ioutil.ReadDir(root)
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	for _, file := range files {
		if file.Name() == ".vscode" || file.Name() == "examples" || file.Name() == "golang.json" {
			continue
		}
		if ! strings.HasSuffix(file.Name(), ".md") {
			fmt.Printf("Unrecognized entry: %v\n", file.Name())
			errors++
		}
		//read in the
		filename := filepath.Join(root, file.Name())
		var fh *os.File
		//fmt.Println(filename)
		fh, err = os.Open(filename)
		if err != nil {
			panic(fmt.Sprintf("Could not open file '%v':  %v", filename, err))
		}
		// ![](examples/variable-scope/scope.go)
		//importFilename := regexp.MustCompile(`^!\[\]\(examples/([a-z-]+/[a-z_.])\)\s*\n?$`)
		importFilename := regexp.MustCompile(`^!\[\]\(examples/([a-z0-9-/_.]+)\)?$`)
		scanner := bufio.NewScanner(fh)
		for scanner.Scan() {
			line := scanner.Text()
			//fmt.Println(line)
			res := importFilename.FindAllSubmatch([]byte(line), -1)
			//fmt.Println(len(res))
			if len(res) > 0 {
				importPath := fmt.Sprintf("%q", res[0][1])
				*imports = append(*imports, importPath)
				//fmt.Printf("%q\n", res[0][1])
				//fmt.Println(line)
			}
		}
		if err := scanner.Err(); err != nil {
			fmt.Fprintln(os.Stderr, "reading standard input:", err)
		}
	}
	//fmt.Println(imports)
	return errors
}

func countMissing(a, b []string) int {
	errors := 0
	for i := 0; i < len(a); i++ {
		found := false
		for j := 0; j < len(b); j++ {
			if a[i] == b[j] {
				found = true
				break
			}
		}
		if !found {
			log.Printf("File '%v' is not imported into the slides", a[i])
			errors++
		}
	}
	return errors
}

//func walk() {
//	root := "golang"
//	subDirToSkip := "xyz"
//	err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
//		if err != nil {
//			fmt.Printf("Cannot access dir at path %q: %v", path, err)
//			return err
//		}
//		if info.IsDir() && info.Name() == subDirToSkip {
//			fmt.Printf("Skipping directory %+v \n", info.Name())
//		}
//		//fmt.Printf("Visiting %q\n", path)
//		if ! info.Mode().IsRegular() {
//			return nil
//		}
//		fmt.Printf("Visiting %q\n", path)
//		return nil
//	})
//	if err != nil {
//		fmt.Printf("error walking the path %q: %v\n", root, err)
//	}
//}
