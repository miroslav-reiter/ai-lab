# 📄 GPTZero – Microsoft Word, Google Dokumenty a Writing Replay

Podklady pre učiteľov, lektorov, doktorandov, vedúcich záverečných prác, znalcov a výskumníkov. Rozlišujeme **analýzu hotového textu** a **zaznamenaný proces písania**.

## 🪟 Microsoft Word – doplnok GPTZero

### **1. Nainštalovanie doplnku**

**Postup:**
1. Otvoríme Microsoft Word.
2. Prejdeme na **Home → Add-ins → More Add-ins** (prípadne File → Get Add-ins).
3. Vyhľadáme **GPTZero**.
4. Vyberieme **Add** a v prípade potreby sa prihlásime.
5. Na karte **Home** otvoríme **Show GPTZero**.

**Čo to robí:** Zobrazí GPTZero v bočnom paneli dokumentu.

**Vysvetlenie:** Dostupnosť doplnku môže závisieť od verzie Office, nastavení organizácie a povolených doplnkov.

### **2. Analýza označeného textu**

**Postup:**
1. Otvoríme vlastný tréningový DOCX dokument.
2. Označíme súvislý text v rozsahu aspoň **250 znakov**.
3. Počkáme, kým sa výber zobrazí v paneli GPTZero.
4. Klikneme na **Get Results**.
5. Preskúmame klasifikáciu a zvýraznené vety.

**Čo to robí:** Vykoná detekciu na vybranom texte.

**Vysvetlenie:** Pri bezplatnom pláne je limit na prvých 10 000 znakov výberu. Pri väčších dokumentoch si musíme uvedomiť, že výsledok nemusí reprezentovať celý text.

### **3. Celý dokument vs. jeden odsek**

**Postup:** Otestujeme jeden dostatočne dlhý odsek a potom väčší blok toho istého dokumentu.

**Čo to robí:** Porovnáme klasifikácie pri rozdielnej veľkosti vzorky.

**Vysvetlenie:** Odlišný výsledok nie je automaticky technickou chybou, pretože sa mení kontext vstupu.

### **4. Praktická ukážka so zmiešaným textom**

**Postup:** V Worde spojíme preukázateľne vlastný odsek a AI ukážku z `data/text-ai-vzor.txt`. Obidva bloky označíme a otestujeme samostatne aj spolu.

**Čo to robí:** Demonštruje úlohu kontextu a dĺžky.

**Vysvetlenie:** Nevyhlasujeme každú žltú vetu za preukázateľne vytvorenú AI.

## ☁️ Google Dokumenty – Writing Report

### **5. Príprava testovacieho dokumentu**

**Postup:**
1. Nainštalujeme oficiálne rozšírenie GPTZero pre Chrome, Edge alebo Firefox.
2. Prihlásime sa do GPTZero.
3. Vytvoríme **vlastný** Google Dokument.
4. Napíšeme niekoľko viet a dokument upravíme.
5. V ponuke GPTZero zvolíme **Watch Writing Report**.

**Čo to robí:** Zobrazí dostupné záznamy písania a vkladania textu.

**Vysvetlenie:** Pre Writing Report je potrebný prístup na úpravy dokumentu. Pri dokumente iba na čítanie sa táto funkcia nemusí zobraziť.

### **6. Writing Replay – postupné písanie a vložený odsek**

**Postup:**
1. Manuálne napíšeme odsek.
2. Niekoľko viet zmeníme.
3. Skopírujeme a vložíme **vlastný** pripravený odsek.
4. Otvoríme Writing Report a porovnáme udalosti.

**Čo to robí:** Učí nás čítať časový priebeh editovania.

**Vysvetlenie:** Hromadné vloženie nie je automaticky plagiátorstvo. Autor mohol písať offline alebo v inom editore.

### **7. Zdieľanie Writing Report**

**Postup:** V zázname otvoríme Share a rozhodneme, či má byť zdieľanie cez odkaz povolené.

**Čo to robí:** Poskytne ďalšej osobe prístup k záznamu podľa nastavení.

**Vysvetlenie:** Nesprávne nastavený verejný odkaz môže sprístupniť detaily tvorby dokumentu. Pred zdieľaním skontrolujeme oprávnenia, osobné údaje a pravidlá školy.

### **8. Čo Writing Replay dokazuje a čo nie**

| Záznam | Čo vieme vyvodiť | Čo nevieme vyvodiť |
|---|---|---|
| Postupné písanie | zaznamenané jednotlivé vloženia a úpravy | totožnosť osoby za klávesnicou |
| Hromadný paste | text bol vložený naraz | automaticky použitie AI alebo plagiát |
| Chýbajúci záznam | nemáme dostatočné procesné dáta | že text nevytvoril človek |
| Writing Report | spôsob úprav v rámci sledovaného prostredia | úplný pôvod dokumentu mimo zaznamenanej relácie |

## 🔒 Ochrana údajov

Pri aktivovaní Writing Replay Anywhere výrobca uvádza zaznamenávanie úprav vo vybraných editoroch vrátane vložení a odstránení textu. Údaje môžu odchádzať na jeho servery. U citlivých prác, dokumentov klientov alebo výskumných dát preveríme nastavenia záznamu a právny základ skôr, než funkciu aktivujeme.

## 📚 Oficiálne zdroje

- https://support.gptzero.me/articles/4982038962-How-can-I-get-the-Microsoft-Word-Add-In
- https://support.gptzero.me/articles/8893155578-how-can-i-use-the-microsoft-word-add-in-to-check-for-ai
- https://support.gptzero.me/articles/7001890416-what-is-the-google-docs-writing-report-for-origin
- https://support.gptzero.me/articles/7223290711-writing-replay-anywhere-faq
