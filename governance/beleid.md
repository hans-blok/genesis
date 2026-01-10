# Genesis Workspace Beleid

**Versie**: 1.0  
**Datum**: 10 januari 2026  
**Taal**: Nederlands  
**Status**: Actief

---

## Context

Genesis is een basisrepository voor het initialiseren en standaardiseren van document-repositories. Het dient als fundament waaruit nieuwe workspaces worden opgezet met een consistente structuur, governance en agent-framework.

Genesis bevat geen applicatie code, maar governance documenten, standaarden, templates en de definitie van Agent Logos - de Git en GitHub expert voor repository beheer.

## Scope

### Wat valt binnen de scope van Genesis:

**Governance en Standaardisatie**:
- ✅ Constitutie (gedragscode) die geldt voor alle repositories
- ✅ Workspace standaarden voor folderstructuur en naamgeving
- ✅ Markdown formatting standaarden
- ✅ Git/GitHub best practices documentatie

**Agent Definities**:
- ✅ Agent Logos definitie en rolbeschrijving
- ✅ Agent templates voor nieuwe workspaces
- ✅ Prompt bestanden voor agents

**Templates en Voorbeelden**:
- ✅ Document templates (rolbeschrijvingen, procedures, etc.)
- ✅ README templates
- ✅ Beleid templates voor nieuwe workspaces

**Configuratie Standaarden**:
- ✅ Git ignore patterns voor document-repositories
- ✅ Editor configuraties (vim, copilot)
- ✅ GitHub configuratie voorbeelden

**Documentatie over Genesis**:
- ✅ Hoe Genesis te gebruiken
- ✅ Hoe nieuwe workspaces te initialiseren
- ✅ Uitleg van governance model

## Niet in Scope

### Wat valt NIET binnen de scope van Genesis:

**Domein-specifieke Content**:
- ❌ Business procedures of policies van specifieke projecten
- ❌ Domein-specifieke technische documentatie
- ❌ Project-specifieke requirements of specificaties
- ❌ Inhoudelijke documentatie van andere workspaces

**Applicatie Ontwikkeling**:
- ❌ Source code of applicatie logic
- ❌ Build tools en deployment scripts
- ❌ Test frameworks en test code
- ❌ Database schemas of migrations

**Operationele Zaken**:
- ❌ Deployment procedures voor specifieke applicaties
- ❌ Monitoring en alerting configuratie
- ❌ Infrastructure as Code
- ❌ Secrets management

**Sub-Agents**:
- ❌ Domein-specifieke agents (die horen in workspace repositories)
- ❌ Workflow-specifieke agents (A-G fases, U-utility)
- ❌ Moeder-agents van andere workspaces

**Data en Assets**:
- ❌ Binaire bestanden (behalve kleine voorbeelden)
- ❌ Grote media bestanden
- ❌ Data dumps of exports
- ❌ Wachtwoorden, keys of credentials

## Agent Werking

### Agent Logos

**Rol**: Git en GitHub expert voor repository beheer

**Verantwoordelijkheden** in Genesis context:
- Onderhouden van workspace-standaard.md
- Valideren van Genesis structuur tegen eigen standaarden
- Adviseren over git/github best practices
- Zorgen voor consistente markdown formatting

**Niet verantwoordelijk** in Genesis context:
- Inhoudelijke wijzigingen aan constitutie (alleen redactioneel indien toegestaan)
- Maken van domein-specifieke agents
- Business beslissingen over governance regels

### Toekomstige Agents

Genesis bevat alleen Agent Logos. Andere agents worden gedefinieerd in:
- **agent-capabilities**: Herbruikbare agent definities
- **workspace repositories**: Domein-specifieke agents

## Kwaliteitsnormen

### Documentatie
- Alle documenten in Nederlands
- Taalniveau B1 (conform Constitutie Artikel 2)
- Markdown (.md) format
- Duidelijke structuur met logische headings

### Structuur
- Conform workspace-standaard.md
- Lowercase folder en bestandsnamen
- Gebruik hyphens in plaats van spaties
- Maximaal 3 niveaus diep

### Governance
- Geen conflicten met constitutie
- Duidelijke scope afbakening
- Traceerbare beslissingen
- Versiebeheer van belangrijke documenten

### Git/GitHub
- Meaningful commit messages
- Geen grote binaire bestanden
- README altijd up-to-date
- .gitignore correct geconfigureerd

## Bijdragen aan Genesis

### Wie mag bijdragen
Genesis wordt onderhouden door:
- Repository owner
- Agent Logos (voor structuur en formatting)
- Contributors met expliciete toestemming

### Proces voor wijzigingen

**Governance documenten** (gedragscode.md):
- Alleen inhoudelijke wijzigingen door mensen
- Logos mag alleen redactioneel verbeteren (zie Constitutie Artikel 8)
- Vereist review en goedkeuring

**Standaarden** (workspace-standaard.md):
- Voorstellen via issues
- Discussie en consensus
- Implementatie door Logos

**Templates**:
- Kunnen vrij worden toegevoegd/aangepast
- Moeten voldoen aan markdown standaarden
- Review door Logos voor formatting

**Agent definities**:
- Wijzigingen aan Logos via PR
- Review vereist
- Testing in test-workspace

## Relatie met Andere Repositories

### Genesis → Workspace Repositories
Genesis dient als **bron** voor:
- Governance documenten (worden gekopieerd)
- Templates (worden hergebruikt)
- Standaarden (worden gevolgd)
- Agent Logos definitie (wordt gebruikt)

### Genesis ← Workspace Repositories
Genesis wordt **niet beïnvloed** door:
- Domein-specifieke policies
- Workspace-specifieke agents
- Project-specifieke templates

Feedback van workspaces kan wel leiden tot verbeteringen in Genesis standaarden.

## Versiebeheer

- **Versie 1.0** (2026-01-10): Initiële opzet met Logos en basis governance
- Belangrijke wijzigingen worden gedocumenteerd
- Breaking changes krijgen nieuw major versie nummer

## Contact en Ondersteuning

Voor vragen over Genesis:
- Raadpleeg de documentatie in `/docs` (indien aanwezig)
- Review governance documenten in `/governance`
- Gebruik Logos voor structuur en formatting vragen

---

**Maintained by**: Repository Owner + Agent Logos  
**Status**: Actief en bindend voor Genesis workspace  
**Laatste review**: 10 januari 2026
