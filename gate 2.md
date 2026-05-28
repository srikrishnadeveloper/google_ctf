  # Gate 2 Walkthrough: "The Quantum Scroll"

### 1. Challenge Overview
* **Target Website:** `https://gates-of-shell.vercel.app/`
* **Current Gate:** Gate 2 — “The Quantum Scroll”
* **Clue provided:** 
  > *"My probability matrices indicate it is not merely a document, but a weaponized archive... Focus your extraction efforts on translating the fractured geometry and combine it with the surviving fragments to reveal the truth."*
  > *"the degradation is asymmetric."*
  > *"cages, lines, and dots."*

This is a classic visual cryptography challenge based on the **Pigpen Cipher** (also known as the Masonic Cipher), combined with a **180-degree rotation (both horizontal and vertical reversal)** and **leetspeak substitution**.

---

### 2. Systematic Forensic Analysis

#### **A. Spatial Orientation & Reading Order**
Looking at the scroll, the text is split into two lines:
* **Line 1 (Top):** Begins with a closing curly bracket `}` and ends with an opening curly bracket `{`.
* **Line 2 (Bottom):** Contains 6 geometric symbols.

In standard English and standard CTF flag formats, flags begin with `iFound{` and end with `}`. 
The presence of `}` at the start of Line 1 and `{` at the end of Line 1, along with a 6-letter word on Line 2, indicates that **the entire text has been rotated 180 degrees (mirrored vertically and horizontally)**.

To decode, we must:
1. Read the lines from bottom to top (Line 2 first, then Line 1).
2. Read each line from right to left (reversed).

---

### 3. Decrypting Line 2: The Prefix (`iFound`)

Reading Line 2 from **right to left**:

| Order (Right to Left) | Visual Symbol | Pigpen Grid Position | Decoded Letter |
| :---: | :---: | :---: | :---: |
| 1 | `Г` | Bottom-Right (No Dot) | **I** |
| 2 | `[` | Middle-Right (No Dot) | **F** |
| 3 | `[•` (looks like `E•`) | Middle-Right (With Dot) | **O** |
| 4 | `<` | X-Grid Right (No Dot) | **U** |
| 5 | `⬜•` | Center (With Dot) | **N** |
| 6 | `]` | Middle-Left (No Dot) | **D** |

* **Result of Line 2 (Reversed):** `IFOUND` (representing `iFound`).

---

### 4. Decrypting Line 1: The Payload (`{5cr0ll_15_3mpty}`)

Reading Line 1 from **right to left**:

| Order (Right to Left) | Visual Symbol | Translation / Grid Position | Decoded Character |
| :---: | :---: | :---: | :---: |
| 1 | `{` | Literal Character | **`{`** |
| 2 | `5` | Literal Character (Leetspeak for `S`) | **`5`** (S) |
| 3 | `└` (looks like `L`) | Top-Right (No Dot) | **`C`** |
| 4 | `┌•` (looks like `F•`) | Bottom-Right (With Dot) | **`R`** |
| 5 | `0` | Literal Character (Leetspeak for `O`) | **`0`** (O) |
| 6 | `└•` (looks like `L•`) | Top-Right (With Dot) | **`L`** |
| 7 | `└•` (looks like `L•`) | Top-Right (With Dot) | **`L`** |
| 8 | `_` | Literal Character | **`_`** |
| 9 | `1` | Literal Character (Leetspeak for `I`) | **`1`** (I) |
| 10 | `5` | Literal Character (Leetspeak for `S`) | **`5`** (S) |
| 11 | `_` | Literal Character | **`_`** |
| 12 | `3` | Literal Character (Leetspeak for `E`) | **`3`** (E) |
| 13 | `⊐•` (looks like `]•`) | Middle-Left (With Dot) | **`M`** |
| 14 | `┐•` (looks like `7•`) | Bottom-Left (With Dot) | **`P`** |
| 15 | `>` | X-Grid Left (No Dot) | **`T`** |
| 16 | `<•` | X-Grid Right (With Dot) | **`Y`** |
| 17 | `}` | Literal Character | **`}`** |

* **Result of Line 1 (Reversed):** `{5cr0ll_15_3mpty}` (interprets to `{scroll_is_empty}`).

---

### 5. Final Reconstruction & Verification

Combining the prefix and payload in their corrected, reconstructed order:

$$\text{Line 2 (Reversed)} + \text{Line 1 (Reversed)} = \text{iFound} + \text{\{5cr0ll\_15\_3mpty\}}$$

* **Final Flag:** `iFound{5cr0ll_15_3mpty}`
* **Confidence Level:** 100% (Perfect typographic and geometric alignment)
