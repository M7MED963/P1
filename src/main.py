# Final CI trigger test
from calculator.evaluator import evaluate_expression

def main():
    print("Welcome to CLI Calculator! Type 'exit' to quit.")
    while True:
        expr = input(">> ")
        if expr.lower() in ["exit", "quit"]:
            break
        try:
            result = evaluate_expression(expr)
            print("= ", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
