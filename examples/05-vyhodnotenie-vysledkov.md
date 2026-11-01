# 📊 Laboratórne cvičenie 5 – Vyhodnotenie výsledkov GPTZero

**Cieľ:** Z porovnateľných vzoriek so známym pôvodom vytvoriť jednoduchý protokol.

**Vstup:** `data/vysledky-vzor.csv`.

**Postup:**
1. Skenujeme kontrolované vzorky.
2. V CSV vyplníme `predikcia` hodnotami `human`, `ai`, `mixed` alebo `uncertain`.
3. Spustíme lokálny skript.

**Windows PowerShell:**

```powershell
py -3 scripts/vyhodnotenie-gptzero.py --input data/vysledky-vzor.csv
```

**Ubuntu / Kali Linux:**

```bash
python3 scripts/vyhodnotenie-gptzero.py --input data/vysledky-vzor.csv
```

**Čo to robí:** Spočíta pozorovanú zhodu, false positives a false negatives a samostatne eviduje Mixed a Uncertain.

**Vysvetlenie:** Skript nevykonáva AI detekciu. Na základe niekoľkých vzoriek nedokazujeme univerzálnu presnosť služby.

**Očakávaný výstup:** Matica klasifikácií a slovne uvedené obmedzenia experimentu.
