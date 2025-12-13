# Genesis

> *"In den beginne was het Woord [...] Alle dingen zijn door het Woord geworden en zonder dit is geen ding geworden, dat geworden is."*  
> — Geïnspireerd door Johannes 1:1,3

**Genesis** is een agent-gedreven framework voor repository-initialisatie. Het brengt structuur, orde en governance aan in nieuwe projecten via de **Logos** basis-agent.

---

## 🎯 Overzicht

Genesis automatiseert het opzetten van een complete repository-structuur met:
- **Gestandaardiseerde directory-structuur**
- **Governance documenten** (constitutie, handvest, beleid)
- **Agent framework** (moeder-agent + sub-agents)
- **Configuratiebestanden** (vim, copilot, gitignore)
- **Documentatie templates**

## 🏗️ Structuur

Genesis bevat:

```
/.github
    /agents              # Agent definities
        genesis.logos.agent.md
    /prompts             # Prompt bestanden
        genesis.logos.prompt.md
/config                  # Standaard configuraties
    .vimrc
    copilot.lua
constitutie.md           # Algemene constitutie (bindend)
handvest-logos.md        # Logos structuurprincipes
.gitignore               # Standard ignore regels
```

## 🚀 Gebruik

### Initialiseer een Nieuwe Repository

```
@github /genesis.logos
```
Geef aan dat logos moet het onstaan in gang zet met het woord 'ontsta'
Voeg daar aan toe:

**Benodigde informatie:**
1. **Taal**: `Nederlands` of `Engels`
2. **Context**: Korte omschrijving van het toepassingsdomein
3. **Kit-naam**: Bij voorkeur 3 letters (bijv. `DMS`, `TLX`, `CMR`)

**Voorbeeld:**
```
@github /genesis.logos 
Taal: Nederlands
Context: Data migratie toolkit voor legacy systemen
Kit: DMS
```

### Resultaat

Logos creëert de volgende structuur in de nieuwe repository:

```
/docs                    # Documentatie
/input                   # Input bestanden (lokaal, niet in git)
/desc-agents             # Agent beschrijvingen
/.github
    /agents              # Agent definities (.agent.md)
    /prompts             # Prompt bestanden (.prompt.md)
/<kit-naam>-kit
    /scripts             # Utility scripts en agent-scripts
    /templates           # Herbruikbare templates
    /config              # Editor configuraties
/<kit-naam>-governance
    constitutie.md       # Algemene regels
    handvest-logos.md    # Structuurprincipes
    beleid.md            # Project-specifiek beleid (template)
.gitignore               # Ignore regels aangepast voor project
README.md                # Project overzicht
```

## 📋 Governance

### Constitutie
De **constitutie** (`constitutie.md`) bevat algemene regels die bindend zijn voor alle repositories en agents:
- Taalgebruik en communicatie (B1 niveau)
- Professionele normen (agile, duurzaam ontwerp)
- Kwaliteitseisen voor specificaties
- AI-agent gedrag en orkestratie
- Transparantie en traceerbaarheid

### Handvest van Logos
Het **handvest** (`handvest-logos.md`) definieert hoe Logos repositories initialiseert:
- Verplichte repository-structuur
- Moeder-agent en sub-agent hiërarchie
- Scheiding tussen prompts en beschrijvingen
- Discipline en validatie
- Cleanup gedrag (Logos ruimt zichzelf op na voltooiing)

### Beleid
Elk project krijgt een **beleid** (`beleid.md`) dat project-specifieke regels bevat. Dit wordt ingevuld door de moeder-agent.

## 🤖 Agent Hiërarchie

### 1. Logos (Genesis)
- **Rol**: Repository initialisatie
- **Locatie**: `.github/agents/genesis.logos.agent.md`
- **Taken**: Structuur aanmaken, governance kopiëren, moeder-agent creëren
- **Cleanup**: Verwijdert zichzelf en handvest na voltooiing

### 2. Moeder-Agent (Per Project)
- **Rol**: Project management en workflow
- **Locatie**: `.github/agents/<kit-naam>.moeder.agent.md`
- **Taken**: Context beheren, sub-agents maken, beleid definiëren
- **Gebruik**: `@github /<kit-naam>.moeder`

### 3. Sub-Agents (Per Taak)
- **Rol**: Specifieke taken binnen workflow
- **Locatie**: `.github/agents/<kit-naam>.<agent-naam>.agent.md`
- **Nummering**: 01-89 voor workflow agents, 90-99 voor ondersteunende agents
- **Scripts**: Optioneel PowerShell script in `/<kit-naam>-kit/scripts/`

## 📝 Agent Documentatie

Agents hebben twee componenten:

1. **Agent Definitie** (`.github/agents/*.agent.md`)
   - Compact, focus op uitvoering
   - Gelezen door GitHub Copilot
   - YAML frontmatter met beschrijving

2. **Agent Beschrijving** (`/desc-agents/*.md`)
   - Gedetailleerde documentatie
   - Voorbeelden en rationale
   - Voor menselijke lezers

**Rationale voor scheiding:**
- Efficiënt tokengebruik (Copilot laadt alleen compacte definitie)
- Duidelijke functie-scheiding (AI vs. mens)
- Betere onderhoudbaarheid

## ⚙️ Configuratie

Genesis kopieert standaard configuraties naar nieuwe repositories:

### Editor Configuraties
- **`.vimrc`**: Vim/Neovim configuratie voor Copilot
- **`copilot.lua`**: Lua configuratie voor Neovim Copilot plugin

### Git Configuratie
- **`.gitignore`**: Negeert `/input/`, backup bestanden, afbeeldingen
- Kopregel wordt aangepast naar project naam

## 🛠️ PowerShell Scripts

Agents kunnen PowerShell scripts genereren voor herhaald gebruik:
- **Naam**: `<kit-naam>.<agent-naam>.ps1`
- **Locatie**: `/<kit-naam>-kit/scripts/`
- **Doel**: Automatiseren van agent-taken zonder AI-interactie

## 📚 Voorbeelden

### DMS (Data Migratie Systeem)
```
Taal: Nederlands
Context: Data migratie toolkit voor het overzetten van legacy databases naar moderne platformen
Kit: DMS
```

**Resulteert in:**
- `dms-kit/` met scripts en templates
- `dms-governance/` met beleid
- `@github /dms.moeder` als centrale agent

### TLX (Telemetrie/Analytics)
```
Taal: Engels
Context: Telemetry collection and analysis framework for IoT devices
Kit: TLX
```

**Resulteert in:**
- `tlx-kit/` with scripts and templates
- `tlx-governance/` with policy
- `@github /tlx.moeder` as central agent

## 🔄 Workflow

1. **Initialisatie**: `@github /genesis.logos` met taal, context, kit-naam
2. **Structuur**: Logos creëert directories, kopieert governance en config
3. **Moeder-agent**: Logos maakt moeder-agent aan voor het project
4. **Cleanup**: Logos verwijdert zichzelf en handvest uit root
5. **Activatie**: `@github /<kit-naam>.moeder` om verder te gaan
6. **Sub-agents**: Moeder-agent creëert specifieke agents voor workflow
7. **Beleid**: Moeder-agent vult project-specifiek beleid in

## 🎓 Principes

Genesis volgt deze kernprincipes:

1. **Orde en Structuur**: Consistente directory-structuur in alle projecten
2. **Governance-first**: Constitutie en handvest zijn bindend
3. **Agent Hiërarchie**: Logos → Moeder → Sub-agents
4. **Scheiding van Zorgen**: Prompt ≠ Beschrijving, Agent ≠ Script
5. **Zelf-cleanup**: Logos is eenmalig, moeder-agent blijft
6. **Menselijke Controle**: Alleen mensen wijzigen constitutie

## ❓ FAQ

**Q: Waarom ruimt Logos zichzelf op?**  
A: Logos is een initialisatie-agent die bij Genesis hoort, niet bij het nieuwe project. De moeder-agent neemt het over. Het handvest blijft beschikbaar in de governance directory.

**Q: Kan ik de constitutie aanpassen?**  
A: Alleen mensen mogen inhoudelijke wijzigingen maken. Logos mag alleen formattering aanpassen. Andere agents mogen de constitutie niet aanraken.

**Q: Waarom twee bestanden per agent?**  
A: De `.agent.md` in `.github/agents/` is compact voor Copilot (efficiënt tokengebruik). De beschrijving in `desc-agents/` is uitgebreid voor mensen.

**Q: Wat als ik meer dan 3 letters wil voor de kit-naam?**  
A: Dit kan, maar 3 letters is de voorkeur voor consistentie en leesbaarheid (bijv. `DMS`, `TLX`, `CMR`).

**Q: Kan ik andere talen gebruiken dan Nederlands of Engels?**  
A: Nee, het handvest staat alleen Nederlands en Engels toe. Dit zorgt voor consistentie in de documentatie.

**Q: Wat is het verschil tussen moeder-agent en sub-agents?**  
A: De moeder-agent kent de volledige context en workflow. Sub-agents doen specifieke taken. Alleen de moeder-agent mag nieuwe agents maken.

## 📖 Documentatie

- **Constitutie**: `constitutie.md` - Algemene regels (10 artikelen)
- **Handvest**: `handvest-logos.md` - Logos gedrag (10 artikelen)
- **Agent Definitie**: `.github/agents/genesis.logos.agent.md` - Logos implementatie

## 🤝 Bijdragen

Genesis is een intern framework. Wijzigingen aan de constitutie of handvest moeten:
1. Via menselijke review gaan
2. Consistent zijn met bestaande principes
3. Geen conflicten introduceren

## 📄 Licentie

Intern gebruik.

---

**Genesis** - *Agent-gedreven repository initialisatie*

*"Logos is kenner van het scheppen en het ordenen"*
