# Genesis

**🌱 Agent-driven repository initialization framework**

Genesis bevat de Logos agent die nieuwe repositories initialiseert met een consistente structuur, governance documenten en een moeder-agent die het project beheert.

---

## Wat is Genesis?

Genesis is een framework voor het **gestructureerd opzetten van repositories** via AI-agents. Het kernconcept:

1. **Logos** - De basis-agent die repositories initialiseert
2. **Constitutie** - Algemene regels voor alle projecten
3. **Handvest** - Structuurprincipes voor repository-opzet
4. **Moeder-agent** - Project-specifieke agent die sub-agents beheert

### Principes

- **Duidelijkheid**: Heldere structuur en documentatie op B1 niveau
- **Traceerbaarheid**: Alle beslissingen zijn gedocumenteerd
- **Consistentie**: Geen conflicten tussen documenten
- **Agent-orkestratie**: Duidelijke taakverdeling tussen agents

---

## Structuur

```
genesis/
├── .github/
│   └── agents/
│       └── genesis.logos.agent.md    # Logos agent definitie
│
├── desc-agents/
│   └── 00-genesis-logos-agent.md     # Uitgebreide Logos documentatie
│
├── constitutie.md                     # Algemene constitutie (bindend)
├── handvest-logos.md                  # Repository structuurprincipes
└── agent-file-template.md             # Template voor nieuwe agents
```

---

## Gebruik

### Initialiseer een Nieuwe Repository

Gebruik de Logos agent in GitHub Copilot Chat:

```
@github /genesis.logos Taal: Nederlands, Context: Data migratie tools voor legacy ERP systemen, Kit: dms
```

**Vereiste informatie**:
- **Taal**: `Nederlands` of `Engels`
- **Context**: Korte omschrijving van het toepassingsdomein
- **Kit-naam**: Identifier van 3 letters (bijv. `dms`, `tlx`, `cmr`)

### Wat doet Logos?

Logos creëert de volgende structuur in de nieuwe repository:

```
nieuwe-repo/
├── docs/                              # Projectdocumentatie (leeg)
├── input/                             # Input bestanden (leeg)
├── desc-agents/                       # Agent beschrijvingen
│   └── 00-moeder-agent.md             # Template
│
├── .github/
│   ├── agents/
│   │   └── <kit>-moeder.agent.md      # Moeder-agent definitie
│   └── prompts/                       # Herbruikbare prompts
│
├── <kit>-kit/                         # Kit-specifieke bestanden
│   ├── scripts/                       # Utility scripts
│   └── templates/                     # Templates
│
├── <kit>-governance/                  # Governance documenten
│   ├── constitutie.md                 # Kopie van algemene constitutie
│   ├── handvest-logos.md              # Kopie van handvest
│   └── beleid.md                      # Template voor project beleid
│
└── README.md                          # Project overzicht
```

**Na initialisatie**:
- ✅ Repository structuur is compleet
- ✅ Moeder-agent is geïnitialiseerd
- ✅ Governance documenten zijn aanwezig
- ✅ Logos ruimt zichzelf op uit de nieuwe repository

---

## Governance

### Constitutie

De **constitutie** (`constitutie.md`) bevat algemene regels voor alle repositories:

- Taalgebruik en communicatie
- Professionele normen
- Kwaliteit van specificaties
- AI-agents en orkestratie
- Transparantie en vertrouwen
- Veiligheid en integriteit

**Bindend voor alle projecten** - mag niet worden overschreven.

### Handvest van Logos

Het **handvest** (`handvest-logos.md`) beschrijft:

- Benodigde informatie voor repository-opzet
- Verplichte directory structuur
- Rol van moeder-agent vs sub-agents
- Workflow en documentatie vereisten

**Bindend voor repository initialisatie** - Logos volgt dit strikt.

### Project Beleid

Elk project heeft een **beleid** (`<kit>-governance/beleid.md`) dat:

- Project-specifieke regels definieert
- Consistent is met constitutie en handvest
- Door de moeder-agent wordt ingevuld

---

## Agent Hiërarchie

### 1. Logos (Genesis)
- **Rol**: Initialisatie-agent
- **Taak**: Creëert repository structuur
- **Eenmalig**: Ruimt zichzelf op na voltooiing
- **Locatie**: Blijft in Genesis repository

### 2. Moeder-Agent (Project)
- **Rol**: Centrale project-agent
- **Taak**: Beheert workflow, creëert sub-agents, definieert beleid
- **Doorlopend**: Blijft actief gedurende project
- **Locatie**: In de nieuwe repository

### 3. Sub-Agents (Project)
- **Rol**: Specifieke taken binnen workflow
- **Taak**: Voeren gedefinieerde stappen uit
- **Per fase**: Kunnen worden aangemaakt/verwijderd
- **Locatie**: In de nieuwe repository

---

## Agent Template

Genesis bevat een **agent template** (`agent-file-template.md`) voor het creëren van nieuwe agents.

Het template bevat secties voor:
- Beschrijving en rol
- Governance verwijzingen
- Invoer en verantwoordelijkheden
- Workflow stappen met validatie
- Beperkingen (NIET mag / WEL mag)
- Output en artefacten
- Volgende stap in workflow

Moeder-agents gebruiken dit template om sub-agents te creëren.

---

## Voorbeelden

### Data Migratie Systeem (DMS)

```
@github /genesis.logos Taal: Nederlands, Context: Data migratie tools voor legacy ERP systemen, Kit: dms
```

**Resultaat**:
- Repository met `dms-kit/` en `dms-governance/`
- Moeder-agent: `@github /dms.moeder`
- Sub-agents: `dms.extract`, `dms.transform`, `dms.load`

### Telemetrie Analyse (TLX)

```
@github /genesis.logos Taal: Engels, Context: Telemetry analysis for IoT devices, Kit: tlx
```

**Resultaat**:
- Repository met `tlx-kit/` en `tlx-governance/`
- Moeder-agent: `@github /tlx.moeder`
- Sub-agents: `tlx.ingest`, `tlx.analyze`, `tlx.report`

---

## Ontwikkeling

### Vereisten

- GitHub Copilot met Chat enabled
- GitHub repository (voor agents)
- Git (optioneel, voor versiebeheer)

### Genesis Aanpassen

1. **Constitutie wijzigen**: Update `constitutie.md` (alleen na goedkeuring)
2. **Handvest aanpassen**: Update `handvest-logos.md` (alleen structurele wijzigingen)
3. **Logos verbeteren**: Update `.github/agents/genesis.logos.agent.md` en documentatie
4. **Template verbeteren**: Update `agent-file-template.md`

**Let op**: Wijzigingen in constitutie en handvest zijn bindend voor alle bestaande én nieuwe repositories.

### Testen

Test Logos door een nieuwe repository te initialiseren:

```
@github /genesis.logos Taal: Nederlands, Context: Test repository voor Genesis validatie, Kit: tst
```

Valideer:
- [ ] Structuur is correct aangemaakt
- [ ] Governance documenten zijn gekopieerd
- [ ] Moeder-agent template is aanwezig
- [ ] README bevat juiste informatie
- [ ] Logos heeft zichzelf opgeruimd

---

## Veelgestelde Vragen

### Waarom ruimt Logos zichzelf op?

Logos is een **eenmalige initialisatie-agent** die hoort bij Genesis. Na het creëren van de repository structuur en moeder-agent heeft Logos zijn taak voltooid. De moeder-agent neemt het over.

### Kan ik Logos opnieuw gebruiken?

Nee, Logos werkt **eenmalig per repository**. Als je wijzigingen wilt maken aan een bestaande repository, gebruik dan de moeder-agent van die repository.

### Wat als ik een bestaand project wil migreren?

Gebruik Logos om een **nieuwe repository structuur** te maken en kopieer daarna de bestaande code naar de juiste locaties in de nieuwe structuur.

### Mag ik de constitutie aanpassen per project?

**Nee**, de constitutie is bindend voor alle projecten. Wel kun je **project-specifiek beleid** toevoegen in `<kit>-governance/beleid.md` dat consistent is met de constitutie.

### Hoe voeg ik een nieuwe agent toe?

Gebruik de **moeder-agent** van je project. Deze kan nieuwe sub-agents creëren met het `agent-file-template.md` als basis.

---

## Documentatie

- **Logos Agent**: [desc-agents/00-genesis-logos-agent.md](desc-agents/00-genesis-logos-agent.md)
- **Constitutie**: [constitutie.md](constitutie.md)
- **Handvest**: [handvest-logos.md](handvest-logos.md)
- **Agent Template**: [agent-file-template.md](agent-file-template.md)

---

## Licentie

Genesis is een intern framework. Gebruik binnen je organisatie is toegestaan volgens de principes in de constitutie.

---

## Contact

Voor vragen over Genesis, constitutie of handvest: zie de documentatie of neem contact op met de repository eigenaar.

---

**Laatst bijgewerkt**: 2025-12-11  
**Versie**: 1.0.0  
**Status**: Actief
