import matplotlib.pyplot as plt
import networkx as nx

class Grammar:
    def __init__(self):
        self.rules = {}

    def add_rule(self, non_terminal, productions):
        self.rules[non_terminal] = productions

    def is_simple(self):
        """Check if the grammar is simple."""
        for nt, prods in self.rules.items():
            for prod in prods:
                # Ensure no production has more than one non-terminal
                if len([char for char in prod if char.isupper()]) > 1:
                    return False
        return True

class TopDownParser:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, sequence, start_symbol):
        """Start parsing the sequence."""
        return self._parse_helper(sequence, start_symbol, 0)

    def _parse_helper(self, sequence, symbol, index):
        """Recursive helper for parsing."""
        # If terminal, directly match
        if symbol.islower():
            if index < len(sequence) and sequence[index] == symbol:
                return True, index + 1
            return False, index

        # If non-terminal, try its productions
        for production in self.grammar.rules.get(symbol, []):
            sub_index = index
            valid = True
            for sym in production:
                valid, sub_index = self._parse_helper(sequence, sym, sub_index)
                if not valid:
                    break
            if valid:
                return True, sub_index

        return False, index


def main():
    grammar = Grammar()

    while True:
        print("\n--- Top Down Parser ---")
        print("1. Add Grammar Rules")
        print("2. Check if Grammar is Simple")
        print("3. Parse a Sequence")
        print("4. Modify Grammar")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter number of rules: "))
            for _ in range(n):
                rule = input("Enter rule (e.g., S -> aA | bB): ").strip()

                # Ensure the rule contains exactly one "->"
                if "->" not in rule or rule.count("->") != 1:
                    print("Invalid rule format! Please use the format: S -> aA | bB")
                    continue

                try:
                    non_terminal, productions = rule.split("->")
                    non_terminal = non_terminal.strip()
                    productions = [p.strip() for p in productions.split("|")]

                    # Ensure the non-terminal is valid
                    if not non_terminal.isupper():
                        print("Non-terminal must be an uppercase letter!")
                        continue

                    grammar.add_rule(non_terminal, productions)
                    print(f"Rule added: {non_terminal} -> {productions}")
                except Exception as e:
                    print(f"Error processing the rule: {e}")

        elif choice == "2":
            if grammar.is_simple():
                print("The grammar is Simple.")
            else:
                print("The grammar is NOT Simple.")

        elif choice == "3":
            if not grammar.rules:
                print("No grammar rules defined! Please add grammar first.")
                continue

            sequence = input("Enter sequence to parse: ").strip()
            start_symbol = list(grammar.rules.keys())[0]  # Assume the first added non-terminal is the start symbol
            parser = TopDownParser(grammar)
            result, _ = parser.parse(sequence, start_symbol)

            if result:
                print("Accepted")
            else:
                print("Rejected")

        elif choice == "4":
            grammar = Grammar()  # Reset grammar
            print("Grammar reset successfully.")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
