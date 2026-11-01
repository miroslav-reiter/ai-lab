# 📚 GPTZero – plagiátorstvo, parafrázovanie, citácie a kontrola zdrojov

Cieľom je **rozlišovať nezávislé otázky**: kto alebo čo pravdepodobne vytvorilo text, či sa text podobá existujúcim zdrojom a či sú tvrdenia správne podložené.

## 🧠 Tri základné rozdiely

| Kontrola | Otázka | Čo výsledok nedokazuje |
|---|---|---|
| AI Detection | Vykazuje text vzory typické pre AI? | identitu autora ani etické previnenie |
| Plagiarism Check | Zodpovedá text existujúcim zdrojom? | že každá zhoda je plagiát |
| AI Hallucinations / Source Check | Existujú citácie a podopierajú tvrdenia? | že text je automaticky pravdivý |
| Possible AI Paraphrasing | Mohol byť pôvodný AI text následne upravený? | kto, prečo a za akých podmienok text upravil |

**Pravidlo:** Text napísaný pomocou AI môže byť použitý v súlade s pravidlami organizácie. Naopak, ľudský text môže byť plagiátom. Plagiátorstvo je otázka nepriznaného prevzatia cudzieho obsahu, nie len klasifikácie štýlu.

## 🧪 Praktické príklady

### **1. Plagiarism Check – kontrola zhody**

**Postup:** Prihlásime sa do GPTZero → Dashboard → vložíme alebo nahráme vlastný tréningový dokument → vyberieme **Plagiarism Check** → **Scan**.

**Čo to robí:** Porovnáva pasáže s dostupnými webovými a publikačnými zdrojmi.

**Vysvetlenie:** Funkcia môže vyžadovať platený plán. Výsledkom je zhoda, nie automatická kvalifikácia „plagiát“.

### **2. Overenie nájdeného zdroja**

**Postup:** Pri nájdenej zhode otvoríme citovaný zdroj, porovnáme originál a analyzovanú pasáž a vyhodnotíme úvodzovky, parafrázu, kontext a bibliografický odkaz.

**Čo to robí:** Odlišuje odôvodnenú textovú podobnosť od nesprávneho prevzatia.

**Vysvetlenie:** Riadená citácia môže spôsobiť vysokú podobnosť bez porušenia pravidiel citovania.

### **3. Plagiátorstvo vs. správne citovanie**

**Postup:** Pripravíme dve tréningové verzie odseku: jednu ako riadne označený citát s presným zdrojom, druhú s nepriznaným prevzatím. Skontrolujeme podobnosť.

**Čo to robí:** Ukazuje, že zhodu treba interpretovať podľa citovania.

**Vysvetlenie:** Percento zhody nie je percento plagiátorstva.

### **4. Kontrola DOI, názvu a autorov**

**Postup:** V `data/citacie-kontrola.md` nájdeme jeden reálny a jeden výslovne fiktívny príklad. Overíme bibliografické údaje v Crossref alebo u vydavateľa.

**Čo to robí:** Preveruje existenciu a správnosť referencie.

**Vysvetlenie:** DOI alebo názov môže byť uvedený nesprávne aj v dobre napísanej práci.

### **5. Súhlas tvrdenia so zdrojom**

**Postup:** Nájdeme originálny zdroj, prečítame relevantnú pasáž a overíme, či podporuje analyzované tvrdenie. Ak je dostupná funkcia AI Hallucinations, porovnáme jej výsledok s vlastným overením.

**Čo to robí:** Posudzuje faktickú oporu textu.

**Vysvetlenie:** Existujúca publikácia môže byť citovaná nesprávne alebo mimo kontextu.

### **6. Possible AI Paraphrasing**

**Postup:** V Advanced Scan sledujeme príznak „Possible AI Paraphrasing“ a jeho vysvetlenie. Zaznamenáme mieru istoty a podľa potreby konzultujeme pôvod textu s autorom.

**Čo to robí:** Označuje potenciálne prepracovaný AI text.

**Vysvetlenie:** Funkcia je podľa dokumentácie výrobcu označená ako beta a stále ide o klasifikačný odhad.

### **7. Akademická kontrola – vyhodnotenie bez automatického odsúdenia**

**Postup:** Preveríme pravidlá školy, históriu vzniku, dostupné pracovné verzie, citácie a výsledky detekcie. S autorom vecne prejdeme sporné pasáže.

**Čo to robí:** Získavame širší kontext pre transparentné rozhodovanie.

**Vysvetlenie:** Samotné skóre GPTZero nie je postačujúcim dôkazom podvodu.

## 🧾 Formulár pracovného záveru

| Pole | Čo zaznamenáme |
|---|---|
| Dokument | anonymizovaný identifikátor |
| Rozsah a jazyk | počet znakov/slov a jazyk |
| Režim GPTZero | Basic / Advanced / Plagiarism / Source |
| Výsledok AI detekcie | presná klasifikácia a vysvetlenie |
| Výsledok podobnosti | zdroje, zhody a správnosť citovania |
| Overenie zdrojov | odkazy na originály, DOI, kontext |
| Ďalšie dôkazy | pracovné verzie, história úprav, vyjadrenie autora |
| Predbežné vyhodnotenie | nejednoznačné / vyžaduje vysvetlenie / bez indikácie |
| Finálne rozhodnutie | podľa postupov školy alebo organizácie, nie automaticky podľa modelu |

## 🔒 Citlivé dokumenty

Neskenujeme cudzie rukopisy, znalecké posudky, interné zmluvy, osobné údaje alebo nepublikované výskumné výsledky bez oprávnenia a posúdenia zmluvných podmienok spracúvania.

## 📚 Oficiálne zdroje

- https://support.gptzero.me/articles/1988519176-What-is-Plagiarism-Check
- https://support.gptzero.me/articles/7953436668-what-are-ai-hallucinations-and-fact-check
- https://support.gptzero.me/articles/5593633457-how-does-gptzero-detect-ai-paraphrasing-and-ai-bypassers
- https://search.crossref.org/
