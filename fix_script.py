import re
import json
import codecs

# We will just run the previously written generate_content.py but with fixed regex!
with codecs.open('e:\\pagina web aldea global 2\\generate_content.py', 'r', 'utf-8') as f:
    script_content = f.read()

# Fix regex for Japan
script_content = script_content.replace(
    r'r\'<div id="country-japon"[^>]*>.*?<!-- Japan indicators will be populated here -->.*?</div>\s*</div>\'',
    r'r\'<div id="country-japon"[^>]*>.*?</div>\s*</div>(?=\s*<div id="country-arabia")\''
)

# Fix regex for UAE
script_content = script_content.replace(
    r'r\'<div id="country-arabia"[^>]*>.*?<!-- UAE indicators will be populated here -->.*?</div>\s*</div>\'',
    r'r\'<div id="country-arabia"[^>]*>.*?</div>\s*</div>(?=\s*</main>)\''
)

with codecs.open('e:\\pagina web aldea global 2\\generate_content_fixed.py', 'w', 'utf-8') as f:
    f.write(script_content)

print("Fixed script generated")
