# Altair's Tools

A collection of 30+ free online utility tools for developers, designers, and photographers.

## Features

- 30+ tools across 5 categories: Text, Developer, Image, Generator, Utility
- Unique tools: Color Transfer, Pixel Art Generator, ASCII Art Generator, Film Look Presets
- Fully bilingual (English / Chinese) with auto-detection
- All tools run client-side in the browser - no uploads to server
- Mobile responsive

## Categories

| Category | Tools |
|----------|-------|
| Text | Word Counter, Text Case Converter, Lorem Ipsum, HTML Entity, Text Diff |
| Developer | JSON Formatter, Base64, URL Encoder, Hash Generator, Regex Tester, CSV↔JSON, Border Radius |
| Image | Color Converter, Color Picker, Image Filters, Image Crop, Image Compare, Image Resize, Palette Generator, Color Transfer, Pixel Art, ASCII Art, Film Presets |
| Generator | UUID Generator, Password Generator, QR Code Generator |
| Utility | Unit Converter, QR Code Reader, Markdown Preview, Batch Palette Converter |

## Deployment

- Hosted on Render (free tier)
- Auto-deploys from GitHub master branch
- Python Flask + Tailwind CSS

## How to Add a New Tool

1. Add tool ID to `TOOLS` list in `app/routes.py`
2. Create template in `app/templates/tools/`
3. Add translation to `app/templates/base.html`
4. Add category in `app/templates/index.html`
5. Push to GitHub - Render auto-deploys

## Guestbook

Messages are stored as GitHub Issues. Submit via the Contact page.

## Local Development

```
cd outputs/toolsite
pip install flask gunicorn markdown pillow qrcode
python run.py
```
