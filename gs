#!/bin/bash -e

root=$(dirname $(realpath $0))
$root/generate_slides --ext html $1

