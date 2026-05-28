













# Gate 1 Walkthrough: "The Presentation Layer"

### 1. Challenge Overview
* **Target Website:** `https://gates-of-shell.vercel.app/`
* **Linked Domain (Gaia's Domain):** `https://gdg-on-campus-ssn.github.io/`
* **Clue provided:** *"To the oblivious observer, this node functions normally. However, those who understand the architecture know that every site has a subconscious—a place where diagnostic logs and background operations are recorded out of sight. You must visit this domain, but do not be distracted by the rendered illusion. Look behind the curtain. Inspect the foundation. Observe. Intercept. Decode."*

The clue heavily emphasizes looking behind the standard visual rendering to check the site's "subconscious"—commonly referring to console logs, network traffic, comments, or cookies.

---

### 2. Systematic Reconnaissance
An automated, deep frontend analysis was executed on Gaia's Domain (`https://gdg-on-campus-ssn.github.io/`) to inspect its source code, assets, robots.txt, sitemaps, and runtime logs.

#### **A. Checking `robots.txt` & `sitemap.xml`**
Navigating to `https://gdg-on-campus-ssn.github.io/robots.txt` returned the standard:
```text
User-agent: *
Disallow:
Allow: /
Sitemap: https://gdg-on-campus-ssn.github.io/sitemap.xml
```
Checking the sitemap showed only the standard blog routes and event posts. No hidden administrative backends or hidden pages were listed here.

#### **B. Developer Console Monitoring ("The Subconscious")**
When the browser loads `https://gdg-on-campus-ssn.github.io/`, a script inside the DOM is automatically evaluated. Monitoring the **Developer Console** logs intercepted the following print statement:

> **Console Log:**
> ```text
> Greetings, seeker of forbidden bytes.
> 
> The First Gate has chosen to speak in numbers pretending to be words.
> 
> 69 46 6F 75 6E 64 7B 31 5F 34 6D 5F 35 34 6E 33 7D
> 
> Fear not, Player. They are only pretending to be intimidating.
> 
> Let ASCII and hexadecimal guide you through this gate.
> ```

---

### 3. Hexadecimal & ASCII Decoding Analysis
The extracted string of hexadecimal numbers representing the flag is:
`69 46 6F 75 6E 64 7B 31 5F 34 6D 5F 35 34 6E 33 7D`

Converting each hex byte to its equivalent ASCII character:

| Hex Byte | Decimal Value | ASCII Character |
| :---: | :---: | :---: |
| `69` | 105 | **`i`** |
| `46` | 70 | **`F`** |
| `6F` | 111 | **`o`** |
| `75` | 117 | **`u`** |
| `6E` | 110 | **`n`** |
| `64` | 100 | **`d`** |
| `7B` | 123 | **`{`** |
| `31` | 49 | **`1`** |
| `5F` | 95 | **`_`** |
| `34` | 52 | **`4`** |
| `6D` | 109 | **`m`** |
| `5F` | 95 | **`_`** |
| `35` | 53 | **`5`** |
| `34` | 52 | **`4`** |
| `6E` | 110 | **`n`** |
| `33` | 51 | **`3`** |
| `7D` | 125 | **`}`** |

Combining the converted characters yields the decoded flag:
`iFound{1_4m_54n3}` *(translating to "I found {I am sane}")*

---

### 4. Findings & Conclusion
* **Extracted Flag:** `iFound{1_4m_54n3}`
* **Method of Discovery:** Runtime Developer Console logging interception of the landing page on the linked domain.
* **Cipher Type:** Hexadecimal representation of ASCII characters.

No automated submissions have been performed. You are ready to manually copy this flag and submit it in the input field of Gate 1 on `https://gates-of-shell.vercel.app/` to unlock Gate 2!