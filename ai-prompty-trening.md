# 🤖 AI prompty na tvorbu kontrolovaných testovacích vzoriek

Cieľom je pripraviť **AI generované texty so známym pôvodom** na porovnanie výsledkov v GPTZero. Nejde o návod na obchádzanie detektorov ani na vydávanie AI textu za vlastnú študentskú prácu.

## 🧠 Ako pripraviť reprodukovateľný test

Zaznamenáme použitý model, dátum, jazyk, presný prompt, prípadné ďalšie inštrukcie a to, či bol text upravený. Zadaním identického promptu nemusíme dostať rovnaký text.

| Prvok | Čo evidujeme |
|---|---|
| Model | napr. ChatGPT, Gemini alebo Claude, ak ho testujeme |
| Jazyk | slovenčina alebo iný zvolený jazyk |
| Prompt | presný text zadania |
| Dĺžka | počet znakov a slov |
| Prepracovanie | žiadne / manuálne / AI asistované |
| Výstup GPTZero | Human / Mixed / AI / Uncertain a vysvetlenie |
| Opakovanie | výsledok ďalšieho skenovania rovnakej vzorky |

## 📝 Praktické prompty

### **1. Vytvorenie informatívneho článku**

**Prompt:**

> Napíš 400 až 500 slov po slovensky o tom, ako sa organizujú online školenia digitálnych zručností. Použi jasné nadpisy a vecný štýl. Neuvádzaj vymyslené štatistiky ani bibliografické citácie.

**Čo to robí:** Pripraví kontrolovanú AI vzorku v informatívnom štýle.

**Vysvetlenie:** Pôvod označíme AI, aj keď GPTZero môže výsledok vyhodnotiť inak.

### **2. Formálny odborný text**

**Prompt:**

> Priprav 400-slovné vysvetlenie rozdielu medzi autentifikáciou a autorizáciou v IT v slovenskom jazyku. Použi formálny tón a praktické príklady bez uvádzania neoverených zdrojov.

**Čo to robí:** Testuje výsledok na odbornom textovom štýle.

### **3. Neformálny text na sociálne siete**

**Prompt:**

> Vytvor dva pôvodné príspevky o digitálnej bezpečnosti: jeden do 100 znakov a druhý približne 350 slov. Oba označ ako syntetické tréningové príklady.

**Čo to robí:** Porovnáme krátku a dlhú vzorku.

### **4. Marketingový opis kurzu**

**Prompt:**

> Napíš neutrálny modelový produktový opis fiktívneho online kurzu práce s tabuľkami, približne 300 slov. Neuvádzaj skutočné referencie, garancie ani údaje o zákazníkoch.

**Čo to robí:** Testuje marketingový a šablónový jazyk.

### **5. Text s rôznou dĺžkou viet**

**Prompt:**

> Napíš vecný článok o tvorbe vzdelávacích materiálov s kombináciou krátkych a dlhších viet. Zachovaj rovnakú tému a podobný rozsah ako pri predchádzajúcej vzorke.

**Čo to robí:** Umožňuje porovnať jazykový štýl vzoriek.

### **6. Porovnanie jazykov**

**Prompt:**

> Napíš dva obsahovo porovnateľné texty o online vzdelávaní, jeden po slovensky a druhý po anglicky. Každý nech má približne 350 slov. Oba sú určené iba na testovanie AI detekcie.

**Čo to robí:** Umožňuje sledovať rozdiely klasifikácie podľa jazyka.

### **7. Kontrolovaný text s citáciou**

**Prompt:**

> Vysvetli, ako kontrolovať dôveryhodnosť odborných zdrojov. Ak nemáš overenú publikáciu, nevytváraj názvy článkov ani DOI. Namiesto toho explicitne označ miesto, kde treba zdroj doplniť.

**Čo to robí:** Učí predchádzať fiktívnym citáciám.

### **8. Zmiešaný dokument**

**Postup:** AI vzorku získame podľa príkladu 1 a doplníme k nej odsek, ktorý účastník napísal úplne samostatne. Pred skenovaním zaznamenáme hranice jednotlivých pasáží.

**Čo to robí:** Vytvoríme skutočne zmiešaný kontrolovaný dokument.

## 🔒 Dôležité

- AI vytvorený text **nikdy nepremenujeme na preukázateľne ľudský text**.
- Účastníci musia skutočné ľudské vzorky vytvoriť samostatne.
- Vzorky môžu byť fakticky nesprávne, preto ich obsah neberieme ako zdroj odborných faktov.
- Výsledky GPTZero zapisujeme do `data/vysledky-vzor.csv` až po skutočnom skenovaní.
