with open('DINKES_PINRANG_MOCKUP_V4/assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m_hdr = re.search(r'function header\([^)]*\)\s*\{[\s\S]*?\nfunction footer', text)
if m_hdr:
    print('HEADER CODE:')
    print(m_hdr.group(0))

m_ftr = re.search(r'function footer\([^)]*\)\s*\{[\s\S]*?\nfunction [a-zA-Z0-9_]+Page', text)
if m_ftr:
    print('FOOTER CODE:')
    print(m_ftr.group(0))
