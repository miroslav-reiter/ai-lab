# 🧪 GPTZero – testovacie texty so známym pôvodom

Tento priečinok obsahuje **10 textových vzoriek vytvorených pomocou generatívnej AI** a metodiku ich testovania. Sada slúži na predvedenie funkcií GPTZero na školeniach, pri testovaní rôznych textových štýlov a pri porovnávaní výsledkov detekcie.

**Dôležité:** Všetky ukážky označené prefixom `ai-` majú známy pôvod **AI**. Nesmú sa prezentovať ako autenticky ľudské texty. Výsledok GPTZero nie je známy vopred a na týchto súboroch nebol vykonaný živý sken.

## 📄 Microsoft Word – DOCX verzie všetkých textov

Všetkých 10 testovacích vzoriek je dostupných aj ako **samostatné Word dokumenty (.docx)**. Text zostal rovnaký ako v pôvodných TXT súboroch, bez pridaného nadpisu alebo popisu v tele dokumentu. Takto môžeme porovnať výsledok GPTZero pre TXT a DOCX bez obsahovej zmeny.

- **[Stiahnuť celý balík 10 DOCX súborov (ZIP)](gptzero-testovacie-texty-word.zip)**
- **[Otvoriť priečinok so samostatnými Word dokumentmi](word/)**

| Word dokument | Téma |
|---|---|
| [01-ai-odborny-it-kyberbezpecnost.docx](word/01-ai-odborny-it-kyberbezpecnost.docx) | Kybernetická bezpečnosť |
| [02-ai-akademicky-text-vzdelavanie.docx](word/02-ai-akademicky-text-vzdelavanie.docx) | Akademický pedagogický text |
| [03-ai-seo-wordpress-blog.docx](word/03-ai-seo-wordpress-blog.docx) | SEO a WordPress |
| [04-ai-marketingovy-prispevok.docx](word/04-ai-marketingovy-prispevok.docx) | Marketingový text |
| [05-ai-uradny-formalny-text.docx](word/05-ai-uradny-formalny-text.docx) | Formálny úradný text |
| [06-ai-literarny-pribeh.docx](word/06-ai-literarny-pribeh.docx) | Kreatívne písanie |
| [07-ai-produktovy-popis.docx](word/07-ai-produktovy-popis.docx) | Produktový opis |
| [08-ai-popularizacny-vedecky.docx](word/08-ai-popularizacny-vedecky.docx) | Populárno-vedecký text |
| [09-ai-english-training.docx](word/09-ai-english-training.docx) | Anglický odborný text |
| [10-ai-kratky-komentar.docx](word/10-ai-kratky-komentar.docx) | Krátky komentár |

Na opätovné vytvorenie Word dokumentov z originálnych TXT súborov slúži skript [generuj-gptzero-docx.py](../../scripts/generuj-gptzero-docx.py).

## 📁 Zoznam vzoriek

| Súbor | Žáner | Jazyk | Počet slov | Skutočný pôvod |
|---|---|---|---:|---|
| [01-ai-odborny-it-kyberbezpecnost.txt](01-ai-odborny-it-kyberbezpecnost.txt) | Odborný IT text | sk | 321 | AI |
| [02-ai-akademicky-text-vzdelavanie.txt](02-ai-akademicky-text-vzdelavanie.txt) | Akademický text | sk | 355 | AI |
| [03-ai-seo-wordpress-blog.txt](03-ai-seo-wordpress-blog.txt) | SEO článok | sk | 341 | AI |
| [04-ai-marketingovy-prispevok.txt](04-ai-marketingovy-prispevok.txt) | Marketingový príspevok | sk | 306 | AI |
| [05-ai-uradny-formalny-text.txt](05-ai-uradny-formalny-text.txt) | Úradný text | sk | 345 | AI |
| [06-ai-literarny-pribeh.txt](06-ai-literarny-pribeh.txt) | Literárny príbeh | sk | 353 | AI |
| [07-ai-produktovy-popis.txt](07-ai-produktovy-popis.txt) | Produktový opis | sk | 317 | AI |
| [08-ai-popularizacny-vedecky.txt](08-ai-popularizacny-vedecky.txt) | Vedecký popularizačný text | sk | 344 | AI |
| [09-ai-english-training.txt](09-ai-english-training.txt) | English training text | en | 426 | AI |
| [10-ai-kratky-komentar.txt](10-ai-kratky-komentar.txt) | Krátky komentár | sk | 29 | AI |

Prehľad v strojovo čitateľnej forme obsahuje [metadata-vzoriek.csv](metadata-vzoriek.csv).

## 🎬 Ako používať jednotlivé texty vo videu

### **1. Základná AI detekcia**

1. Otvoríme [GPTZero](https://gptzero.me/).
2. Vyberieme prvý text, napríklad `01-ai-odborny-it-kyberbezpecnost.txt`.
3. Skopírujeme **iba obsah TXT** a vložíme ho do GPTZero. Neskopírujeme názov súboru s označením `ai-`.
4. Spustíme Basic Scan alebo dostupný Advanced Scan.
5. Pozrieme klasifikáciu Human / AI / Mixed a stupeň istoty.
6. Skutočný výsledok zapíšeme do [../vysledky-vzor.csv](../vysledky-vzor.csv).

**Čo to robí:** Porovnávame predikciu so známym AI pôvodom. Nízka istota alebo výsledok Human je súčasť experimentu, nie dôvod prepísať označenie pôvodu.

### **2. Slovenský odborný vs. tvorivý text**

Porovnáme vzorky `01`, `02`, `06` a `08`. Všetky sú AI texty, ale používajú odlišnú štylistiku. Vyhodnotíme, či sa výsledky líšia podľa žánru.

### **3. Slovenčina vs. angličtina**

Otestujeme slovenský odborný článok a anglickú vzorku `09`. Témy nie sú totožné, preto rozdiel výsledkov **nemôžeme pripísať výlučne jazyku**. Pre riadny jazykový experiment treba pripraviť obsahovo porovnateľné texty.

### **4. Krátky komentár**

Vzor `10` má 29 slov a **212 znakov**. Je zámerne krátky a nemusí spĺňať minimálny rozsah jednotlivých režimov. Vo Word Add-ine je limit najmenej 250 znakov. <https://support.gptzero.me/articles/8893155578-how-can-i-use-the-microsoft-word-add-in-to-check-for-ai>

### **5. Microsoft Word**

Otvoríme Word, vytvoríme prázdny dokument a vložíme obsah ľubovoľnej dlhej TXT vzorky. Uložíme ako DOCX a pomocou **Home → Show GPTZero → Get Results** vykonáme kontrolu vybraného textu.

### **6. Google Dokumenty a Writing Replay**

Na Google Dokumenty potrebujeme rozlíšiť *pôvod textu* od *udalostí editovania*. Vloženie celého AI vzoru zaznamená paste, ale hromadné vloženie samo osebe nepreukazuje plagiátorstvo ani AI pôvod.

### **7. Ľudská kontrolná vzorka – treba ju reálne napísať**

Použijeme [vzor-ludskeho-textu-na-doplnenie.md](vzor-ludskeho-textu-na-doplnenie.md). Účastník **nezávisle od AI napíše 300 až 450 slov** na podobnú tému. Bez známeho a zdokumentovaného spôsobu tvorby nemáme platnú Human vzorku.

### **8. Zmiešaný text – treba spojiť reálne ľudský a AI text**

Podľa [mixed-vzorka-postup.md](mixed-vzorka-postup.md) spojíme autenticky ľudský text od účastníka s pasážou z existujúcej AI vzorky. Necháme si presnú mapu hraníc oboch častí.

## 📊 Spracovanie výsledkov

Ručne zapíšeme `predikcia` do `data/vysledky-vzor.csv` v koreňovom repozitári. Základný lokálny audit:

```bash
python3 scripts/vyhodnotenie-gptzero.py --input data/vysledky-vzor.csv
```

Skript **neskenuje texty** a nepoužíva GPTZero API. Zobrazuje iba porovnanie výsledkov, ktoré zadáme po skutočnom teste.

## 🔒 Limity a zásady

- AI skóre nie je presný percentuálny podiel skutočne AI napísaných viet.
- Výsledok Human pri AI vzorke je potenciálnym falošne negatívnym výsledkom, nie zmenou jej pôvodu.
- Výsledok AI pri nezávisle vytvorenej ľudskej vzorke predstavuje potenciálne falošné pozitívum.
- Krátke texty, šablónový jazyk a rôzne jazyky môžu ovplyvniť spoľahlivosť.
- Tieto syntetické materiály sú verejné. Nenahrávame do nich osobné alebo neverejné dokumenty.
- Nevykonávame disciplinárne ani právne závery iba na základe automatickej detekcie.

## 📚 Oficiálna dokumentácia

- https://support.gptzero.me/articles/4965048546-How-do-I-interpret-a-GPTZero-result
- https://support.gptzero.me/articles/1787085022-what-are-the-limitations-of-gptzero-s-ai-classifier
- https://support.gptzero.me/articles/8893155578-how-can-i-use-the-microsoft-word-add-in-to-check-for-ai
