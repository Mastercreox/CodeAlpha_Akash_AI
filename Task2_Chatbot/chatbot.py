faq = {
    "hacking": "Hacking is finding vulnerabilities in systems.",
    "bug bounty": "Bug bounty is earning money by finding bugs.",
    "sql injection": "SQL injection is a database attack.",
    "xss": "Cross-Site Scripting (XSS) allows attackers to inject scripts into web pages."
}

def main():
    print("=== FAQ Chatbot (type 'exit' to quit) ===")
    while True:
        question = input("Ask: ").lower().strip()
        if question == "exit":
            print("Goodbye!")
            break

        found = False
        for key in faq:
            if key in question:
                print(faq[key])
                found = True
                break

        if not found:
            print("Sorry, I don't understand.")

if __name__ == "__main__":
    main()
