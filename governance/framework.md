# Framework — Development Value Stream

## Overzicht

Alle agents (behalve Logos) werken volgens het **SAFe framework** voor de development value stream. Dit framework beschrijft de fases van idee tot deployment en helpt agents hun positie in de workflow te begrijpen.

## Development Value Stream

```
A. Trigger → B. Architectuur → C. Specificatie → D. Ontwerp → E. Bouw → F. Validatie → G. Deployment
   ↓              ↓                   ↓               ↓           ↓           ↓              ↓
Business       ADR's            Requirements      API         Code        Tests        Release
Cases         Patterns         Datamodellen      Design      Generation   Validatie    Management
```

## Fases

### A. Trigger
**Doel**: Identificeren van zakelijke behoeften en kansen

**Artefacten**:
- Business cases
- Stakeholder input
- Probleemomschrijvingen
- Waardevragen

**Agents in deze fase**: Agents die business input verwerken en initiële analyse doen

---

### B. Architectuur
**Doel**: Architecturale beslissingen en patronen vastleggen

**Artefacten**:
- ADR's (Architecture Decision Records)
- Architectuur patronen
- Technische richtlijnen
- Infrastructuur keuzes

**Agents in deze fase**: Agents die architecturale beslissingen voorbereiden en documenteren

---

### C. Specificatie
**Doel**: Functionele en non-functionele requirements definiëren

**Artefacten**:
- Requirements documenten
- Datamodellen
- Use cases
- Acceptatiecriteria
- Entiteitsrelaties

**Agents in deze fase**: Agents die specificaties opstellen, datamodellen maken, requirements analyseren

---

### D. Ontwerp
**Doel**: Technisch ontwerp en API definitie

**Artefacten**:
- API designs
- Interface specificaties
- Component diagrammen
- Interaction designs

**Agents in deze fase**: Agents die technische ontwerpen maken op basis van specificaties

---

### E. Bouw
**Doel**: Code generatie en implementatie

**Artefacten**:
- Gegenereerde code
- Scripts
- Database migraties
- Configuraties

**Agents in deze fase**: Agents die code genereren, scripts maken, implementatie automatiseren

---

### F. Validatie
**Doel**: Testen en kwaliteitscontrole

**Artefacten**:
- Test rapporten
- Validatie resultaten
- Code reviews
- Performance metrics

**Agents in deze fase**: Agents die testen uitvoeren, kwaliteit valideren, compliance checken

---

### G. Deployment
**Doel**: Release en deployment management

**Artefacten**:
- Release notes
- Deployment scripts
- Rollback procedures
- Monitoring setup

**Agents in deze fase**: Agents die deployment voorbereiden en releases beheren

---

## U. Utility (Ondersteunende Agents)

**Doel**: Generieke taken die niet direct in de workflow passen

**Voorbeelden**:
- Format conversie (Markdown → XML, JSON → CSV, etc.)
- Document generatie
- Code formatting
- Data transformatie
- Template processing

**Agents in deze fase**: Agents die ondersteunende, cross-cutting taken uitvoeren

---

## Agent Positionering

### Moeder-Agent Verantwoordelijkheid

De **moeder-agent** plaatst elke nieuwe agent in een fase van de workflow:

1. **Agent creatie**: Moeder-agent vraagt om:
   - Naam van de agent
   - Domein van de agent
   - Context (wat doet de agent)

2. **Fase bepaling**: Op basis van de agent-context bepaalt de moeder-agent in welke fase de agent hoort

3. **Folder structuur**: Agent bestanden worden geplaatst in fase-folders:
   ```
   /.github/agents/
       /A-Trigger/
       /B-Architectuur/
       /C-Specificatie/
       /D-Ontwerp/
       /E-Bouw/
       /F-Validatie/
       /G-Deployment/
       /U-Utility/
   
   /.github/prompts/
       /A-Trigger/
       /B-Architectuur/
       /C-Specificatie/
       /D-Ontwerp/
       /E-Bouw/
       /F-Validatie/
       /G-Deployment/
       /U-Utility/
   
   /desc-agents/
       /A-Trigger/
       /B-Architectuur/
       /C-Specificatie/
       /D-Ontwerp/
       /E-Bouw/
       /F-Validatie/
       /G-Deployment/
       /U-Utility/
   ```

4. **Autonome plaatsing**: De moeder-agent neemt deze beslissing zelfstandig op basis van de agent-context

### Agent Naamgeving

**Formaat**: `<kit-naam>.<fase>.<agent-naam>`

**Voorbeelden**:
- `dms.C.specificeer` — Specificatie agent in DMS kit
- `tlx.E.genereer` — Code generatie agent in TLX kit
- `cmr.U.convert` — Utility conversie agent in CMR kit
- `gen.B.adr` — Architectuur beslissing agent in GEN kit

### Agent Bestanden

Voor een agent genaamd `dms.C.specificeer`:

```
/.github/agents/C-Specificatie/dms.C.specificeer.agent.md
/.github/prompts/C-Specificatie/dms.C.specificeer.prompt.md
/desc-agents/C-Specificatie/01-specificeer.md
```

**Volgnummering in beschrijvingen**:
- Binnen elke fase krijgen agents een volgnummer (01, 02, 03, etc.)
- Volgnummer bepaalt volgorde binnen de fase
- Utility agents krijgen ook volgnummers (01, 02, 03, etc.)

---

## Logos Uitzondering

**Logos heeft geen kennis van dit framework**:
- Logos werkt alleen volgens `constitutie.md` en `handvest-logos.md`
- Logos maakt de basis directory structuur zonder fase-folders
- De moeder-agent past de structuur aan door fase-folders toe te voegen
- De moeder-agent verplaatst eigen bestanden naar de juiste fase-folder

---

## Framework Evolutie

- Dit framework mag worden aangepast via expliciet updateproces
- Alleen de gebruiker mag het framework wijzigen
- Agents volgen het framework, maar mogen geen wijzigingen aanbrengen
- Bij onduidelijkheden meldt de agent dit aan de gebruiker

---

**Versie**: 1.0.0  
**Laatst Bijgewerkt**: 2025-12-13
