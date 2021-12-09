#!/usr/bin/swift

import Foundation

let dataFilePath = "../day2_data.txt"

// Read file
let fileContents = try String(contentsOfFile: dataFilePath, encoding: String.Encoding.utf8)
let directions = fileContents.split(whereSeparator: \.isNewline).map( { $0 } ) // Force unwrapping not ideal

// Variables to store counts in
var aimCount = 0
var horizontalCount = 0
var depthCount = 0

// Update counter for each direction instruction
directions.forEach {
    let magnitude = Int($0.filter("0123456789".contains))!
    switch $0 {
        case _ where $0.contains("down"): aimCount += magnitude
        case _ where $0.contains("up"): aimCount -= magnitude
        case _ where $0.contains("forward"):
            horizontalCount += magnitude
            depthCount += (aimCount * magnitude)
        default: break
    }
}

print("Aim: \(aimCount), horizontal: \(horizontalCount), depth: \(depthCount) = \(horizontalCount)*\(depthCount) = \(horizontalCount * depthCount)")