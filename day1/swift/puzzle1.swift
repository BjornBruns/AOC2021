#!/usr/bin/swift

import Foundation

let dataFilePath = "../day1_data.txt"

// Read file
let fileContents = try String(contentsOfFile: dataFilePath, encoding: String.Encoding.utf8)
let depthMeasurements = fileContents.split(whereSeparator: \.isNewline).map( { Int($0)! } ) // Force unwrapping not ideal

// Filter by looking at previous measurement (guard against first value, otherwise IndexOutOfRange error)
let deeperMeasurements = depthMeasurements.enumerated().filter( { ($0.offset != 0) ? $0.element > depthMeasurements[$0.offset - 1] : false } )
print(deeperMeasurements.count)
