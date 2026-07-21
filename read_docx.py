import zipfile, xml.etree.ElementTree as ET
with open('emiratos_temp.txt', 'w', encoding='utf-8') as f:
    text = ''
    for paragraph in ET.XML(zipfile.ZipFile(r'e:\pagina web aldea global 2\entregas\entrega-3\INDICADORES\emiratos arabes.docx').read('word/document.xml')).iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        text += ''.join([node.text for node in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]) + '\n'
    f.write(text)
