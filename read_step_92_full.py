import json
import codecs

f = codecs.open('C:\\Users\\Lucas\\.gemini\\antigravity-ide\\brain\\99ec0e81-d2fb-4ae9-845b-4f9463d98ccc\\.system_generated\\logs\\transcript.jsonl', 'r', 'utf-8')
for line in f:
    data = json.loads(line)
    if data.get('step_index') == 92:
        print("STEP 92 CONTENT:")
        print(data.get('content', '')[:3000])
        print("LENGTH:", len(data.get('content', '')))
        break
