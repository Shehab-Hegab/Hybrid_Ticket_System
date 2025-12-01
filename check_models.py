import google.generativeai as genai

# PASTE YOUR KEY HERE
API_KEY = "AIzaSyBDl96wjh34dgaEZRlKHaSoYBGt8tCaPIM"
genai.configure(api_key=API_KEY)

print("🔍 Searching for available models for your key...")

try:
    found_any = False
    for m in genai.list_models():
        # We only want models that can generate text (generateContent)
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ Found: {m.name}")
            found_any = True
            
    if not found_any:
        print("❌ No text generation models found. Check your API Key permissions.")

except Exception as e:
    print(f"❌ Error: {e}")
