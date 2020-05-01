package main

// go get -u github.com/ilyakaznacheev/cleanenv

import (
	"fmt"
	"os"

	"github.com/ilyakaznacheev/cleanenv"
)

type configDatabase struct {
	Port string `yaml:"port" env:"PORT" env-default:"5432"`
	Host string `yaml:"host" env:"HOST" env-default:"localhost"`
	// Name     string `yaml:"name" env:"NAME" env-default:"postgres"`
	// User     string `yaml:"user" env:"USER" env-default:"user"`
	// Password string `yaml:"password" env:"PASSWORD"`
}

var cfg configDatabase

func main() {
	err := cleanenv.ReadConfig("config.yml", &cfg)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Printf("port: %v\n", cfg.Port)
	fmt.Printf("host: %v\n", cfg.Host)
}
