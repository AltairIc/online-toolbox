
from flask import Blueprint, render_template, request, jsonify

main = Blueprint("main", __name__)

TOOLS = [
    {"id": "word-counter", "cat": "text", "name": "Word Counter", "desc": "Count words, characters, sentences and paragraphs", "icon": "file-text"},
    {"id": "text-case", "cat": "text", "name": "Text Case Converter", "desc": "Convert text between uppercase, lowercase, title case and more", "icon": "type"},
    {"id": "json-formatter", "cat": "dev", "name": "JSON Formatter", "desc": "Format, validate and beautify JSON data", "icon": "braces"},
    {"id": "base64", "cat": "dev", "name": "Base64 Encoder/Decoder", "desc": "Encode or decode Base64 strings instantly", "icon": "lock"},
    {"id": "url-encoder", "cat": "dev", "name": "URL Encoder/Decoder", "desc": "Encode or decode URLs for web use", "icon": "link"},
    {"id": "hash-generator", "cat": "dev", "name": "Hash Generator", "desc": "Generate MD5, SHA1, SHA256, SHA512 hashes", "icon": "fingerprint"},
    {"id": "text-diff", "cat": "text", "name": "Text Diff Checker", "desc": "Compare two texts and highlight differences", "icon": "git-compare"},
    {"id": "color-converter", "cat": "image", "name": "Color Converter", "desc": "Convert colors between HEX, RGB and HSL formats", "icon": "palette"},
    {"id": "uuid-generator", "cat": "gen", "name": "UUID Generator", "desc": "Generate random UUIDs (v4) in bulk", "icon": "shuffle"},
    {"id": "html-entity", "cat": "text", "name": "HTML Entity Converter", "desc": "Escape or unescape HTML entities", "icon": "code"},
    {"id": "markdown-preview", "cat": "util", "name": "Markdown Preview", "desc": "Write and preview Markdown in real-time", "icon": "markdown"},
    {"id": "lorem-ipsum", "cat": "text", "name": "Lorem Ipsum Generator", "desc": "Generate placeholder text for designs and layouts", "icon": "text"},
    {"id": "regex-tester", "cat": "dev", "name": "Regex Tester", "desc": "Test regular expressions with real-time matching", "icon": "search"},
    {"id": "password-generator", "cat": "gen", "name": "Password Generator", "desc": "Generate strong random passwords", "icon": "key"},
    {"id": "unit-converter", "cat": "util", "name": "Unit Converter", "desc": "Convert between length, weight, temperature and more", "icon": "ruler"},
    {'id': 'qr-generator', 'name': 'QR Code Generator', 'desc': 'Generate QR codes from text, URLs and more', 'icon': 'qr-code'},
    {'id': 'qr-reader', 'name': 'QR Code Reader', 'desc': 'Decode and read QR codes from images', 'icon': 'camera'},
    {"id": "color-picker", "cat": "image", "name": "Color Picker from Image", "desc": "Pick colors from images, get RGB/HEX values, and build color palettes for photo editing", "icon": "droplet"},
    {"id": "image-filters", "cat": "image", "name": "Image Filters", "desc": "Apply filters like grayscale, sepia, blur, brightness and contrast to images", "icon": "image"},
    {"id": "image-crop", "cat": "image", "name": "Image Crop", "desc": "Crop images with custom or preset aspect ratios", "icon": "crop"},
    {"id": "image-compare", "cat": "image", "name": "Image Compare", "desc": "Compare two images side by side with a draggable slider", "icon": "git-compare"},
    {"id": "image-resize", "cat": "image", "name": "Image Resize", "desc": "Resize images and convert between PNG, JPG and WEBP formats", "icon": "maximize"},
    {"id": "palette-generator", "name": "Color Palette Generator", "desc": "Generate complementary, analogous, triadic and more color schemes from any base color", "cat": "image"}]


@main.route("/ads.txt")
def ads_txt():
    return "google.com, pub-4613836349381729, DIRECT, f08c47fec0942fa0\n", 200, {"Content-Type": "text/plain"}
@main.route("/")
def index():
    return render_template("index.html", tools=TOOLS)

@main.route("/tool/<tool_id>")
def tool_page(tool_id):
    tool = next((t for t in TOOLS if t["id"] == tool_id), None)
    if not tool:
        return render_template("index.html", tools=TOOLS)
    return render_template(f"tools/{tool_id}.html", tool=tool)

@main.route("/api/word-counter", methods=["POST"])
def api_word_counter():
    text = request.json.get("text", "")
    words = len(re.findall(r"\b\w+\b", text))
    chars = len(text)
    chars_no_space = len(text.replace(" ", ""))
    sentences = len(re.findall(r"[.!?]+", text)) or (1 if text.strip() else 0)
    paragraphs = len([p for p in text.split("\n") if p.strip()]) or 0
    return jsonify(words=words, chars=chars, chars_no_space=chars_no_space, sentences=sentences, paragraphs=paragraphs)

@main.route("/api/text-case", methods=["POST"])
def api_text_case():
    text = request.json.get("text", "")
    case = request.json.get("case", "upper")
    if case == "upper": result = text.upper()
    elif case == "lower": result = text.lower()
    elif case == "title": result = text.title()
    elif case == "sentence": result = ". ".join(s.capitalize() for s in text.split(". "))
    elif case == "camel": result = re.sub(r"[-_\s]+(.)", lambda m: m.group(1).upper(), text.strip().lower())
    elif case == "snake": result = re.sub(r"[-\s]+", "_", re.sub(r"([A-Z])", r"_\1", text).strip().lower()).lstrip("_")
    elif case == "kebab": result = re.sub(r"[_\s]+", "-", text.strip().lower())
    else: result = text
    return jsonify(result=result)

@main.route("/api/json-formatter", methods=["POST"])
def api_json_formatter():
    data = request.json.get("data", "")
    indent = int(request.json.get("indent", 2))
    try:
        parsed = json.loads(data)
        result = json.dumps(parsed, indent=indent, sort_keys=True, ensure_ascii=False)
        return jsonify(result=result, valid=True)
    except json.JSONDecodeError as e:
        return jsonify(result=str(e), valid=False)

@main.route("/api/base64", methods=["POST"])
def api_base64():
    data = request.json.get("data", "")
    mode = request.json.get("mode", "encode")
    try:
        if mode == "encode":
            result = base64.b64encode(data.encode()).decode()
        else:
            result = base64.b64decode(data).decode("utf-8", errors="replace")
        return jsonify(result=result, error=None)
    except Exception as e:
        return jsonify(result="", error=str(e))

@main.route("/api/url-encoder", methods=["POST"])
def api_url_encoder():
    data = request.json.get("data", "")
    mode = request.json.get("mode", "encode")
    try:
        if mode == "encode":
            result = urllib.parse.quote(data)
        else:
            result = urllib.parse.unquote(data)
        return jsonify(result=result, error=None)
    except Exception as e:
        return jsonify(result="", error=str(e))

@main.route("/api/hash-generator", methods=["POST"])
def api_hash_generator():
    data = request.json.get("data", "").encode()
    return jsonify(
        md5=hashlib.md5(data).hexdigest(),
        sha1=hashlib.sha1(data).hexdigest(),
        sha256=hashlib.sha256(data).hexdigest(),
        sha512=hashlib.sha512(data).hexdigest(),
    )

@main.route("/api/text-diff", methods=["POST"])
def api_text_diff():
    text1 = request.json.get("text1", "")
    text2 = request.json.get("text2", "")
    lines1, lines2 = text1.split("\n"), text2.split("\n")
    import difflib
    diff = list(difflib.unified_diff(lines1, lines2, lineterm=""))
    return jsonify(diff="\n".join(diff))

@main.route("/api/color-converter", methods=["POST"])
def api_color_converter():
    color = request.json.get("color", "").strip()
    from_to = request.json.get("from_to", "hex_to_rgb")
    try:
        if from_to == "hex_to_rgb":
            c = color.lstrip("#")
            r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
            return jsonify(r=r, g=g, b=b, hex=color, rgb=f"rgb({r},{g},{b})")
        elif from_to == "rgb_to_hex":
            m = re.match(r"rgb\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", color)
            if m:
                r, g, b = int(m[1]), int(m[2]), int(m[3])
                return jsonify(r=r, g=g, b=b, hex=f"#{r:02x}{g:02x}{b:02x}", rgb=color)
        return jsonify(error="Invalid color format")
    except Exception as e:
        return jsonify(error=str(e))

@main.route("/api/uuid-generator", methods=["POST"])
def api_uuid_generator():
    import uuid
    count = min(int(request.json.get("count", 1)), 100)
    uuids = [str(uuid.uuid4()) for _ in range(count)]
    return jsonify(uuids=uuids)

@main.route("/api/html-entity", methods=["POST"])
def api_html_entity():
    data = request.json.get("data", "")
    mode = request.json.get("mode", "encode")
    import html
    if mode == "encode":
        result = html.escape(data)
    else:
        result = html.unescape(data)
    return jsonify(result=result)

@main.route("/api/markdown-preview", methods=["POST"])
def api_markdown_preview():
    data = request.json.get("data", "")
    import markdown
    result = markdown.markdown(data, extensions=["fenced_code", "tables", "codehilite"])
    return jsonify(html=result)

@main.route("/api/lorem-ipsum", methods=["POST"])
def api_lorem_ipsum():
    count = min(int(request.json.get("count", 5)), 100)
    unit = request.json.get("unit", "paragraphs")
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    words = lorem.split()
    if unit == "words":
        result = " ".join(words[:count])
    elif unit == "sentences":
        result = ". ".join([" ".join(words[i*7:(i+1)*7]) for i in range(count)])
    else:
        result = "\n\n".join([lorem for _ in range(count)])
    return jsonify(result=result)

@main.route("/api/regex-tester", methods=["POST"])
def api_regex_tester():
    pattern = request.json.get("pattern", "")
    text = request.json.get("text", "")
    try:
        matches = list(re.finditer(pattern, text))
        results = [{"text": m.group(), "start": m.start(), "end": m.end()} for m in matches]
        return jsonify(matches=results, count=len(results), error=None)
    except re.error as e:
        return jsonify(matches=[], count=0, error=str(e))

@main.route("/api/password-generator", methods=["POST"])
def api_password_generator():
    import secrets, string
    length = min(int(request.json.get("length", 16)), 128)
    use_upper = request.json.get("use_upper", True)
    use_lower = request.json.get("use_lower", True)
    use_digits = request.json.get("use_digits", True)
    use_symbols = request.json.get("use_symbols", True)
    chars = ""
    if use_upper: chars += string.ascii_uppercase
    if use_lower: chars += string.ascii_lowercase
    if use_digits: chars += string.digits
    if use_symbols: chars += string.punctuation
    if not chars: chars = string.ascii_letters
    password = "".join(secrets.choice(chars) for _ in range(length))
    return jsonify(password=password)

@main.route("/api/unit-converter", methods=["POST"])

@main.route('/api/qr-generator', methods=['POST'])
def api_qr_generator():
    import qrcode, io, base64
    data = request.json.get('data', '')
    size = int(request.json.get('size', 200))
    if not data:
        return jsonify(error='No data provided')
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img = img.resize((size, size))
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    b64 = base64.b64encode(buf.getvalue()).decode()
    return jsonify(image='data:image/png;base64,' + b64, error=None)


