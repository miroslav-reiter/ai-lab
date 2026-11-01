# 🧪 GPTZero – praktické príklady a cvičenia

Praktická zbierka úloh pre **GPTZero, AI detekciu textu, kontrolu originality, Word, Google Dokumenty, sociálne siete a akademické práce**. Pracujeme s vlastnými alebo výslovne označenými tréningovými materiálmi.

> **Základné pravidlo:** Výsledok GPTZero je odhad modelu, nie dokázané autorstvo, plagiát či podvod. Osobnú a akademickú zodpovednosť posudzujeme podľa príslušných pravidiel, overených dôkazov a komunikácie s autorom.

## 🧠 Ako čítať výsledky GPTZero

| Pojem | Význam |
|---|---|
| GPTZero | online služba na odhad pôvodu textu |
| Human | model odhaduje pravdepodobne ľudský text |
| AI | model odhaduje pravdepodobne generovaný text |
| Mixed | model identifikuje znaky zmiešaného pôvodu |
| Confidence | istota modelu v jeho odhade, nie fyzicky nameraný podiel AI viet |
| Basic Scan | základná klasifikácia dokumentu |
| Advanced Scan | rozšírená analýza a zvýraznené vety podľa plánu |
| False positive | ľudský text nesprávne označený ako AI |
| False negative | AI text nesprávne označený ako ľudský |
| Plagiarism Check | kontrola podobnosti s existujúcimi textami |
| Writing Replay | záznam úprav a procesu tvorby, nie overenie identity autora |
| Source Check | overovanie publikácií, citácií a podpory tvrdení |
| AI Vision | automatická analýza podporovaných stránok počas prehliadania |

## 📝 Detekcia a interpretácia textov

### **1. Základná AI analýza textu**

**Cieľ:** Naučiť sa vložiť text a prečítať klasifikáciu.

**Postup:**
1. Otvoríme [gptzero.me](https://gptzero.me/).
2. Skopírujeme obsah `data/text-ai-vzor.txt`.
3. Spustíme **Basic Scan**.
4. Zapíšeme výsledok do `data/vysledky-vzor.csv`.

**Čo to robí:** GPTZero porovná jazykové charakteristiky s naučenými vzormi.

**Vysvetlenie:** Tréningový text pochádza od AI asistenta. Ak GPTZero vráti Human, zaznamenáme falošne negatívny výsledok na tejto vzorke, nie univerzálne zlyhanie nástroja.

### **2. Nahratie vlastného dokumentu DOCX alebo PDF**

**Cieľ:** Overiť skenovanie bez kopírovania textu.

**Postup:** V Microsoft Worde vložíme tréningový text do dokumentu, uložíme ako `gptzero-test.docx` a v GPTZero použijeme upload súboru. Porovnáme výsledok s priamym vložením textu.

**Čo to robí:** Služba spracuje text z podporovaného formátu.

**Vysvetlenie:** Pri PDF môže presnosť extrakcie ovplyvniť rozloženie, tabuľky a naskenovaný obraz. Neodovzdávame citlivé ani cudzie súbory bez oprávnenia.

### **3. Basic Scan vs. Advanced Scan**

**Cieľ:** Rozlíšiť celkový výsledok od analýzy konkrétnych viet.

**Postup:** Ten istý text preveríme v základnom režime a – ak to plán umožňuje – v rozšírenom režime. Porovnáme označené pasáže.

**Čo to robí:** Poskytne rôzne úrovne podrobnosti interpretácie.

**Vysvetlenie:** Zvýraznená veta nie je priamym dôkazom, že ju vytvoril konkrétny jazykový model.

### **4. Čo znamená vysoké AI skóre**

**Cieľ:** Predísť mylnej interpretácii percent.

**Postup:** Otvoríme výsledok, prečítame slovný popis skóre a zaznamenáme hodnotu **presne tak, ako ju uvádza daný režim**.

**Čo to robí:** Odlišujeme modelovú pravdepodobnosť, istotu a podiel označených viet.

**Vysvetlenie:** Hodnota „80 % AI“ nie je automaticky dôkaz, že 80 % dokumentu vyprodukovala AI.

### **5. Kontrola skutočne ľudského textu**

**Cieľ:** Demonštrovať riziko falošného pozitíva.

**Postup:** Lektor alebo účastník samostatne napíše aspoň 250 znakov **bez použitia AI**, zaznamená tento spôsob vzniku a otestuje text.

**Čo to robí:** Testujeme klasifikátor na vzorke so známym pôvodom.

**Vysvetlenie:** Žiadny text vytvorený týmto repozitárom sa nevydáva za preukázateľne ľudský. Pripravíme si vlastnú vzorku podľa `data/README.md`.

### **6. Zmiešaný dokument**

**Cieľ:** Posúdiť text kombinujúci vlastnú a AI časť.

**Postup:** Do nového dokumentu vložíme jeden nezávisle napísaný ľudský odsek a jeden odsek zo `data/text-ai-vzor.txt`. Pri ukladaní si presne poznamenáme hranice pasáží. V GPTZero sledujeme výsledok Mixed a zvýraznenie.

**Čo to robí:** Skúmame citlivosť modelu na odlišný pôvod častí textu.

**Vysvetlenie:** Ak detektor správne neoznačí konkrétnu pasáž, neznamená to, že sa text zmenil na ľudský.

## 🌐 Web a sociálne siete

### **7. Detekcia AI obsahu na blogu**

**Cieľ:** Analyzovať väčší webový článok.

**Postup:** Na vlastnom testovacom webe otvoríme článok, označíme text a v rozšírení GPTZero použijeme **Scan Selection** alebo **Scan Page**, ak je dostupné.

**Čo to robí:** Skontrolujeme pôvod textu bez manuálneho prenášania do inej aplikácie.

**Vysvetlenie:** Nástroj neoveruje pravdivosť informácií. Pre hodnotenie faktov použijeme aj kontrolu zdrojov.

### **8. AI Vision na sociálnych sieťach**

**Cieľ:** Rozlíšiť automatickú detekciu a manuálnu analýzu.

**Postup:** Rozšírenie → nastavenie **AI Vision** → **Auto-scan my feed** → povolíme vybranú podporovanú sociálnu sieť → otvoríme vlastný tréningový príspevok.

**Čo to robí:** Zobrazuje štítky pri textovom obsahu počas prehliadania.

**Vysvetlenie:** Označenie nie je dôkaz, že autor klame. Podporu funkcie môže ovplyvniť prehliadač, stránka a plán.

### **9. Krátky komentár vs. dlhší príspevok**

**Cieľ:** Ukázať vplyv dĺžky textu.

**Postup:** Porovnáme jednoriadkový komentár s dlhším tréningovým príspevkom, ktorý tvorí súvislý text.

**Čo to robí:** Sledujeme, či systém krátky obsah vôbec vyhodnotí a aký má výstup.

**Vysvetlenie:** Veľmi krátky text často neobsahuje dostatok jazykových indícií.

## 📄 Microsoft Word a Google Dokumenty

### **10. Doplnok GPTZero v Microsoft Word**

**Cieľ:** Detekovať text bez opustenia Wordu.

**Postup:** **Home → Add-ins → More Add-ins** → vyhľadáme GPTZero → **Add** → **Home → Show GPTZero** → prihlásenie → označíme text → **Get Results**.

**Čo to robí:** Zobrazuje klasifikáciu v pravom bočnom paneli Wordu.

**Vysvetlenie:** Výber musí mať najmenej 250 znakov; bezplatný plán môže obmedzovať dĺžku skenu. Podrobnosti v `gptzero-word-google-docs.md`.

### **11. Google Dokumenty – Writing Report**

**Cieľ:** Zobraziť proces vzniku dokumentu.

**Postup:** Otvoríme **vlastný** Google Dokument s oprávnením úprav, nainštalovaným rozšírením GPTZero a vykonáme niekoľko úprav. Potom použijeme **Watch Writing Report**.

**Čo to robí:** Prehrá zaznamenané úpravy, vkladanie a priebeh písania podľa dostupných záznamov.

**Vysvetlenie:** Záznam nepreukazuje, kto sedel pri počítači, ani či prenesený text vznikol inde vlastnou prácou.

### **12. Hromadné vloženie textu vs. postupné písanie**

**Cieľ:** Ukázať rozdiel medzi pozorovaním procesu a dôkazom autorstva.

**Postup:** V novom testovacom dokumente najprv ručne píšeme, potom vložíme vlastný pripravený odsek a pozrieme si Writing Report.

**Čo to robí:** Uvidíme rozdielne udalosti editovania.

**Vysvetlenie:** Paste event nie je automaticky plagiát alebo AI generovanie.

## 📚 Originalita, plagiátorstvo a veda

### **13. Plagiarism Check**

**Cieľ:** Rozlíšiť textovú podobnosť a autorstvo.

**Postup:** V Dashboarde zvolíme **Plagiarism Check**, vložíme autorizovaný text, spustíme kontrolu a otvoríme jednotlivé zdroje zhody.

**Čo to robí:** Porovnáva text s dostupnými zdrojmi a uvádza podobnosť.

**Vysvetlenie:** Zhodná pasáž môže byť správne citovaná. Percento zhody nie je percento plagiátorstva. Funkcia môže byť platená.

### **14. Kontrola citácie a DOI**

**Cieľ:** Overiť skutočnú existenciu zdroja.

**Postup:** Otvoríme `data/citacie-kontrola.md`, nájdeme zdroj v katalógu, vydavateľovi alebo Crossref a preveríme názov, autora a DOI. Podľa plánu porovnáme s kontrolou v GPTZero.

**Čo to robí:** Odhaľujeme možné neexistujúce alebo nesúvisiace bibliografické odkazy.

**Vysvetlenie:** Existujúci DOI sám nezaručuje, že zdroj podporuje tvrdenie.

### **15. AI parafrázovanie**

**Cieľ:** Pochopiť hodnotenie „Possible AI Paraphrasing“.

**Postup:** Ak máme Advanced Scan, otvoríme túto beta funkciu, porovnáme opis výsledku s pôvodným textom a zapíšeme nejednoznačnosti.

**Čo to robí:** GPTZero sa pokúša odhadnúť, či AI text prešiel výrazným prepracovaním.

**Vysvetlenie:** Beta príznak je indícia, nie dôkaz obchádzania pravidiel.

### **16. Súhrnný experiment a vyhodnotenie**

**Cieľ:** Porovnať predikciu so známym pôvodom.

**Postup:** Zaznamenáme výsledky do `data/vysledky-vzor.csv`, doplníme skutočné triedy a predikcie a spustíme:

```bash
python3 scripts/vyhodnotenie-gptzero.py --input data/vysledky-vzor.csv
```

**Čo to robí:** Lokálne vypíše počet správnych a nesprávnych klasifikácií pre zadané vzorky.

**Vysvetlenie:** Skript sám **nedeteguje AI** a neposiela dokumenty nikam na internet.

## 📚 Zdroje

- https://gptzero.me/
- https://support.gptzero.me/articles/1675846160-ai-vision
- https://support.gptzero.me/articles/8893155578-how-can-i-use-the-microsoft-word-add-in-to-check-for-ai
- https://support.gptzero.me/articles/7001890416-what-is-the-google-docs-writing-report-for-origin
- https://support.gptzero.me/articles/1988519176-What-is-Plagiarism-Check
