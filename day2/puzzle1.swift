#!/usr/bin/swift

import Foundation

let dataFilePath = "day2_data.txt"

// Read file
let fileContents = try String(contentsOfFile: dataFilePath, encoding: String.Encoding.utf8)
let directions = fileContents.split(whereSeparator: \.isNewline).map( { $0 } ) // Force unwrapping not ideal

// Reduce directions to counts per direction
let downCount = directions.reduce(0) { $0 + ($1.contains("down") ? Int($1.filter("0123456789".contains))! : 0 ) }
let upCount = directions.reduce(0) { $0 + ($1.contains("up") ? Int($1.filter("0123456789".contains))! : 0 ) }
let forwardCount = directions.reduce(0) { $0 + ($1.contains("forward") ? Int($1.filter("0123456789".contains))! : 0) }

print("Up: \(upCount), down: \(downCount), forward: \(forwardCount) = \(forwardCount)*(\(downCount)-\(upCount)) = \(forwardCount * (downCount-upCount))")