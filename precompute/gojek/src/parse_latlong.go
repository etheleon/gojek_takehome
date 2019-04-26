package main

import (
	"bufio"
  "encoding/binary"
	"encoding/csv"
	"encoding/hex"
	"fmt"
	"github.com/golang/geo/s2"
	"io"
	"log"
	"os"
  "strconv"
  "strings"
)

func main() {

	csvFile, _ := os.Open(os.Args[1])
	reader := csv.NewReader(bufio.NewReader(csvFile))

  reader.Read()
	for {
		line, error := reader.Read()
		if error == io.EOF {
			break
		} else if error != nil {
			log.Fatal(error)
		}
		latitude, err := strconv.ParseFloat(line[1], 64)
		if err != nil {
			fmt.Println("Failed to parse latitude")
			return
		}
    // fmt.Println(latitude)

		longitude, err := strconv.ParseFloat(line[2], 64)
		if err != nil {
			fmt.Println("Failed to parse longitude")
			return
		}

    s2ID := int64(s2.CellIDFromLatLng(s2.LatLngFromDegrees(latitude, longitude)).Parent(16))

    content := make([]byte, 8)
    binary.BigEndian.PutUint64(content, uint64(s2ID))
	  encodedStr := hex.EncodeToString(content)
	  fmt.Printf("%s,%s,%s\n", line[0], strings.Trim(encodedStr, "0"), line[3])
	}
}
