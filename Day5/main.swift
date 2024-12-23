import Foundation

func parseInput(_ input: String) -> ([String], [[Int]]) {
    let sections = input.components(separatedBy: "\n\n")
    let rules = sections[0].split(separator: "\n").map { String($0) }
    let updates = sections[1].split(separator: "\n").map {
        $0.split(separator: ",").compactMap { Int($0) }
    }
    return (rules, updates)
}

func isCorrectOrder(update: [Int], rules: [String]) -> Bool {
    let updateSet = Set(update)
    let filteredRules = rules.compactMap { rule -> (Int, Int)? in
        let parts = rule.split(separator: "|").compactMap { Int($0) }
        guard parts.count == 2, updateSet.contains(parts[0]), updateSet.contains(parts[1]) else {
            return nil
        }
        return (parts[0], parts[1])
    }

    var precedence: [Int: Set<Int>] = [:]
    for (before, after) in filteredRules {
        precedence[before, default: []].insert(after)
    }

    for (i, current) in update.enumerated() {
        for j in (i + 1)..<update.count {
            let next = update[j]
            if precedence[next]?.contains(current) == true {
                return false
            }
        }
    }

    return true
}

func correctOrder(update: [Int], rules: [String]) -> [Int] {
    let updateSet = Set(update)
    let filteredRules = rules.compactMap { rule -> (Int, Int)? in
        let parts = rule.split(separator: "|").compactMap { Int($0) }
        guard parts.count == 2, updateSet.contains(parts[0]), updateSet.contains(parts[1]) else {
            return nil
        }
        return (parts[0], parts[1])
    }

    var graph: [Int: Set<Int>] = [:]
    for (before, after) in filteredRules {
        graph[before, default: []].insert(after)
    }

    var visited = Set<Int>()
    var stack = [Int]()

    func dfs(_ node: Int) {
        guard !visited.contains(node) else { return }
        visited.insert(node)
        for neighbor in graph[node] ?? [] {
            dfs(neighbor)
        }
        stack.append(node)
    }

    for page in update {
        dfs(page)
    }

    return stack.reversed().filter { updateSet.contains($0) }
}

func findMiddlePage(_ update: [Int]) -> Int? {
    guard !update.isEmpty else { return nil }
    return update[update.count / 2]
}

func main() {
    let filePath = "input.txt"
    
    guard let input = try? String(contentsOfFile: filePath, encoding: .utf8) else {
        print("Error: Could not read file \(filePath)")
        return
    }

    let (rules, updates) = parseInput(input)

    var totalMiddlePagesPart1 = 0
    var totalMiddlePagesPart2 = 0
    var incorrectUpdates: [[Int]] = []

    for update in updates {
        if isCorrectOrder(update: update, rules: rules) {
            if let middlePage = findMiddlePage(update) {
                totalMiddlePagesPart1 += middlePage
            }
        } else {
            incorrectUpdates.append(update)
        }
    }

    for update in incorrectUpdates {
        let correctedUpdate = correctOrder(update: update, rules: rules)
        if let middlePage = findMiddlePage(correctedUpdate) {
            totalMiddlePagesPart2 += middlePage
        }
    }

    print("Total of middle pages (Part 1): \(totalMiddlePagesPart1)")
    print("Total of middle pages (Part 2): \(totalMiddlePagesPart2)")
}


main()
