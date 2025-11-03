
---

### 🐍 **main.py**
```python
import random

quotes = [
    "Simplicity is the ultimate sophistication. – Leonardo da Vinci",
    "In the middle of difficulty lies opportunity. – Albert Einstein",
    "Stay hungry, stay foolish. – Steve Jobs",
    "What we think, we become. – Buddha",
    "Do one thing every day that scares you. – Eleanor Roosevelt"
]

def show_random_quote():
    print(random.choice(quotes))

if __name__ == "__main__":
    show_random_quote()
