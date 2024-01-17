# Gunārs Leitāns, 1.kurss 4.grupa, DITF fakultāte

## Projekta izvēle un skaidrojums

### Projekta mērķis

Pēc RTU kursa **Lietojumprogrammatūras automatizēšanas rīki(1),23/24-R** prasībām, izveidot Python programmēšanas valodas projektu izmantojot kursā apskatītās tehnoloģijas, tika izveidots projekts ***JobSearch: Automated vacancy search program***. Projekta mērķis ir atvieglot un automatizēt lietotāja spēju meklēt darba vakances, saglabāt tās excel datnē priekš vēlākas aplūkošanas.

### Projekta nosacījumi un skaidrojums

Projekta nosacījumi iekļauj sevī veidot programmu izmantojot Python programmēšanas valodu. Programma tika izstrādā izmantojot Visual Studio Code.

- Projektu veidoja viena persona, Gunārs Leitāns

Projekta izstrādē tika izmantotas vairāks Python bibliotēkas:

- Selenium
- Pandas ar iebūvēto openpyxl atbalstu
- Tkinter
- datetime
- os

Projekta izstrādei tiek izmantotas sekojošās bibliotēkas, lai spētu izmantot Python valodas priekšrocības automatizēt lietotāja darba vakanču meklēšanu.

Selenium bibliotēka tiek izmantota, lai izgūtu un vēlāk apstrādātu iegūto informāciju no mājaslapas.

Pandas bibliotēka ar openpyxl iebūvēto atbalstu nodrošina iespēju saglabāt izgūtu informāciju no mājaslapas excel(.xlsx) formātā.

Tkinter bibliotēka ir lietotāja interfeiss(GUI), kas sniedz ērtāku lietotāja saskarni un patīkamāku programmas izmantošanas procesu.

Datetime un OS bibliotēkas ir sistēmas bibliotēkas. Datetime bibliotēka nolasa laiku, kurā tiek veiktas kādas darbības. OS bibliotēka ļauj atrast sistēmā nepieciešamos failus, ja tādi pastāv.

## Projekta izstrāde

### Projekta nepieciešamie uzstādījumi pirms palaišanas

Lai šo projektu spētu atkārtot uz citām ierīcēm vai pārbaudīt darbību, nepieciešams iegūt sekojošās bibliotēkas, kuras netiek ielādētas ar Python programmēšanas valodu.

Šis bibliotēkas tika paskaidrotas un minētas projekta skaidrojuma daļā, taču lai izmantotu Selenium, Pandas ar iekļauto openpyxl un Tkinter bibliotēkas, tās ir nepieciešams ielādēt savā izstrādes vidē.

### Lai iegūtu Selenium:
`pip install selenium`

### Lai iegūtu Pandas un openpyxl:
`pip install pandas`
`pip install openpyxl`

### Lai iegūtu Tkinter:
`pip install tkinter`

Kad šis tiek veikts, programmas darbību veikšanai jānorit veiksmīgi. Programma tiek palaista; atveras lietotāja ievade, kurā tiek prasīts ievadīt prasīto; pēc mirkļa tiek izveidots excel(.xlsx) fails, kuru var atvērt uz ekrāna.

### Projekta piemēru attēli

Šeit var aplūkot projekta attēlus, kuros ir redzama lietotāja vide. Arī tiek parādīts, kur tiek izmantota lietotāja ievadītā informācija un saglabāto excel faila saturu.

**Lietotāja vides saskarnes logs:**



**Lietotāja vides saskarnes logs ar informāciju:**



**Lietotāja ievadītā informācijas pielietojums:**



**Saglabātais fails ar rezultātu:**



Izmantojot šo programmu var arī novērot, ka nevienmēr excel faila informācijas formāts būs vienāds, jo dažreiz vakances nesatur informāciju par, piemēram, atalgojumu vai termiņa beigām.

***Excel fails saglabā šādu informāciju, ja to spēj atrast:***

Amata nosaukumu; Atrašanās vietu; Vakances publikācijas laiku; Vidējo atalgojumu(bruto); Vakances termiņa beigas; Vakances saite; Programmas veikšanas laiku.