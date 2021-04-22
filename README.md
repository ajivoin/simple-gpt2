# simple-gpt2 ([PyPI](https://pypi.org/project/simple-gpt2/))
Python package for generating text using DeepAI's GPT-2 API.

Requires no configuration from user besides providing an API key from [DeepAI](https://deepai.org).

## Installation

```sh
$ pip install --upgrade simple-gpt2
```

## Usage
```python3
from simple_gpt2 import TextGenerator

text_gen = TextGenerator('<DeepAI API Key>')
base_text = 'Hello world!'
print(text_gen.generate(base_text))
```
