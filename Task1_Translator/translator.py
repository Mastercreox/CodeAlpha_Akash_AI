from deep_translator import GoogleTranslator

def main():
    print("=== Language Translator ===")
    text = input("Enter text: ").strip()
    if not text:
        print("No text entered.")
        return

    # Change 'hi' to any target language code if needed
    try:
        result = GoogleTranslator(source='auto', target='hi').translate(text)
        print("Translated:", result)
    except Exception as e:
        print(f"Translation error: {e}")

if __name__ == "__main__":
    main()
