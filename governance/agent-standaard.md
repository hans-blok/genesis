# Agent Standaard voor Document-Repositories

**Versie**: 1.0  
**Datum**: 10 januari 2026  
**Status**: Bindend

---

## Doel

Dit document normeert de structuur, componenten en werking van agents in document-repositories. Het zorgt voor consistentie, herbruikbaarheid en duidelijkheid in agent-definities.

## Toepassingsgebied

Deze standaard geldt voor:
- Alle agents in document-repositories
- Agent definities in Genesis
- Herbruikbare agents in agent-capabilities
- Workspace-specifieke agents

---

## Agent Componenten

Elke agent bestaat uit **drie verplichte componenten**:

### 1. Rolbeschrijving (Interne Werking)

**Locatie**: `/governance/rolbeschrijvingen/<agent-naam>.md`

**Doel**: Beschrijft de interne werking, verantwoordelijkheden en grenzen van de agent voor menselijke gebruikers en andere agents.

**Karakter**: Documentatie en referentie

**Verplichte secties**:
```markdown
# Rolbeschrijving: <Agent Naam>

**Agent**: <workspace>.<agent-naam>
**Domein**: <kennisgebied>
**Type**: <type agent>

---

## Rol en Verantwoordelijkheid

[Beschrijving van de hoofdrol]

### Kerntaken

1. **<Taak 1>**
   - [Onderdelen]

2. **<Taak 2>**
   - [Onderdelen]

## Specialisaties

### <Specialisatie 1>
[Details]

### <Specialisatie 2>
[Details]

## Grenzen

### Wat <Agent> NIET doet
- ❌ [Beperking 1]
- ❌ [Beperking 2]

### Wat <Agent> WEL doet
- ✅ [Mogelijkheid 1]
- ✅ [Mogelijkheid 2]

## Werkwijze

### Bij <scenario 1>
[Stappen]

### Bij <scenario 2>
[Stappen]

## Communicatie

[Hoe de agent communiceert]

---

**Versie**: 1.0
**Laatst bijgewerkt**: <datum>
```

**Kenmerken**:
- **Uitgebreid**: Volledige beschrijving van werking
- **Mensvriendelijk**: Op B1 taalniveau
- **Stabiel**: Wijzigt niet vaak
- **Referentie**: Voor begrip en onboarding

### 2. Prompt (Contract)

**Locatie**: /.github/prompts/<agent-naam>.prompt.md

**Doel**: Definieert het contract tussen gebruiker en agent - wat gaat erin, wat komt eruit.

**Karakter**: Interface specificatie (geen gedetailleerde werkinstructies).

**Verplichte structuur**:
```markdown
---
agent: <workspace>.<agent-naam>
description: <Korte beschrijving>
---

# <Agent Naam> Prompt

## Rolbeschrijving

<Korte samenvatting van de rol>.

**VERPLICHT**: Lees governance/rolbeschrijvingen/<agent-naam>.md voor volledige context.

## Contract

### Input (Wat gaat erin)

**Verplichte parameters** (of vrije opdracht):
- <parameter1>: <beschrijving> (type: <type>)

**Optionele parameters**:
- <parameter2>: <beschrijving> (type: <type>, default: <waarde>)

### Output (Wat komt eruit)

Bij een geldige opdracht levert de agent altijd:
- Een korte samenvatting van de uitgevoerde of voorgenomen actie.
- Een overzicht van de belangrijkste resultaten of bevindingen.
- Eventuele waarschuwingen als iets afwijkt van governance of rolbeschrijving.

### Foutafhandeling

De agent:
- Stopt wanneer acties in strijd zouden zijn met governance of eigen grenzen.
- Vraagt om verduidelijking bij onduidelijke opdrachten of ontbrekende informatie.

## Werkwijze

Deze prompt is een contract op hoofdlijnen. Voor alle details over gedrag, scenario's en interne stappen verwijst de agent volledig naar governance/rolbeschrijvingen/<agent-naam>.md.

---

Documentatie: Zie governance/rolbeschrijvingen/<agent-naam>.md  
Runner: scripts/<agent-naam>.py
```

**Kenmerken**:
- Compact: alleen essentiële interface-informatie.
- Contract: duidelijk wat erin gaat en wat eruit komt.
- Actionable: direct bruikbaar door Copilot.
- Gescheiden verantwoordelijkheden: details staan in de rolbeschrijving, niet in de prompt.

### 3. Runner (Python Script)

**Locatie**: `/scripts/<agent-naam>.py`

**Doel**: Automatisering van agent taken zonder AI-interactie voor herhaalbare workflows.

**Karakter**: Executable automation

### Aanbevolen basisontwerp voor runners

Sommige agents bestaan uit meerdere vaste stappen (bijvoorbeeld: boundary → contract → rol → runner). Voor dit soort agents is het aanbevolen om **één hoofd-runner** te maken die meerdere operaties kan uitvoeren.

1) **Eén hoofd-runner per agent**
- Doet **routing**: kiest welke operatie hoort bij de opdracht.
- Doet **policy**: voert scope checks, quality gates en anti-pattern checks uit.
- Beheert **state**: geeft context door tussen operaties (bijvoorbeeld de boundary en gekozen parameters).
- Doet **logging/traceerbaarheid**: legt per operatie een kort artefact vast (wat is gedaan en welke bestanden zijn geraakt).

2) **Operation handlers (interne subroutines, geen aparte runners)**
- Per vaste stap één interne handler/functie (conceptueel):
    - boundary-definitie
    - prompt-design (contract)
    - rolbeschrijving genereren
    - runner genereren (voor de nieuwe agent)
- Deze handlers zijn **geen** losse `scripts/<stap>.py` runners; ze zijn onderdeel van dezelfde hoofd-runner.

Dit ontwerp houdt de automation consistent en voorkomt dat scope/quality checks per stap verschillen.

**Plaatsing van Output**:
- Agents die een **schema** (planning, overzicht, stappenplan) genereren, schrijven dit direct weg als Markdown-document in de daarvoor bedoelde documentstructuur (bijvoorbeeld onder `docs/` of `docs/resultaten/<agent-naam>/`).
- Agents die een **plan** (ontwerp, voorstel, werk-in-uitvoering) genereren, plaatsen dit standaard in de tijdelijke context-map `temp/` (bijvoorbeeld `temp/<onderwerp>-plan.md`).
- Structurele documenten voor eindgebruik (schema's, checklists, handleidingen) horen in `docs/` of onder `docs/resultaten/`.
- Tijdelijke of experimentele documenten (plannen, varianten, voorstellen) horen in `temp/` en worden niet gecommit.

**Toegestane Bestandsformaten**:
- Standaardagents in document-repositories genereren alleen:
    - Markdown-bestanden (`.md`) voor documentatie, schema's en rapporten.
    - Optioneel Python-scripts (`.py`) als onderdeel van automation of tooling.
- **Niet toegestaan voor standaardagents**:
    - Geen directe generatie van PDF-bestanden.
    - Geen directe generatie van HTML-bestanden of andere publicatieformaten.
    - Geen binaire documenten (zoals Word, PowerPoint) of afbeeldingen.
- **Uitzondering: Publisher-agent**:
    - De publisher-agent heeft als kerntaak het maken van publicatieformaten (bijvoorbeeld HTML) op basis van Markdown-bronbestanden.
    - Andere publicatieformaten (zoals PDF) zijn alleen toegestaan als dit expliciet is vastgelegd in de rolbeschrijving van de publisher.
    - Andere agents die publicatie nodig hebben, leveren hun output aan als Markdown en laten de omzetting naar andere formaten over aan de publisher.

**Verplichte structuur**:
```python
#!/usr/bin/env python3
"""
<Agent Naam> Runner

Automatiseert taken van de <agent-naam> agent zonder AI-interactie.

Usage:
    python scripts/<agent-naam>.py [options]

Requirements:
    - Python 3.8+
    - <dependencies>
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Constants
WORKSPACE_ROOT = Path(__file__).parent.parent
AGENT_NAME = "<agent-naam>"
VERSION = "1.0.0"


class <AgentNaam>Runner:
    """Runner voor <Agent Naam> agent."""
    
    def __init__(self, workspace_root: Path):
        """
        Initialiseer runner.
        
        Args:
            workspace_root: Root directory van de workspace
        """
        self.workspace_root = workspace_root
        self.governance_dir = workspace_root / "governance"
        self.docs_dir = workspace_root / "docs"
    
    def validate_input(self, **kwargs) -> bool:
        """
        Valideer input parameters.
        
        Args:
            **kwargs: Input parameters
            
        Returns:
            True als input geldig is
            
        Raises:
            ValueError: Als verplichte parameter ontbreekt
        """
        # Validatie logica
        required = ['param1', 'param2']
        for param in required:
            if param not in kwargs:
                raise ValueError(f"Verplichte parameter '{param}' ontbreekt")
        return True
    
    def run(self, **kwargs) -> Dict[str, any]:
        """
        Voer agent taak uit.
        
        Args:
            **kwargs: Input parameters
            
        Returns:
            Dictionary met output resultaten
        """
        # Valideer input
        self.validate_input(**kwargs)
        
        # Implementatie van agent logica
        results = {
            'success': True,
            'artifacts': [],
            'message': ''
        }
        
        # ... agent logica ...
        
        return results


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description=f'{AGENT_NAME} runner - Automatiseert agent taken'
    )
    
    # Verplichte argumenten
    parser.add_argument(
        'param1',
        help='Beschrijving van parameter 1'
    )
    
    # Optionele argumenten
    parser.add_argument(
        '--param2',
        default='default_waarde',
        help='Beschrijving van parameter 2'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Verbose output'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version=f'{AGENT_NAME} runner v{VERSION}'
    )
    
    args = parser.parse_args()
    
    # Maak runner en voer uit
    runner = <AgentNaam>Runner(WORKSPACE_ROOT)
    
    try:
        results = runner.run(
            param1=args.param1,
            param2=args.param2
        )
        
        if results['success']:
            print(f"✅ {AGENT_NAME} succesvol uitgevoerd")
            if results['artifacts']:
                print(f"\nAangemaakte/gewijzigde bestanden:")
                for artifact in results['artifacts']:
                    print(f"  - {artifact}")
        else:
            print(f"❌ {AGENT_NAME} gefaald: {results.get('message', 'Onbekende fout')}")
            sys.exit(1)
            
    except ValueError as e:
        print(f"❌ Validatie fout: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Onverwachte fout: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
```

**Kenmerken**:
- **Executable**: Direct uitvoerbaar zonder AI
- **Type-safe**: Met type hints
- **Error handling**: Duidelijke foutmeldingen
- **CLI**: Argument parsing met help
- **Testbaar**: Unit test vriendelijk

**Best practices voor runner code**:

1. **Import ordering**: Groepeer imports logisch
   ```python
   # Standaard library (stdlib)
   import sys
   from pathlib import Path
   
   # Third-party packages
   # (indien van toepassing)
   
   # Lokale imports
   from agent_naam.core import execute_operation
   ```

2. **Constanten**: Definieer magic numbers/strings bovenaan
   ```python
   # Policy constants
   MIN_BOUNDARY_LENGTH = 10
   FORBIDDEN_TERMS_DEFAULT = ("pdf", "html")
   MAX_RETRIES = 3
   DEFAULT_TIMEOUT = 30
   ```

3. **Type hints**: Gebruik moderne Python 3.10+ syntax
   ```python
   # Modern (voorkeur)
   def process(data: str | None = None) -> list[Path]:
       pass
   
   # Oudere stijl (vermijd indien Python 3.10+)
   from typing import Optional, List
   def process(data: Optional[str] = None) -> List[Path]:
       pass
   ```

4. **Exception handling**: Wees specifiek, vermijd bare `except`
   ```python
   # Goed
   try:
       rel = path.relative_to(workspace_root)
   except ValueError:
       # Path is not relative to workspace_root
       rel = str(path)
   
   # Vermijd
   except Exception:
       pass
   ```

5. **Exit codes**: Gebruik conventionele codes
   - `0`: success
   - `1`: algemene fout (validatie, policy, runtime)
   - `2`: misuse (syntax error, verkeerde argumenten) — alleen voor CLI parsing errors

6. **Template management**: Voor grote templates (prompt/rol/runner skeletons)
   - Overweeg aparte template-bestanden in `scripts/<agent_naam>/templates/`
   - Laad templates runtime in plaats van hardcoded strings
   - Maakt onderhoud en aanpassingen eenvoudiger

7. **Logging en traceability**: Leg acties vast
   - Print belangrijke stappen naar stdout
   - Errors naar stderr
   - Optioneel: schrijf trace/audit bestanden naar `temp/`
   - Overweeg `logging` module voor complexere runners

8. **Dataclasses**: Gebruik frozen dataclasses voor results
   ```python
   from dataclasses import dataclass
   
   @dataclass(frozen=True)
   class OperationResult:
       success: bool
       message: str
       artifacts: list[Path]
   ```

---

## Naamgevingsconventies

### Rolbeschrijving
- **Bestandsnaam**: `<agent-naam>.md` (lowercase, hyphens)
- **Locatie**: `governance/rolbeschrijvingen/`
- **Voorbeeld**: `governance/rolbeschrijvingen/logos.md`

### Prompt
- **Bestandsnaam**: `<agent-naam>.prompt.md`
- **Locatie**: `.github/prompts/`
- **Voorbeeld**: `.github/prompts/logos.prompt.md`

### Runner
- **Bestandsnaam**: `<agent-naam>.py`
- **Locatie**: `scripts/`
- **Voorbeeld**: `scripts/logos.py`
- **Class naam**: `<AgentNaam>Runner` (PascalCase)

### Agent Identifier
- **Format**: `<workspace>.<agent-naam>`
- **Voorbeelden**: 
  - `genesis.logos`
  - `dms.validator`
  - `tlx.analyzer`

---

## Agent Types

Agents kunnen verschillende types hebben:

### Technische Beheerder
**Voorbeelden**: Logos (git/github), validator, formatter

**Kenmerken**:
- Technische taken
- Geen domein kennis vereist
- Herbruikbaar over workspaces
- Focus op structuur en proces

### Domein Expert
**Voorbeelden**: Data modelleur, API designer, security reviewer

**Kenmerken**:
- Domein-specifieke kennis
- Workspace-gebonden
- Focus op inhoud en kwaliteit
- Adviserend

### Utility
**Voorbeelden**: Converter, extractor, reporter

**Kenmerken**:
- Ondersteunende taken
- Input → verwerking → output
- Vaak volledig geautomatiseerd
- Geen beslissingen

---

## Relaties tussen Componenten

```
┌─────────────────────────────────────────────────────────────┐
│                         Agent Ecosystem                      │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Gebruiker                                                    │
│     │                                                         │
│     ├─ Wil begrijpen ──────────► Rolbeschrijving            │
│     │                             (interne werking)          │
│     │                                                         │
│     ├─ Wil gebruiken ───────────► Prompt                     │
│     │                             (contract: in/uit)         │
│     │                                                         │
│     └─ Wil automatiseren ───────► Runner                     │
│                                    (Python script)           │
│                                                               │
│  GitHub Copilot                                              │
│     │                                                         │
│     ├─ Leest context ────────────► Rolbeschrijving          │
│     │                                                         │
│     └─ Volgt instructies ────────► Prompt                    │
│                                                               │
│  CI/CD Pipeline                                              │
│     │                                                         │
│     └─ Voert uit ────────────────► Runner                    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Flow: Ontwikkeling

1. **Ontwerp**: Beschrijf rol en verantwoordelijkheden (rolbeschrijving)
2. **Interface**: Definieer contract (prompt)
3. **Implementatie**: Bouw runner voor herhaalbare taken
4. **Test**: Valideer met runner in verschillende scenario's
5. **Document**: Zorg dat alle drie sync blijven

### Flow: Gebruik

**Handmatig (met AI)**:
```
Gebruiker → @github /agent → Copilot leest prompt + rolbeschrijving → Uitvoering
```

**Geautomatiseerd (zonder AI)**:
```
Gebruiker/CI → python scripts/agent.py → Uitvoering → Output
```

---

## Validatie Checklist

Bij het maken of reviewen van een agent:

### Rolbeschrijving
- [ ] Bestand bestaat in `governance/rolbeschrijvingen/`
- [ ] Bevat alle verplichte secties
- [ ] Op B1 taalniveau
- [ ] Duidelijke grenzen (WEL/NIET)
- [ ] Concrete voorbeelden
- [ ] Versieinformatie en datum

### Prompt
- [ ] Bestand bestaat in `.github/prompts/`
- [ ] Verwijst naar rolbeschrijving
- [ ] Duidelijk contract (input/output)
- [ ] Voorbeelden van gebruik
- [ ] Foutafhandeling beschreven
- [ ] Success criteria gedefinieerd

### Runner
- [ ] Python script bestaat in `scripts/`
- [ ] Executable permissions (indien Unix)
- [ ] Docstring met usage
- [ ] Type hints gebruikt
- [ ] Error handling aanwezig
- [ ] CLI argumenten gedocumenteerd
- [ ] Main guard (`if __name__ == '__main__'`)
- [ ] Bij multi-step agents: één hoofd-runner met interne operation handlers (geen losse stap-runners)
- [ ] Bij multi-step agents: twee lagen (frontdoor + core) of equivalent, zodat parsing/formatting los staat van policy/uitvoering

### Consistentie
- [ ] Alle drie componenten hebben zelfde `<agent-naam>`
- [ ] Versienummers zijn sync
- [ ] Beschrijvingen zijn consistent
- [ ] Input/output parameters matchen
- [ ] Voorbeelden kloppen over componenten heen

### Kwaliteit
- [ ] Geen conflicten met governance
- [ ] Volgt workspace standaarden
- [ ] Tests bestaan (indien complex)
- [ ] README updated met agent info

---

## Levenscyclus van een Agent

### 1. Creatie
1. Bepaal rol en scope
2. Schrijf rolbeschrijving in `governance/rolbeschrijvingen/`
3. Definieer contract in `.github/prompts/`
4. Implementeer runner in `scripts/`
5. Test handmatig en geautomatiseerd
6. Update workspace README

### 2. Onderhoud
- Rolbeschrijving: Review bij scope wijziging
- Prompt: Update bij interface changes
- Runner: Bug fixes en features
- Versioning: Sync alle componenten

### 3. Deprecation
1. Markeer als deprecated in alle drie componenten
2. Documenteer migratie pad
3. Behoud voor backwards compatibility
4. Na grace period: verwijder of archive

---

## Best Practices

### Rolbeschrijving
- **Wees specifiek**: "Controleert markdown links" i.p.v. "Verbetert documentatie"
- **Geef voorbeelden**: Concrete use cases
- **Definieer grenzen**: Duidelijk wat WEL en NIET
- **Update regelmatig**: Bij scope changes

### Prompt
- **Compactheid**: Kort maar volledig
- **Testbaarheid**: Success criteria meetbaar
- **Gebruiksvriendelijk**: Duidelijke voorbeelden
- **Error-first**: Beschrijf eerst wat fout kan gaan

### Runner
- **DRY principe**: Herbruikbare functies
- **Single responsibility**: Eén taak per runner
- **Fail fast**: Valideer vroeg
- **Logging**: Voor debugging en audit trail
- **Idempotent**: Meerdere runs = zelfde resultaat

### Algemeen
- **Consistency**: Sync tussen componenten
- **Versioning**: Semantic versioning
- **Testing**: Unit tests voor runner
- **Documentation**: Voorbeelden in README

---

## Voorbeeld: Agent Logos

### Structuur
```
governance/
  rolbeschrijvingen/
    logos.md                    # Interne werking
.github/
  prompts/
    logos.prompt.md            # Contract
scripts/
  logos.py                     # Runner
```

### Gebruik

**Met AI**:
```bash
@github /logos Analyseer repository structuur
```

**Zonder AI**:
```bash
python scripts/logos.py --check-structure --fix-naming
```

---

## Referenties

- [Workspace Standaard](workspace-standaard.md) - Folder structuur
- [Gedragscode Artikel 5](gedragscode.md#artikel-5) - Agent orkestratie
- [Genesis Beleid](beleid.md) - Agent scope in Genesis

---

**Maintained by**: Logos + Repository Owner  
**Status**: Bindend voor alle agents in document-repositories  
**Laatste review**: 10 januari 2026
