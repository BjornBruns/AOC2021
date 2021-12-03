#!/usr/bin/swift

import Foundation

let dataFilePath = "day1_data.txt"

// Read file
let fileContents = try String(contentsOfFile: dataFilePath, encoding: String.Encoding.utf8)
let depthMeasurements = fileContents.split(whereSeparator: \.isNewline).map( { Int($0)! } ) // Force unwrapping not ideal

// First make sure there are 2 values before the current (prevent indexOutOfRange error), then sum current and previous two values
let slidingMeasurements = depthMeasurements.enumerated().filter( { $0.offset > 1 } ).map( { $0.element + depthMeasurements[$0.offset - 1] + depthMeasurements[$0.offset - 2] } )

// Same logic as puzzle 1 - filter by looking at previous measurement (guard against first value, otherwise IndexOutOfRange error)
let deeperMeasurements = slidingMeasurements.enumerated().filter( { ($0.offset != 0) ? $0.element > slidingMeasurements[$0.offset - 1] : false } )
print(deeperMeasurements.count)