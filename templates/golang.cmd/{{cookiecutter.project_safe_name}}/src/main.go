package main

import (
	"fmt"
	"os"

	"github.com/urfave/cli"
)

const VERSION = "0.0.1"

func main() {
	app := cli.NewApp()
	app.Version = VERSION
	app.Commands = []cli.Command{
		{
			Name:  "version",
			Usage: "Show version",
			Action: func(c *cli.Context) error {
				fmt.Println(VERSION)
				return nil
			},
		},
	}

	app.Run(os.Args)
}
