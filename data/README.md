# 🧪 Tréningové dáta pre GPTZero

Cieľom je zabezpečiť **známy pôvod každej vzorky** a viesť reprodukovateľný protokol bez vymyslených výsledkov.

| Súbor | Čo obsahuje |
|---|---|
| [text-ai-vzor.txt](text-ai-vzor.txt) | syntetický článok vytvorený AI asistentom |
| [socialne-prispevky.md](socialne-prispevky.md) | syntetické krátke a dlhšie sociálne príspevky |
| [citacie-kontrola.md](citacie-kontrola.md) | existujúci aj úmyselne fiktívny zdroj |
| [vysledky-vzor.csv](vysledky-vzor.csv) | šablónu na zapisovanie skutočných výsledkov GPTZero |

## 🧠 Ako pripraviť férové vzorky

**1. AI text:** Použijeme `text-ai-vzor.txt` a zaznamenáme, že vznikol s pomocou AI asistenta.

**2. Ľudský text:** Účastník **sám** napíše vlastný text bez AI pomoci a zdokumentuje pôvod. V repozitári ho zámerne nenahrádzame AI generovanou „ľudskou“ vzorkou.

**3. Mixed text:** Spojíme aspoň jeden skutočne vlastný ľudský odsek s AI odsekom zo vzoru. Pôvod oboch pasáží si uložíme oddelene.

**4. Kontrola podobnosti:** Pracujeme iba s vlastnými alebo riadne povolenými materiálmi. Vymyslené bibliografické záznamy sú výslovne označené ako fiktívne.

## 📊 Záznam výsledkov

V `vysledky-vzor.csv` vyplníme stĺpce:
- `predikcia` – jedna z hodnôt `human`, `ai`, `mixed`, `uncertain`;
- `confidence` – voliteľne presná hodnota z rozhrania, bez preinterpretovania;
- `rezim` – Basic alebo Advanced;
- `poznamka` – napríklad „text príliš krátky“ alebo „zmenený jazyk“.

Skript správne rozpoznáva aj rozdiel medzi nevyplneným výsledkom a výsledkom Uncertain.

### Windows PowerShell

```powershell
py -3 scripts/vyhodnotenie-gptzero.py --input data/vysledky-vzor.csv
```

### Ubuntu a Kali Linux

```bash
python3 scripts/vyhodnotenie-gptzero.py --input data/vysledky-vzor.csv
```

**Vysvetlenie:** Skript neodosiela požiadavky na internet, nečíta dokumenty mimo CSV a nedeteguje AI. Počíta len štatistiky výsledkov, ktoré ručne zadáme po skutočnom skenovaní.

## Rozšírená sada GPTZero

V priečinku [gptzero-testovacie-texty/](gptzero-testovacie-texty/README.md) nájdeme 10 ďalších AI ukážok, vysvetlenie testovania, šablónu na nezávisle napísaný ľudský text a postup vytvorenia Mixed vzorky.
