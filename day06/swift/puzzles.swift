#!/usr/bin/swift

import Foundation

let dataFilePath = "../day6_data.txt"

// Read file
let fileContents = try String(contentsOfFile: dataFilePath, encoding: String.Encoding.utf8)

// Map the file contents to a dictionary that contains the number of fish in each age category
var fishDict = [Int: Int]()
fileContents.split(separator: ",").map( { Int($0)! }).forEach( { fishDict[$0, default: 0] += 1 })

func solve(days: Int, fishDict: [Int: Int]) -> Int {
    var fishCopy = fishDict
    for _ in 1...days {
        var newFish = [Int: Int]()
        for (ageGroup, count) in fishCopy {
            if (ageGroup == 0) {
                newFish[6, default: 0] += count
                newFish[8, default: 0] += count
            } else {
                newFish[(ageGroup - 1), default: 0] += count
            }
        }
        fishCopy = newFish
    }
    return fishCopy.values.reduce(0, { $0 + $1 })
}

print(solve(days: 80, fishDict: fishDict))
print(solve(days: 256, fishDict: fishDict))