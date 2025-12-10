import json
import re
import difflib
import os
import random

DATA_FILE = "chatbot_data.json"
BACKUP_DIR = "chatbot_backups"
SIMILARITY_THRESHOLD = 0.4
MAX_MATCHES = 4

print("Welcome User!")
name = input("Please enter your name: ")
print(f"Hello, {name}! Let's perform some calculations.")
need = input("please enter what you want to do {calcuation, chat,}: ")
if need.lower() == 'calcuation':
    print("You have chosen calculation, then continue...")
    print("Here are the available operations: '+', '-', '*', '/' '%', '^', 'sqrt', 'ordinal'")

    while True:
        oper = input("Enter the operation you want to perform: ")
        a = int(input("Enter the first number (a): "))
        b = int(input("Enter the second number (b): "))

        if oper in ['+', 'add', 'addition', 'plus', 'sum']:
            print("The sum of the two numbers is:", a + b)
            print("")

        elif oper in ['-', 'subtract', 'subtraction', 'minus', 'difference']:
            print("The difference of the two numbers is:", a - b)
            print("")

        elif oper in ['*', 'multiply', 'multiplication', 'product', 'times']:
            print("The product of the two numbers is:", a * b)
            print("")

        elif oper in ['/', 'divide', 'division', 'quotient']:
            if b != 0:
                print("The quotient of the two numbers is:", a / b)
                print("")
            else:
                print("Error: Division by zero is not allowed.")
                print("")

        elif oper in ['%', 'modulus', 'mod']:
            if b != 0:
                print("The modulus of the two numbers is:", a % b)
                print("")
            else:
                print("Error: Modulus by zero is not allowed.")
                print("")

        elif oper in ['^', 'exponent', 'power', '**']:
            print("The result of exponentiation is:", a ** b)
            print("")

        elif oper in ['sqrt', 'square root']:
            import math, cmath
            if a >= 0:
                print("The square root of the first number is:", math.sqrt(a))
                print("")
            else:
                print("The square root of the first number is:", cmath.sqrt(a))
                print("")
        elif oper in ['ordinal', 'ord']:
            def get_ordinal(n):
                if 10 <= n % 100 <= 20:
                    suffix = 'th'
                else:
                    suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
                return str(n) + suffix
        
            print(f"The ordinal form of {a} is: {get_ordinal(a)}")
            print("")
        elif oper.lower() in ['exit', 'quit']:
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid operation. Please try again.")
            print("")

if need.lower() == 'chat':
    def load_knowledge():
        if not os.path.exists(DATA_FILE):
            default_data = {
                "hello": ["Hi there!", "Hello!", "Greetings!"],
                "how are you": ["Thanks for asking!, I am doing well", "Doing great, how about you?"],
                "what is your name": ["I am Singh AI, your personal assistant."],
                "Tell me a joke": ["Why did the scarecrow win an award? Because he was outstanding in his field!"],
                "Bye": ["Fine! see you later."],
            }
            with open(DATA_FILE, 'w') as f:
                json.dump(default_data, f, indent=4)
            return default_data
        else:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)


    def save_knowledge(data):
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    def preprocess(text):
        text = text.lower().strip()
        text = re.sub(r"[^\w\s']", "", text)
        text = re.sub(r"\s+", " ", text)
        return text
    def get_best_match(user_input, knowledge):
        user = preprocess(user_input)
        keys = list(knowledge.keys())

        if user in keys:
            return user, 1.0

        matches = difflib.get_close_matches(user, keys, n=MAX_MATCHES, cutoff=SIMILARITY_THRESHOLD)
        if matches:
            best = matches[0]
            score = difflib.SequenceMatcher(None, user, best).ratio()
            return best, score

        user_tokens = set(user.split())
        best, best_score = None, 0.0
        for k in keys:
            k_tokens = set(k.split())
            overlap = len(user_tokens & k_tokens) / max(1, len(user_tokens | k_tokens))
            if overlap > best_score:
                best_score = overlap
                best = k

        if best_score >= 0.60:
            return best, best_score
        return None, 0.0
    knowledge = load_knowledge()
    print("You have chosen chat, then continue...")
    print("Type 'exit' or 'quit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chat ended. Goodbye!")
            break

        best_match, score = get_best_match(user_input, knowledge)
        if best_match:
            response = random.choice(knowledge[best_match])
            print("Singh AI:", response)
        else:
            print("Singh AI: I'm not sure how to respond to that. Could you please teach me?")
            new_response = input("Your response: ")
            knowledge[preprocess(user_input)] = [new_response]
            save_knowledge(knowledge)
            print("Singh AI: Thank you! I've learned something new today.")