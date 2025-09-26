Overview
Pattern is a Python library I developed for efficient pattern matching and recognition in text, data, or code structures. It supports regex-based searching, algorithmic pattern detection (e.g., sequences in lists), and basic design pattern implementations (e.g., Singleton, Observer) to demonstrate clean, reusable code. This project is great for practicing algorithmic thinking and is inspired by common interview problems—perfect for developers honing skills in string manipulation, recursion, and OOP.
Note: Built for educational use; extend it for real-world applications like log analysis or code refactoring.
Features

Regex Engine: Advanced text pattern matching with custom validators (e.g., email, phone, or custom formats).
Algorithmic Patterns: Detect sequences, palindromes, or subsequences in arrays/strings using efficient algorithms (O(n) where possible).
Design Patterns: Implement core GoF patterns (Gang of Four) like Factory, Strategy, and Decorator for modular code.
CLI Tool: Quick command-line interface for testing patterns on input data.
Extensible: Plugin system for adding new pattern types or backends (e.g., integrate with NLTK for NLP patterns).
Performance Optimized: Includes Big-O analysis and benchmarks for key functions.

Tech Stack

Language: Python 3.9+
Key Libraries:

re (built-in) for regex operations.
typing for type hints and static analysis.
pytest for unit testing.
Optional: nltk for advanced text patterns.


Minimal dependencies for easy portability.

Getting Started
Prerequisites

Python 3.9 or higher.
Git for cloning.

Installation

Clone the repository:
bashgit clone https://github.com/abd0o0/pattern.git
cd pattern

Create a virtual environment and install dependencies:
bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Usage

CLI Pattern Matching:
bashpython pattern_cli.py --input "abc123def456" --pattern "\d{3}" --output matches.json
This extracts all 3-digit sequences and saves them as JSON (output: ["123", "456"]).
Programmatic Use (in a Python script):
pythonfrom pattern.matcher import RegexMatcher, SequenceDetector

# Text pattern example
matcher = RegexMatcher(pattern=r"[a-zA-Z]+ \d{4}")  # e.g., "Word 2025"
results = matcher.find_in("Hello 2025, World 2026!")
print(results)  # Output: ["Hello 2025", "World 2026"]

# Algorithmic pattern example
detector = SequenceDetector()
seqs = detector.find_longest_increasing([3, 1, 4, 1, 5, 9, 2, 6])  # Fibonacci-like
print(seqs)  # Output: [1, 1, 2, 6] (increasing subsequence)

Design Pattern Example (Observer):
pythonfrom pattern.design.observer import Subject, Observer

class NewsSubject(Subject):
    def notify(self, message):
        super().notify(message)

observer = Observer("User1")
subject = NewsSubject()
subject.attach(observer)
subject.notify("New update available!")  # Triggers observer callback


Run python pattern_cli.py --help for more flags. Examples in /examples folder; benchmarks in /tests.
