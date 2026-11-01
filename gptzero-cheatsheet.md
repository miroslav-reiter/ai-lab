# 🧾 GPTZero – Cheat Sheet

## 🔍 Nástroje a význam

| Nástroj | Hlavná úloha | Dôležité obmedzenie |
|---|---|---|
| Basic Scan | celkový odhad pôvodu textu | bez dôkazu autorstva |
| Advanced Scan | detailné zvýraznenie pasáží | závisí od plánu a verzie |
| AI Vision | detekcia počas prehliadania webov | len podporované stránky |
| Scan Selection | kontrola označeného textu | kontext výberu |
| Scan Page | kontrola prístupného textu stránky | môže obsahovať navigačný text |
| Word Add-in | analýza výberu v Microsoft Word | výber aspoň 250 znakov |
| Writing Report | záznam procesu úprav | nepotvrdzuje identitu autora |
| Plagiarism Check | zhody s existujúcimi zdrojmi | podobnosť ≠ plagiát |
| AI Hallucinations | kontrola citácií a tvrdení | stále treba čítať zdroj |
| Possible AI Paraphrasing | predbežné vyhodnotenie úprav AI textu | klasifikačný odhad (beta) |

## 🪟 Microsoft Word

| Krok | Umiestnenie |
|---|---|
| Inštalácia | Home → Add-ins → More Add-ins |
| Vyhľadanie doplnku | GPTZero → Add |
| Bočný panel | Home → Show GPTZero |
| Analýza | označiť text → Get Results |

## ☁️ Google Dokumenty

| Krok | Umiestnenie |
|---|---|
| Rozšírenie | Chrome / Edge / Firefox |
| Prihlásenie | panel GPTZero |
| Writing Report | Google Docs s právom editácie → Watch Writing Report |
| Úpravy | postupné písanie, vymazávanie, vloženie textu |
| Zdieľanie | Share v Writing Report – preveriť práva |

## 🌐 Sociálne siete

| Prostredie | Príklad použitia |
|---|---|
| LinkedIn | dlhší odborný text |
| Facebook | príspevok vs. krátky komentár |
| X / Reddit | dlhší príspevok |
| YouTube | komentáre, nie video |
| Medium / Substack | publikované články |
| Webové blogy | Scan Selection / Scan Page |

## 📚 Plagiátorstvo a vedecké texty

| Pojem | Správny výklad |
|---|---|
| AI-generated | pravdepodobný pôvod časti alebo celého textu |
| Human | odhad ľudského pôvodu |
| Mixed | jazykové znaky viacerých pôvodov |
| Confidence | istota klasifikátora |
| Similarity | textová zhoda s dostupnými zdrojmi |
| Citation check | overenie existencie a presnosti citácií |
| Source support | či konkrétny zdroj podporuje tvrdenie |
| False positive | ľudský text nesprávne označený ako AI |
| False negative | AI text nesprávne označený ako ľudský |

## ⚙️ Lokálne vyhodnotenie tréningových výsledkov

**Windows PowerShell:**

```powershell
py -3 scripts/vyhodnotenie-gptzero.py --input data/vysledky-vzor.csv
```

**Ubuntu, Kali Linux a macOS:**

```bash
python3 scripts/vyhodnotenie-gptzero.py --input data/vysledky-vzor.csv
```

Tento skript sa **nepripája na GPTZero**, neskenuje text a neurčuje autorstvo. Len počíta zhodu medzi manuálne zaznamenanou klasifikáciou a skutočným známym pôvodom.

## 🔒 Najdôležitejšie upozornenia

- Výsledok AI detektora nie je dôkaz plagiátorstva.
- Štítok Human nedokazuje, že pri tvorbe nebola použitá AI.
- Paste event nie je dôkaz podvodu.
- Dlhší text býva vhodnejší než krátky komentár.
- Cudzie dôverné dokumenty neskenujeme bez oprávnenia.
- Bezplatné limity a funkcie sa môžu meniť, overíme ich pred školením.
