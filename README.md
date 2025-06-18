# 🕷️ Web Scraper for Web Reconnaissance

> This is a custom-built, CLI-based web scraping and reconnaissance toolkit written in Python and Bash. It automates the discovery of valid endpoints via fuzzing, downloads accessible pages, and extracts valuable metadata for use in web enumeration > > and OSINT tasks.
---

## 📁 Project Structure
- ├── FUZZ_check.py # Fuzzes the base URL with wordlist
- ├── html_download.sh # Downloads each valid endpoint as HTML
- ├── data_scrap.py # Parses downloaded HTML to extract useful data
- ├── main.sh # Main orchestrator script
- ├── FUZZ.txt # Wordlist used for fuzzing
- └── output_dir/ # Stores downloaded HTML pages (auto-created)


---

## ⚙️ Features

- ✅ URL fuzzing using a wordlist  
- ✅ Valid endpoint detection (HTTP 200)  
- ✅ HTML downloading via `curl`  
- ✅ Metadata extraction using BeautifulSoup:
  - Page title
  - Meta tags (name, content)
  - Stylesheet links
  - Hidden input fields
  - Anchor tags

---

## 🚀 How to Run

```bash
chmod +x main.sh
./main.sh <url>
```
Make sure FUZZ.txt contains your wordlist before running.
```bash
./main.sh http://example.com
```

## 🧠 Dependencies
- Python 3.x
- requests
- beautifulsoup4
- Bash shell with curl
- Linux or WSL recommended
  ```bash
  pip install requests beautifulsoup4
  ```
  
## 👨‍💻 Author
  **Raihan Shamnad — Cybersecurity enthusiast and penetration tester-in-training.**

## 🛡️ Disclaimer
> This tool is intended for educational and authorized testing purposes only. Do not use it on domains you do not have permission to audit
