import os

tools_dir = r"C:\Users\Altair\Documents\Codex\2026-07-27\ban\outputs\toolsite\app\templates\tools"

tools = {
    "color-converter.html": ("""
<div class=\"bg-white rounded-xl border border-gray-200 p-6 max-w-3xl mx-auto\">
    <h1 class=\"text-2xl font-bold text-gray-900 mb-2\">Color Converter</h1>
    <p class=\"text-gray-500 mb-4\">Convert colors between HEX, RGB formats.</p>
    <div class=\"grid grid-cols-2 gap-4 mb-6\">
        <div><label class=\"text-sm font-medium text-gray-700 mb-1 block\">Convert from</label><select id=\"direction\" class=\"w-full\"><option value=\"hex_to_rgb\">HEX to RGB</option><option value=\"rgb_to_hex\">RGB to HEX</option></select></div>
        <div><label class=\"text-sm font-medium text-gray-700 mb-1 block\">Color preview</label><div id=\"preview\" class=\"w-full h-10 rounded-lg border\"></div></div>
    </div>
    <label class=\"text-sm font-medium text-gray-700 mb-1 block\">Color value</label>
    <div class=\"flex gap-2 mb-4\"><input id=\"colorInput\" type=\"text\" class=\"font-mono\" placeholder=\"#ff0000 or rgb(255,0,0)\"><button class=\"px-6 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700\" onclick=\"convert()\">Convert</button></div>
    <div id=\"result\" class=\"bg-gray-50 rounded-lg p-4 font-mono text-sm\"></div>
</div>
<script>
async function convert(){const r=await fetch('/api/color-converter',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({color:document.getElementById('colorInput').value,from_to:document.getElementById('direction').value})});const d=await r.json();if(d.error){document.getElementById('result').textContent='Error: '+d.error;return}const h=d.hex||'';document.getElementById('preview').style.background=h;document.getElementById('result').innerHTML='<div>HEX: '+d.hex+'</div><div>RGB: '+d.rgb+'</div>'}
document.getElementById('direction').addEventListener('change',()=>{document.getElementById('colorInput').value='';document.getElementById('result').textContent=''});
</script>
""", "Color Converter - Convert HEX to RGB and RGB to HEX Online"),

    "uuid-generator.html": ("""
<div class=\"bg-white rounded-xl border border-gray-200 p-6 max-w-3xl mx-auto\">
    <h1 class=\"text-2xl font-bold text-gray-900 mb-2\">UUID Generator</h1>
    <p class=\"text-gray-500 mb-4\">Generate random UUIDs (v4) in bulk. Perfect for database keys, test data, and unique identifiers.</p>
    <div class=\"flex items-center gap-4 mb-4\">
        <label class=\"text-sm text-gray-600\">Count: <input id=\"count\" type=\"number\" value=\"5\" min=\"1\" max=\"100\" class=\"w-20\"></label>
        <button class=\"px-6 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700\" onclick=\"generate()\">Generate UUIDs</button>
        <button class=\"px-4 py-2 text-sm border border-gray-300 rounded-lg hover:bg-gray-50\" onclick=\"copyAll()\">Copy All</button>
    </div>
    <div id=\"result\" class=\"bg-gray-50 rounded-lg p-4 font-mono text-sm\"></div>
</div>
<script>
async function generate(){const r=await fetch('/api/uuid-generator',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({count:parseInt(document.getElementById('count').value)})});const d=await r.json();document.getElementById('result').innerHTML=d.uuids.map((u,i)=>'<div class=\"py-1 '+(i%2?'':'bg-white/50')+'\">'+u+'</div>').join('')}
function copyAll(){const uuids=[...document.getElementById('result').querySelectorAll('div')].map(d=>d.textContent).join('\\n');navigator.clipboard.writeText(uuids)}
</script>
""", "UUID Generator - Generate Random UUIDs v4 Online"),

    "markdown-preview.html": ("""
<div class=\"bg-white rounded-xl border border-gray-200 p-6 max-w-4xl mx-auto\">
    <h1 class=\"text-2xl font-bold text-gray-900 mb-2\">Markdown Preview</h1>
    <p class=\"text-gray-500 mb-4\">Write and preview Markdown in real-time.</p>
    <div class=\"grid grid-cols-2 gap-4\">
        <div><label class=\"text-sm font-medium text-gray-700 mb-1 block\">Markdown Input</label><textarea id=\"markdownInput\" rows=\"15\" class=\"w-full font-mono text-sm\"># Hello World\\n\\nThis is **bold** and *italic* text.\\n\\n- List item 1\\n- List item 2\\n\\n1. Ordered item\\n2. Ordered item\\n\\n`python\\nprint(\"Hello\")\\n`</textarea></div>
        <div><label class=\"text-sm font-medium text-gray-700 mb-1 block\">Preview</label><div id=\"preview\" class=\"border border-gray-300 rounded-lg p-4 h-[390px] overflow-y-auto prose prose-sm max-w-none\"></div></div>
    </div>
</div>
<script>
const mdInput=document.getElementById('markdownInput');const preview=document.getElementById('preview');
async function update(){const r=await fetch('/api/markdown-preview',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({data:mdInput.value})});const d=await r.json();preview.innerHTML=d.html}
mdInput.addEventListener('input',update);update();
</script>
""", "Markdown Preview - Write and Preview Markdown Online"),

    "unit-converter.html": ("""
<div class=\"bg-white rounded-xl border border-gray-200 p-6 max-w-3xl mx-auto\">
    <h1 class=\"text-2xl font-bold text-gray-900 mb-2\">Unit Converter</h1>
    <p class=\"text-gray-500 mb-4\">Convert between length, weight and temperature units.</p>
    <div class=\"grid grid-cols-2 gap-4 mb-4\">
        <label class=\"text-sm text-gray-600\">Category: <select id=\"category\" class=\"w-full\" onchange=\"updateUnits()\"><option value=\"length\">Length</option><option value=\"weight\">Weight</option><option value=\"temperature\">Temperature</option></select></label>
    </div>
    <div class=\"grid grid-cols-3 gap-4 items-end mb-4\">
        <div><label class=\"text-sm text-gray-600 block mb-1\">Value</label><input id=\"value\" type=\"number\" value=\"1\" step=\"any\"></div>
        <div><label class=\"text-sm text-gray-600 block mb-1\">From</label><select id=\"fromUnit\" class=\"w-full\"></select></div>
        <div><label class=\"text-sm text-gray-600 block mb-1\">To</label><select id=\"toUnit\" class=\"w-full\"></select></div>
    </div>
    <button class=\"px-6 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 mb-4\" onclick=\"convert()\">Convert</button>
    <div id=\"result\" class=\"bg-gray-50 rounded-lg p-4 text-lg text-center font-medium\"></div>
</div>
<script>
const units={length:{'mm':'Millimeter','cm':'Centimeter','m':'Meter','km':'Kilometer','in':'Inch','ft':'Foot','yd':'Yard','mi':'Mile'},weight:{'mg':'Milligram','g':'Gram','kg':'Kilogram','oz':'Ounce','lb':'Pound'},temperature:{'c':'Celsius','f':'Fahrenheit','k':'Kelvin'}};
function updateUnits(){const cat=document.getElementById('category').value;const u=units[cat];const f=document.getElementById('fromUnit');const t=document.getElementById('toUnit');f.innerHTML=Object.keys(u).map(k=>'<option value=\"'+k+'\"'+(k==='cm'||k==='g'||k==='c'?' selected':'')+'>'+u[k]+'</option>').join('');t.innerHTML=Object.keys(u).map(k=>'<option value=\"'+k+'\"'+(k==='m'||k==='kg'||k==='f'?' selected':'')+'>'+u[k]+'</option>').join('')}
async function convert(){const r=await fetch('/api/unit-converter',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({value:parseFloat(document.getElementById('value').value),from:document.getElementById('fromUnit').value,to:document.getElementById('toUnit').value,category:document.getElementById('category').value})});const d=await r.json();if(d.error){document.getElementById('result').textContent='Error: '+d.error;return}document.getElementById('result').textContent=document.getElementById('value').value+' '+document.getElementById('fromUnit').value+' = '+d.result+' '+document.getElementById('toUnit').value}
updateUnits();
</script>
""", "Unit Converter - Convert Length Weight and Temperature Online"),
}

for filename, (content, title) in tools.items():
    full = f'{{% extends "base.html" %}}\n{{% block title %}}{title}{{% endblock %}}\n{{% block content %}}\n{content}\n{{% endblock %}}'
    path = os.path.join(tools_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(full)
    print(f"Created {filename}")
