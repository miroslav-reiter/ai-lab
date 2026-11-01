# 🧠 Detekcia AI – princípy, presnosť a interpretácia

Táto kapitola vysvetľuje rozdiel medzi **štatistickým odhadom**, **procesným dôkazom**, **kontrolou podobnosti** a **overovaním zdrojov**.

## 📌 Čo detektor v skutočnosti robí

GPTZero analyzuje text pomocou modelov naučených na vzorkách ľudského a AI generovaného textu. Vyhodnocuje jazykové charakteristiky celého textu a pri podporovaných režimoch aj jeho častí. Nečíta históriu tvorby priamo z písmen ani nepozná totožnosť autora.

| Otázka | Nástroj | Čo môže povedať |
|---|---|---|
| Vykazuje text AI vzory? | AI Detector | odhad Human / AI / Mixed |
| Ako dokument vznikal v editore? | Writing Replay | sledované vkladanie a úpravy textu |
| Je text podobný staršiemu zdroju? | Plagiarism Check | zhody a zdrojové odkazy |
| Existuje citovaná publikácia? | Source Check / odborné overenie | existencia a identifikátory publikácie |
| Podporuje zdroj konkrétne tvrdenie? | čítanie originálu / kontrola tvrdení | vecná opora a kontext |

## 📊 Falošné pozitíva a negatíva

- **False positive:** autenticky ľudský text klasifikovaný ako AI.
- **False negative:** autenticky AI text klasifikovaný ako ľudský.
- **Zmienený text:** pasáže so známym rozdielnym pôvodom, ktoré nemožno vždy priamo označiť jednou binárnou triedou.
- **Confidence:** istota klasifikátora podľa jeho metodiky, nie fyzikálne overený „podiel AI“.

### **1. Ako vytvoriť férový experiment**

**Postup:**
1. Pripravíme vzorky s vopred známym pôvodom.
2. U ľudských vzoriek zdokumentujeme, že ich účastník napísal nezávisle od AI.
3. U AI vzoriek zaznamenáme model, dátum, prompt a podmienky použitia.
4. Jazyk a rozsah vzoriek zvolíme porovnateľne.
5. Výsledok skenu zapíšeme bez spätnej úpravy pôvodných štítkov.
6. V analýze odlíšime binárne a zmiešané príklady.

**Čo to robí:** Umožňuje merať presnosť v konkrétnom lokálnom experimente.

**Vysvetlenie:** Výsledok 5/5 na piatich vzorkách neznamená 100 % univerzálnu úspešnosť.

### **2. Prečo je dĺžka textu dôležitá**

**Postup:** Porovnáme jednu krátku vetu a dlhší súvislý text s rovnakou témou.

**Čo to robí:** Ukazuje, že krátke vzorky obsahujú menej informácií a môžu byť odmietnuté alebo klasifikované menej spoľahlivo.

**Vysvetlenie:** Pri dokumente s veľmi malým počtom znakov nevynucujeme interpretáciu.

### **3. AI originál, editácia a parafráza**

**Postup:** Porovnáme neupravený AI text, AI text upravený autorom a samostatný ľudský text. Pri každom zaznamenáme pôvod.

**Čo to robí:** Demonštruje citlivosť výsledku na spôsob prepracovania.

**Vysvetlenie:** Jazyková úprava nezaručuje, že model spoľahlivo identifikuje pôvod.

## 🧪 Matica skutočného pôvodu a výsledku

| Skutočný pôvod | Výsledok Human | Výsledok AI |
|---|---|---|
| Human | správna klasifikácia | falošné pozitívum |
| AI | falošné negatívum | správna klasifikácia |

Výsledok **Mixed** a **Uncertain** evidujeme oddelene. Bez vopred určenej metodiky ich nepočítame automaticky ako správne alebo nesprávne binárne predpovede.

## 🔬 Využitie v znaleckej a akademickej praxi

Pri odbornom posudzovaní predložíme zdokumentované vstupy, verziu a dátum skenovania, podmienky nástroja, vysvetlenie neistoty a ďalšie nezávislé dôkazy. Samotný výsledok AI detekcie **nestačí na forenzné určenie autora**, vyvodenie disciplinárneho previnenia alebo právny záver.

## 📚 Zdroj

- https://support.gptzero.me/articles/1787085022-what-are-the-limitations-of-gptzero-s-ai-classifier
- https://support.gptzero.me/articles/1087723304-what-is-gptzero
