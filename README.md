# Genesis

> *"In den beginne was het Woord [...] Alle dingen zijn door het Woord geworden en zonder dit is geen ding geworden, dat geworden is."*  
> — Geïnspireerd door Johannes 1:1,3

**Genesis** is de basisrepository voor het standaardiseren en onderhouden van document-repositories. Het bevat governance documenten, workspace standaarden en Agent Logos - de Git en GitHub expert.

---

## 🎯 Overzicht

Genesis biedt:
- **Workspace standaarden** voor folderstructuur en naamgeving
- **Governance documenten** (constitutie, beleid)
- **Agent Logos** definitie en rolbeschrijving
- **Templates** voor documenten en configuraties
- **Best practices** voor git/github workflows

## 🏗️ Structuur

```
/docs                    # Documentatie (voor toekomstige uitbreidingen)
/governance             # Governance documenten
    gedragscode.md      # Constitutie voor alle repositories
    beleid.md           # Genesis workspace beleid
    workspace-standaard.md  # Standaard voor document-repositories
    agent-standaard.md  # Standaard voor agent componenten
    /rolbeschrijvingen  
        logos.md        # Agent Logos rolbeschrijving (interne werking)
/templates              # Document templates
    rolbeschrijving-template.md
/scripts                # Agent runners (Python)
    (nog geen runners)
/.github
    /agents             # Agent definities (DEPRECATED - zie agent-standaard)
        genesis.logos.agent.md
    /prompts            # Agent prompts (contract: in/uit)
        logos.prompt.md
/config                 # Editor configuraties
    .vimrc
    copilot.lua
README.md               # Dit bestand
.gitignore             # Git ignore patterns
```

## 🤖 Agent Structuur

Genesis gebruikt een **3-componenten agent model**:

1. **Rolbeschrijving** (`governance/rolbeschrijvingen/`) - Interne werking en verantwoordelijkheden
2. **Prompt** (`.github/prompts/`) - Contract met input/output specificatie
3. **Runner** (`scripts/`) - Python script voor automatisering zonder AI

**Voorbeeld: Agent Logos**
- Rolbeschrijving: [governance/rolbeschrijvingen/logos.md](governance/rolbeschrijvingen/logos.md)
- Prompt: [.github/prompts/logos.prompt.md](.github/prompts/logos.prompt.md)
- Runner: `scripts/logos.py` (nog niet geïmplementeerd)

Zie [governance/agent-standaard.md](governance/agent-standaard.md) voor volledige specificatie.

## 🚀 Gebruik

### Agent Logos Activeren

Gebruik Agent Logos voor git/github advies en repository structurering:

**Met AI (GitHub Copilot)**:
```
@github /logos <opdracht>
```

**Voorbeelden**:
- `@github /logos Richt deze workspace in volgens de standaard`
- `@github /logos Analyseer de huidige structuur`
- `@github /logos Stel een .gitignore op voor deze repository`

**Zonder AI (runner)**:
```bash
python scripts/logos.py --check-structure
```
*(nog niet geïmplementeerd)*

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

### Typische Taken

**Nieuwe repository**:
1. Structuur inrichten volgens workspace-standaard
2. README aanmaken
3. .gitignore configureren
4. Commit conventies documenteren

**Bestaande repository**:
1. Structuur analyseren en optimaliseren
2. Documentatie updaten
3. Git/GitHub best practices toepassen

**Meer informatie**: Zie [governance/rolbeschrijvingen/logos.md](governance/rolbeschrijvingen/logos.md)

## 📋 Governance

### Gedragscode (Constitutie)
[governance/gedragscode.md](governance/gedragscode.md) bevat algemene regels bindend voor alle repositories:
- **Artikel 2**: Taalgebruik op B1 niveau
- **Artikel 4**: Normen en standaarden, beleid per workspace
- **Artikel 5**: AI-agents en orkestratie
- **Artikel 8**: Evolutie van constitutie (alleen mensen wijzigen inhoud)
- **Artikel 9**: Minimale vereisten voor workspace beleid (scope!)

### Workspace Standaard
[governance/workspace-standaard.md](governance/workspace-standaard.md) normeert:
- Verplichte folderstructuur voor document-repositories
- Naamgevingsconventies (lowercase, hyphens)
- Markdown standaarden
- Agent structuur en `/scripts` folder
- Validatie checklist

### Agent Standaard
[governance/agent-standaard.md](governance/agent-standaard.md) definieert:
- **3-componenten model**: Rolbeschrijving + Prompt + Runner
- Rolbeschrijving: Interne werking (in `/governance/rolbeschrijvingen/`)
- Prompt: Contract met in/uit (in `/.github/prompts/`)
- Runner: Python script voor automatisering (in `/scripts/`)
- Naamgevingsconventies en best practices

### Genesis Beleid
[governance/beleid.md](governance/beleid.md) definieert:
- **Scope**: Wat Genesis WEL doet (governance, standaarden, templates, Logos)
- **Niet in scope**: Wat Genesis NIET doet (domein-specifieke content, code, data)
- Kwaliteitsnormen
- Relatie met andere repositories

## 📚 Templates

In [templates/](templates/) vind je herbruikbare sjablonen:
- `rolbeschrijving-template.md` - Voor nieuwe agent rolbeschrijvingen

## ⚙️ Configuratie

In [config/](config/) staan editor configuraties:
- `.vimrc` - Vim/Neovim configuratie
- `copilot.lua` - Copilot configuratie voor Neovim

## 🤝 Bijdragen

**Wijzigingen aan governance**:
- Gedragscode: Alleen mensen mogen inhoudelijke wijzigingen doen
- Logos mag alleen redactioneel verbeteren (Artikel 8)
- Workspace standaard: Via issues en discussie

**Wijzigingen aan Logos**:
- Via pull request met review
- Testing in test-workspace

## 📖 Meer Informatie

- [Gedragscode (Constitutie)](governance/gedragscode.md)
- [Workspace Standaard](governance/workspace-standaard.md)
- [Agent Standaard](governance/agent-standaard.md)
- [Genesis Beleid](governance/beleid.md)
- [Agent Logos Rolbeschrijving](governance/rolbeschrijvingen/logos.md)
- [Agent Logos Prompt](.github/prompts/logos.prompt.md)
- [Agent Logos Definitie (deprecated)](.github/agents/genesis.logos.agent.md)

---

**Genesis** - *Fundament voor gestandaardiseerde document-repositories*

**Maintained by**: Repository Owner + Agent Logos  
**Versie**: 1.0
