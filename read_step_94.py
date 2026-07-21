import json
import codecs

f = codecs.open('C:\\Users\\Lucas\\.gemini\\antigravity-ide\\brain\\99ec0e81-d2fb-4ae9-845b-4f9463d98ccc\\.system_generated\\logs\\transcript.jsonl', 'r', 'utf-8')
for line in f:
    data = json.loads(line)
    if data.get('step_index') == 94:
        print("STEP 94:")
        print("TYPE:", data.get('type'))
        print("TOOL CALLS LENGTH:", len(data.get('tool_calls', [])))
        if data.get('tool_calls'):
            print("FIRST TOOL CALL NAME:", data['tool_calls'][0]['name'])
            # print first 500 chars of code content
            code = data['tool_calls'][0]['args'].get('CodeContent', '')
            print("CODE CONTENT START:")
            print(code[:1000])
        break
