import json
import codecs

with codecs.open('e:\\pagina web aldea global 2\\generate_content.py', 'r', 'utf-8') as f:
    script_content = f.read()

# Instead of using regex, we will use string manipulation in Python
replacement_logic = """
try:
    with codecs.open('e:\\\\pagina web aldea global 2\\\\entregas\\\\entrega-3\\\\index.html', 'r', 'utf-8') as f:
        content = f.read()

    japon_start = content.find('<div id="country-japon"')
    arabia_start = content.find('<div id="country-arabia"')
    main_end = content.find('</main>')

    if japon_start != -1 and arabia_start != -1 and main_end != -1:
        new_content = content[:japon_start] + html_japon + "\\n\\n        " + html_eau + "\\n    " + content[main_end:]
        new_content = new_content.replace('</script>\\n</body>', js_injection)
        with codecs.open('e:\\\\pagina web aldea global 2\\\\entregas\\\\entrega-3\\\\index.html', 'w', 'utf-8') as f:
            f.write(new_content)
        print("Success: File updated.")
    else:
        print("Error: Could not find markers.")
except Exception as e:
    print(f"Error: {e}")
"""

# replace the bottom part of generate_content.py starting from "with open('e:\\"
new_script = script_content[:script_content.find("with open('e:\\\\pagina web aldea global 2")] + replacement_logic

with codecs.open('e:\\pagina web aldea global 2\\generate_content_string.py', 'w', 'utf-8') as f:
    f.write(new_script)

print("String replacement script generated")
