# Workspace Context - Genesis

**Datum**: 10 januari 2026  
**Status**: Template voor andere workspaces

---

## Workspace Doel

Genesis is een basisrepository voor het standaardiseren en onderhouden van document-repositories. Het bevat governance documenten, workspace standaarden en initialisatie scripts voor nieuwe workspaces.

## Context

Deze workspace richt zich op:
- Het definiëren van standaarden voor document-repositories
- Het documenteren van governance regels (gedragscode)
- Het beschrijven van agent componenten en hun werking
- Het aanbieden van templates en initialisatie scripts
- Het leveren en beheren van basis agents voor nieuwe workspaces

## Scope

### Wat valt binnen deze workspace:
- Governance documenten (gedragscode, workspace-standaard, agent-standaard)
- Standaarden voor folderstructuur en naamgeving
- Agent Logos (Genesis-specifiek)
- Agent Moeder (basisworkspace-ordenaar)
- Agent Rolbeschrijver (herbruikbaar voor alle workspaces)
- Agent Presentatie Architect (kaders voor presentatie en documentstructuur)
- Agent Publisher (publicatie naar GitHub Pages)
- Templates voor documenten en rolbeschrijvingen
- Initialisatie scripts (init-workspace.py, create-agent.py)
- Editor configuraties

### Wat valt NIET binnen deze workspace:
- Domein-specifieke documentatie
- Applicatie code of development frameworks
- Data of assets
- Project-specifieke agents (buiten basis agents)

## Benodigde Agents

### Huidige Agents
1. **Logos** (genesis.logos)
   - Type: Technische Beheerder
   - Doel: Git/GitHub expert voor Genesis repository structurering
   - Status: Volledig geïmplementeerd (rolbeschrijving + prompt)

2. **Moeder** (genesis.moeder)
   - Type: Technische Beheerder
   - Doel: Bewaakt de ordening en basisstructuur van workspaces
   - Status: Volledig geïmplementeerd (rolbeschrijving + prompt)

3. **Rolbeschrijver** (genesis.rolbeschrijver)
   - Type: Domein Expert
   - Doel: Specialist in agent documentatie en rolbeschrijvingen
   - Status: Volledig geïmplementeerd (rolbeschrijving + prompt)

4. **Presentatie Architect** (genesis.presentatie-architect)
   - Type: Domein Expert
   - Doel: Ontwerpt kaders voor presentatie en documentstructuur
   - Status: Volledig geïmplementeerd (rolbeschrijving + prompt)

5. **Publisher** (genesis.publisher)
   - Type: Technische Beheerder / Utility
   - Doel: Publiceert documentatie naar GitHub Pages, binnen de kaders van de Presentatie Architect
   - Status: Volledig geïmplementeerd (rolbeschrijving + prompt)

### Voorgestelde Agents
6. **Contract-schrijver** (genesis.contract-schrijver)
   - Type: Domein Expert
   - Doel: Specialist in het schrijven van agent prompts (contract: in/uit)
   - Motivatie: Complement van rolbeschrijver, focus op interface definitie

7. **Validator** (genesis.validator)
   - Type: Utility
   - Doel: Valideert workspace tegen standaarden en governance
   - Motivatie: Automatische kwaliteitscontrole

## Target Audience

- Ontwikkelaars die document-repositories opzetten
- Teams die governance willen implementeren
- Organisaties met meerdere documentatie repositories
- Gebruikers die snel een nette workspace willen initialiseren

## Taal

Nederlands (B1 niveau conform gedragscode)

## Relaties met andere Repositories

Genesis dient als bron voor:
- Workspace-specifieke repositories die deze standaarden overnemen
- Agent-capabilities repository met herbruikbare agents
- Project repositories die agents inzetten

## Voorbeeld Workspaces

### Kerstmenu
**Doel**: Planning en documentatie van kerstmenu's met recepten, inkoop lijsten en tijdsplanning

**Scope WEL**:
- Kerstmenu recepten (hoofdgerechten, bijgerechten, desserts)
- Inkoop lijsten per recept
- Tijdsplanning (voorbereiding, kooktijd)
- Menu samenstelling (welke gerechten combineren)

**Scope NIET**:
- Algemene recepten (niet-kerst gerelateerd)
- Budget calculatie (alleen inkoop lijsten)
- Gasten administratie
- Decoratie ideeën

**Agents**: moeder (kerstmenu.moeder), rolbeschrijver (kerstmenu.rolbeschrijver)

**Initialisatie**:
```bash
python genesis\scripts\init-workspace.py --name "kerstmenu" --context "genesis\temp\kerstmenu-context.md"
```

---

**Note**: Dit bestand wordt gebruikt als input voor het opstellen van `governance/beleid.md` en het definiëren van agents. Het blijft lokaal in de `/temp` folder en wordt niet gecommit.
