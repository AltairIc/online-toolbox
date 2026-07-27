import os

tools_dir = r"C:\Users\Altair\Documents\Codex\2026-07-27\ban\outputs\toolsite\app\templates\tools"

# Define all tool templates (name, extra_content, extra_script)
tools = {
    "base64.html": ("""
<div class=\"bg-white rounded-xl border border-gray-200 p-6 max-w-3xl mx-auto\">
    <h1 class=\"text-2xl font-bold text-gray-900 mb-2\">Base64 Encoder / Decoder</h1>
    <p class=\"text-gray-500 mb-4\">Encode text to Base64 or decode Base64 back to text.</p>
    <div class=\"flex gap-2 mb-4\">
        <button class=\"px-6 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700\" onclick=\"process('encode')\">Encode</button>
        <button class=\"px-6 py-2 bg-green-600 text-white rounded-lg text-sm font-medium hover:bg-green-700\" onclick=\"process('decode')\">Decode</button>
        <button class=\"px-4 py-2 text-sm text-gray-600 border border-gray-300 rounded-lg hover:bg-gray-50\" onclick=\"swap()\">Swap &uarr;&darr;</button>
    </div>
    <textarea id=\"inputText\" rows=\"6\" class=\"w-full mb-4 font-mono text-sm\" placeholder=\"Enter text to encode/decode...\"></textarea>
    <textarea id=\"resultText\" rows=\"6\" class=\"w-full font-mono text-sm\" readonly placeholder=\"Result...\"></textarea>
    <button class=\"mt-2 text-sm text-blue-600 hover:underline\" onclick=\"copyResult()\">Copy to clipboard</button>
</div>
<script>
async function process(mode){const r=await fetch('/api/base64',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({data:document.getElementById('inputText').value,mode})});const d=await r.json();document.getElementById('resultText').value=d.result||d.error}
function swap(){const i=document.getElementById('inputText'),r=document.getElementById('resultText');[i.value,r.value]=[r.value,i.value]}
function copyResult(){const t=document.getElementById('resultText');t.select();navigator.clipboard.writeText(t.value)}
</script>
""", "Base64 Encoder Decoder - Encode and Decode Base64 Online"),

    "url-encoder.html": ("""
<div class=\"bg-white rounded-xl border border-gray-200 p-6 max-w-3xl mx-auto\">
    <h1 class=\"text-2xl font-bold text-gray-900 mb-2\">URL Encoder / Decoder</h1>
    <p class=\"text-gray-500 mb-4\">Encode or decode URLs for safe web transmission.</p>
    <div class=\"flex gap-2 mb-4\">
        <button class=\"px-6 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700\" onclick=\"process('encode')\">Encode</button>
        <button class=\"px-6 py-2 bg-green-600 text-white rounded-lg text-sm font-medium hover:bg-green-700\" onclick=\"process('decode')\">Decode</button>
    </div>
    <textarea id=\"inputText\" rows=\"6\" class=\"w-full mb-4 font-mono text-sm\" placeholder=\"Enter URL to encode/decode...\"></textarea>
    <textarea id=\"resultText\" rows=\"6\" class=\"w-full font-mono text-sm\" readonly placeholder=\"Result...\"></textarea>
    <button class=\"mt-2 text-sm text-blue-600 hover:underline\" onclick=\"copyResult()\">Copy to clipboard</button>
</div>
<script>
async function process(mode){const r=await fetch('/api/url-encoder',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({data:document.getElementById('inputText').value,mode})});const d=await r.json();document.getElementById('resultText').value=d.result}
function copyResult(){const t=document.getElementById('resultText');t.select();navigator.clipboard.writeText(t.value)}
</script>
""", "URL Encoder Decoder - Encode and Decode URLs Online"),

    "hash-generator.html": ("""
<div class=\"bg-white rounded-xl border border-gray-200 p-6 max-w-3xl mx-auto\">
    <h1 class=\"text-2xl font-bold text-gray-900 mb-2\">Hash Generator</h1>
    <p class=\"text-gray-500 mb-4\">Generate MD5, SHA-1, SHA-256 and SHA-512 hashes for any text.</p>
    <textarea id=\"inputText\" rows=\"4\" class=\"w-full mb-4 font-mono text-sm\" placeholder=\"Enter text to hash...\"></textarea>
    <button class=\"px-6 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 mb-6\" onclick=\"generate()\">Generate Hashes</button>
    <div id=\"results\"></div>
</div>
<script>
async function generate(){const r=await fetch('/api/hash-generator',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({data:document.getElementById('inputText').value})});const d=await r.json();const r2=['md5','sha1','sha256','sha512'];document.getElementById('results').innerHTML=r2.map(a=>'<div class=\"mb-3\"><div class=\"text-xs font-medium text-gray-500 uppercase mb-1\">'+a+'</div><div class=\"bg-gray-50 rounded-lg p-3 font-mono text-sm break-all\">'+d[a]+'</div></div>').join('')}
</script>
""", "Hash Generator - Generate MD5 SHA1 SHA256 SHA512 Online"),

    "html-entity.html": ("""
<div class=\"bg-white rounded-xl border border-gray-200 p-6 max-w-3xl mx-auto\">
    <h1 class=\"text-2xl font-bold text-gray-900 mb-2\">HTML Entity Converter</h1>
    <p class=\"text-gray-500 mb-4\">Escape or unescape HTML entities in your text.</p>
    <div class=\"flex gap-2 mb-4\">
        <button class=\"px-6 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700\" onclick=\"process('encode')\">Escape</button>
        <button class=\"px-6 py-2 bg-green-600 text-white rounded-lg text-sm font-medium hover:bg-green-700\" onclick=\"process('decode')\">Unescape</button>
    </div>
    <textarea id=\"inputText\" rows=\"6\" class=\"w-full mb-4 font-mono text-sm\" placeholder=\"Enter HTML...\"></textarea>
    <textarea id=\"resultText\" rows=\"6\" class=\"w-full font-mono text-sm\" readonly placeholder=\"Result...\"></textarea>
    <button class=\"mt-2 text-sm text-blue-600 hover:underline\" onclick=\"copyResult()\">Copy to clipboard</button>
</div>
<script>
async function process(mode){const r=await fetch('/api/html-entity',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({data:document.getElementById('inputText').value,mode})});const d=await r.json();document.getElementById('resultText').value=d.result}
function copyResult(){const t=document.getElementById('resultText');t.select();navigator.clipboard.writeText(t.value)}
</script>
""", "HTML Entity Converter - Escape and Unescape HTML Entities Online"),

    "lorem-ipsum.html": ("""
<div class=\"bg-white rounded-xl border border-gray-200 p-6 max-w-3xl mx-auto\">
    <h1 class=\"text-2xl font-bold text-gray-900 mb-2\">Lorem Ipsum Generator</h1>
    <p class=\"text-gray-500 mb-4\">Generate placeholder text for your designs and layouts.</p>
    <div class=\"flex items-center gap-4 mb-4\">
        <label class=\"text-sm text-gray-600\">Count: <input id=\"count\" type=\"number\" value=\"3\" min=\"1\" max=\"100\" class=\"w-20\"></label>
        <label class=\"text-sm text-gray-600\">Unit: <select id=\"unit\"><option value=\"paragraphs\">Paragraphs</option><option value=\"sentences\">Sentences</option><option value=\"words\">Words</option></select></label>
        <button class=\"px-6 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700\" onclick=\"generate()\">Generate</button>
    </div>
    <textarea id=\"resultText\" rows=\"10\" class=\"w-full font-mono text-sm\" readonly placeholder=\"Generated text will appear here...\"></textarea>
    <button class=\"mt-2 text-sm text-blue-600 hover:underline\" onclick=\"copyResult()\">Copy to clipboard</button>
</div>
<script>
async function generate(){const r=await fetch('/api/lorem-ipsum',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({count:parseInt(document.getElementById('count').value),unit:document.getElementById('unit').value})});const d=await r.json();document.getElementById('resultText').value=d.result}
function copyResult(){const t=document.getElementById('resultText');t.select();navigator.clipboard.writeText(t.value)}
</script>
""", "Lorem Ipsum Generator - Generate Placeholder Text Online"),

    "regex-tester.html": ("""
<div class=\"bg-white rounded-xl border border-gray-200 p-6 max-w-3xl mx-auto\">
    <h1 class=\"text-2xl font-bold text-gray-900 mb-2\">Regex Tester</h1>
    <p class=\"text-gray-500 mb-4\">Test your regular expressions with real-time matching.</p>
    <label class=\"text-sm font-medium text-gray-700 mb-1 block\">Regular Expression</label>
    <input id=\"pattern\" type=\"text\" class=\"w-full mb-4 font-mono text-sm\" placeholder=\"Enter regex pattern (e.g. \\\\d+)\">
    <label class=\"text-sm font-medium text-gray-700 mb-1 block\">Test Text</label>
    <textarea id=\"testText\" rows=\"8\" class=\"w-full mb-4 font-mono text-sm\" placeholder=\"Enter text to test against...\"></textarea>
    <button class=\"px-6 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 mb-4\" onclick=\"test()\">Test Regex</button>
    <div id=\"result\"></div>
</div>
<script>
async function test(){const r=await fetch('/api/regex-tester',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({pattern:document.getElementById('pattern').value,text:document.getElementById('testText').value})});const d=await r.json();if(d.error){document.getElementById('result').innerHTML='<div class=\"bg-red-50 text-red-700 rounded-lg p-3 text-sm\">'+d.error+'</div>';return}document.getElementById('result').innerHTML='<div class=\"bg-green-50 text-green-700 rounded-lg p-3 text-sm mb-3\">'+d.count+' match'+(d.count!=1?'es':'')+' found</div>'+(d.matches.length?d.matches.map((m,i)=>'<div class=\"bg-gray-50 rounded-lg p-3 mb-2 font-mono text-sm\"><span class=\"text-gray-400\">#'+(i+1)+'</span> \"'+m.text+'\" <span class=\"text-gray-400\">(pos: '+m.start+')</span></div>'):'')}
</script>
""", "Regex Tester - Test Regular Expressions Online"),

    "text-diff.html": ("""
<div class=\"bg-white rounded-xl border border-gray-200 p-6 max-w-3xl mx-auto\">
    <h1 class=\"text-2xl font-bold text-gray-900 mb-2\">Text Diff Checker</h1>
    <p class=\"text-gray-500 mb-4\">Compare two texts and see the differences highlighted.</p>
    <div class=\"grid grid-cols-2 gap-4 mb-4\">
        <div><label class=\"text-sm font-medium text-gray-700 mb-1 block\">Original Text</label><textarea id=\"text1\" rows=\"8\" class=\"w-full font-mono text-sm\" placeholder=\"Original text...\"></textarea></div>
        <div><label class=\"text-sm font-medium text-gray-700 mb-1 block\">Changed Text</label><textarea id=\"text2\" rows=\"8\" class=\"w-full font-mono text-sm\" placeholder=\"Modified text...\"></textarea></div>
    </div>
    <button class=\"px-6 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 mb-4\" onclick=\"compare()\">Compare</button>
    <pre id=\"diffResult\" class=\"bg-gray-50 rounded-lg p-4 font-mono text-sm overflow-x-auto whitespace-pre-wrap\"></pre>
</div>
<script>
async function compare(){const r=await fetch('/api/text-diff',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text1:document.getElementById('text1').value,text2:document.getElementById('text2').value})});const d=await r.json();document.getElementById('diffResult').textContent=d.diff}
</script>
""", "Text Diff Checker - Compare Text Differences Online"),

    "password-generator.html": ("""
<div class=\"bg-white rounded-xl border border-gray-200 p-6 max-w-3xl mx-auto\">
    <h1 class=\"text-2xl font-bold text-gray-900 mb-2\">Password Generator</h1>
    <p class=\"text-gray-500 mb-4\">Generate strong, random passwords instantly.</p>
    <div class=\"grid grid-cols-2 gap-4 mb-6\">
        <div><label class=\"text-sm text-gray-600\">Length: <input id=\"length\" type=\"number\" value=\"16\" min=\"4\" max=\"128\" class=\"w-20\"></label></div>
        <div></div>
        <label class=\"flex items-center gap-2 text-sm\"><input type=\"checkbox\" id=\"upper\" checked> <span>Uppercase (A-Z)</span></label>
        <label class=\"flex items-center gap-2 text-sm\"><input type=\"checkbox\" id=\"lower\" checked> <span>Lowercase (a-z)</span></label>
        <label class=\"flex items-center gap-2 text-sm\"><input type=\"checkbox\" id=\"digits\" checked> <span>Digits (0-9)</span></label>
        <label class=\"flex items-center gap-2 text-sm\"><input type=\"checkbox\" id=\"symbols\" checked> <span>Symbols (!@#$)</span></label>
    </div>
    <button class=\"px-6 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 mb-4\" onclick=\"generate()\">Generate Password</button>
    <div id=\"result\" class=\"bg-gray-50 rounded-lg p-4 font-mono text-lg text-center break-all\"></div>
    <button class=\"mt-2 text-sm text-blue-600 hover:underline\" onclick=\"copyPass()\">Copy to clipboard</button>
</div>
<script>
async function generate(){const r=await fetch('/api/password-generator',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({length:parseInt(document.getElementById('length').value),use_upper:document.getElementById('upper').checked,use_lower:document.getElementById('lower').checked,use_digits:document.getElementById('digits').checked,use_symbols:document.getElementById('symbols').checked})});const d=await r.json();document.getElementById('result').textContent=d.password}
function copyPass(){navigator.clipboard.writeText(document.getElementById('result').textContent)}
</script>
""", "Password Generator - Generate Strong Random Passwords Online"),
}

for filename, (content, title) in tools.items():
    full = f'''{{% extends "base.html" %}}
{{% block title %}}{title}{{% endblock %}}
{{% block content %}}
{content}
{{% endblock %}}'''
    path = os.path.join(tools_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(full)
    print(f"Created {filename}")
