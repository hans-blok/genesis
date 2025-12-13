---
description: Maak of update de feature specificatie vanuit een natuurlijke taalbeschrijving van de feature.
handoffs: 
  - label: Bouw Technisch Plan
    agent: speckit.plan
    prompt: Maak een plan voor de spec. Ik bouw met...
  - label: Verduidelijk Spec Vereisten
    agent: speckit.clarify
    prompt: Verduidelijk specificatie-eisen
    send: true
---

## Gebruikersinvoer
2. **Conceptueel model** - Ontwerp entiteiten en relaties
```text
$ARGUMENTS
```

Je **MOET** de gebruikersinvoer overwegen voordat je verdergaat (indien niet leeg).

## Overzicht

De tekst die de gebruiker typte na `/speckit.specify` in het activerende bericht **is** de feature-beschrijving. Ga ervan uit dat je deze altijd beschikbaar hebt in dit gesprek, zelfs als `$ARGUMENTS` letterlijk hieronder verschijnt. Vraag de gebruiker niet om deze te herhalen, tenzij ze een leeg commando gaven.

Doe het volgende met die feature-beschrijving:

1. **Genereer een beknopte korte naam** (2-4 woorden) voor de branch:
   - Analyseer de feature-beschrijving en haal de meest betekenisvolle kernwoorden eruit
   - Maak een 2-4 woorden korte naam die de essentie van de feature vastlegt
   - Gebruik actie-zelfstandig naamwoord formaat waar mogelijk (bijv. "add-user-auth", "fix-payment-bug")
   - Behoud technische termen en acroniemen (OAuth2, API, JWT, etc.)
   - Houd het beknopt maar beschrijvend genoeg om de feature in één oogopslag te begrijpen
   - Voorbeelden:
     - "Ik wil gebruikersauthenticatie toevoegen" → "user-auth"
     - "Implementeer OAuth2 integratie voor de API" → "oauth2-api-integration"
     - "Maak een dashboard voor analytics" → "analytics-dashboard"
     - "Repareer payment processing timeout bug" → "fix-payment-timeout"

2. **Controleer op bestaande branches voordat je een nieuwe maakt**:
   
   a. Haal eerst alle remote branches op om te zorgen dat we de laatste informatie hebben:
      ```bash
      git fetch --all --prune
      ```
   
   b. Vind het hoogste feature-nummer over alle bronnen voor de korte-naam:
      - Remote branches: `git ls-remote --heads origin | grep -E 'refs/heads/[0-9]+-<short-name>$'`
      - Lokale branches: `git branch | grep -E '^[* ]*[0-9]+-<short-name>$'`
      - Specs directories: Controleer op directories die matchen met `specs/[0-9]+-<short-name>`
   
   c. Bepaal het volgende beschikbare nummer:
      - Extraheer alle nummers uit alle drie de bronnen
      - Vind het hoogste nummer N
      - Gebruik N+1 voor het nieuwe branch-nummer
   
   d. Voer het script uit `.specify/scripts/powershell/create-new-feature.ps1 -Json "$ARGUMENTS"` met het berekende nummer en korte-naam:
      - Geef `--number N+1` en `--short-name "jouw-korte-naam"` mee samen met de feature-beschrijving
      - Bash voorbeeld: `.specify/scripts/powershell/create-new-feature.ps1 -Json "$ARGUMENTS" --json --number 5 --short-name "user-auth" "Add user authentication"`
      - PowerShell voorbeeld: `.specify/scripts/powershell/create-new-feature.ps1 -Json "$ARGUMENTS" -Json -Number 5 -ShortName "user-auth" "Add user authentication"`
   
   **BELANGRIJK**:
   - Controleer alle drie de bronnen (remote branches, lokale branches, specs directories) om het hoogste nummer te vinden
   - Match alleen branches/directories met het exacte korte-naam patroon
   - Als geen bestaande branches/directories gevonden met deze korte-naam, start met nummer 1
   - Je mag dit script slechts één keer per feature uitvoeren
   - De JSON wordt in de terminal als output gegeven - verwijs daar altijd naar om de werkelijke content te krijgen die je zoekt
   - De JSON output bevat BRANCH_NAME en SPEC_FILE paden
   - Voor enkele quotes in args zoals "I'm Groot", gebruik escape syntax: bijv 'I'\''m Groot' (of dubbele quote indien mogelijk: "I'm Groot")

3. Laad `.specify/templates/spec-template.md` om de vereiste secties te begrijpen.

4. Volg deze uitvoeringsstroom:

    1. Parse gebruikersbeschrijving uit Input
       Indien leeg: ERROR "Geen feature-beschrijving gegeven"
    2. Extraheer kernconcepten uit beschrijving
       Identificeer: actoren, acties, data, beperkingen
    3. Voor onduidelijke aspecten:
       - Maak geïnformeerde gissingen gebaseerd op context en industrie-standaarden
       - Markeer alleen met [VERDUIDELIJKING NODIG: specifieke vraag] als:
         - De keuze de feature-scope of gebruikerservaring significant beïnvloedt
         - Meerdere redelijke interpretaties bestaan met verschillende implicaties
         - Geen redelijke standaard bestaat
       - **LIMIET: Maximum 3 [VERDUIDELIJKING NODIG] markeringen totaal**
       - Prioriteer verduidelijkingen op impact: scope > security/privacy > gebruikerservaring > technische details
    4. Vul User Scenarios & Testing sectie in
       Indien geen duidelijke gebruikersstroom: ERROR "Kan gebruikersscenario's niet bepalen"
    5. Genereer Functionele Eisen
       Elke eis moet testbaar zijn
       Gebruik redelijke standaarden voor niet-gespecificeerde details (documenteer aannames in Aannames sectie)
    6. Definieer Succescriteria
       Creëer meetbare, technologie-agnostische uitkomsten
       Include zowel kwantitatieve metrics (tijd, performance, volume) als kwalitatieve maten (gebruikerstevredenheid, taak-voltooiing)
       Elk criterium moet verifieerbaar zijn zonder implementatie-details
    7. Identificeer Kernentiteiten (indien data betrokken)
    8. Return: SUCCESS (spec klaar voor planning)

5. Schrijf de specificatie naar SPEC_FILE met behulp van de template-structuur, vervang placeholders met concrete details afgeleid van de feature-beschrijving (argumenten) terwijl je de sectie-volgorde en headers behoudt.

6. **Specificatie Kwaliteitsvalidatie**: Na het schrijven van de initiële spec, valideer deze tegen kwaliteitscriteria:

   a. **Maak Spec Kwaliteit Checklist**: Genereer een checklist-bestand op `FEATURE_DIR/checklists/requirements.md` met behulp van de checklist template-structuur met deze validatie-items:

      ```markdown
      # Specificatie Kwaliteit Checklist: [FEATURE NAAM]
      
      **Doel**: Valideer specificatie volledigheid en kwaliteit voordat je verdergaat met planning
      **Aangemaakt**: [DATUM]
      **Feature**: [Link naar spec.md]
      
      ## Inhoudskwaliteit
      
      - [ ] Geen implementatie-details (talen, frameworks, APIs)
      - [ ] Gericht op gebruikerswaarde en zakelijke behoeften
      - [ ] Geschreven voor niet-technische stakeholders
      - [ ] Alle verplichte secties voltooid
      
      ## Eis Volledigheid
      
      - [ ] Geen [VERDUIDELIJKING NODIG] markeringen over
      - [ ] Requirements are testable and unambiguous
      - [ ] Success criteria are measurable
      - [ ] Success criteria are technology-agnostic (no implementation details)
      - [ ] All acceptance scenarios are defined
      - [ ] Edge cases are identified
      - [ ] Scope is clearly bounded
      - [ ] Dependencies and assumptions identified
      
      ## Feature Readiness
      
      - [ ] All functional requirements have clear acceptance criteria
      - [ ] User scenarios cover primary flows
      - [ ] Feature meets measurable outcomes defined in Success Criteria
      - [ ] No implementation details leak into specification
      
      ## Notes
      
      - Items marked incomplete require spec updates before `/speckit.clarify` or `/speckit.plan`
      ```

   b. **Run Validation Check**: Review the spec against each checklist item:
      - For each item, determine if it passes or fails
      - Document specific issues found (quote relevant spec sections)

   c. **Handle Validation Results**:

      - **If all items pass**: Mark checklist complete and proceed to step 6

      - **If items fail (excluding [NEEDS CLARIFICATION])**:
        1. List the failing items and specific issues
        2. Update the spec to address each issue
        3. Re-run validation until all items pass (max 3 iterations)
        4. If still failing after 3 iterations, document remaining issues in checklist notes and warn user

      - **If [NEEDS CLARIFICATION] markers remain**:
        1. Extract all [NEEDS CLARIFICATION: ...] markers from the spec
        2. **LIMIT CHECK**: If more than 3 markers exist, keep only the 3 most critical (by scope/security/UX impact) and make informed guesses for the rest
        3. For each clarification needed (max 3), present options to user in this format:

           ```markdown
           ## Question [N]: [Topic]
           
           **Context**: [Quote relevant spec section]
           
           **What we need to know**: [Specific question from NEEDS CLARIFICATION marker]
           
           **Suggested Answers**:
           
           | Option | Answer | Implications |
           |--------|--------|--------------|
           | A      | [First suggested answer] | [What this means for the feature] |
           | B      | [Second suggested answer] | [What this means for the feature] |
           | C      | [Third suggested answer] | [What this means for the feature] |
           | Custom | Provide your own answer | [Explain how to provide custom input] |
           
           **Your choice**: _[Wait for user response]_
           ```

        4. **CRITICAL - Table Formatting**: Ensure markdown tables are properly formatted:
           - Use consistent spacing with pipes aligned
           - Each cell should have spaces around content: `| Content |` not `|Content|`
           - Header separator must have at least 3 dashes: `|--------|`
           - Test that the table renders correctly in markdown preview
        5. Number questions sequentially (Q1, Q2, Q3 - max 3 total)
        6. Present all questions together before waiting for responses
        7. Wait for user to respond with their choices for all questions (e.g., "Q1: A, Q2: Custom - [details], Q3: B")
        8. Update the spec by replacing each [NEEDS CLARIFICATION] marker with the user's selected or provided answer
        9. Re-run validation after all clarifications are resolved

   d. **Update Checklist**: After each validation iteration, update the checklist file with current pass/fail status

7. Report completion with branch name, spec file path, checklist results, and readiness for the next phase (`/speckit.clarify` or `/speckit.plan`).

**NOTE:** The script creates and checks out the new branch and initializes the spec file before writing.

## General Guidelines

## Quick Guidelines

- Focus on **WHAT** users need and **WHY**.
- Avoid HOW to implement (no tech stack, APIs, code structure).
- Written for business stakeholders, not developers.
- DO NOT create any checklists that are embedded in the spec. That will be a separate command.

### Section Requirements

- **Mandatory sections**: Must be completed for every feature
- **Optional sections**: Include only when relevant to the feature
- When a section doesn't apply, remove it entirely (don't leave as "N/A")

### For AI Generation

When creating this spec from a user prompt:

1. **Make informed guesses**: Use context, industry standards, and common patterns to fill gaps
2. **Document assumptions**: Record reasonable defaults in the Assumptions section
3. **Limit clarifications**: Maximum 3 [NEEDS CLARIFICATION] markers - use only for critical decisions that:
   - Significantly impact feature scope or user experience
   - Have multiple reasonable interpretations with different implications
   - Lack any reasonable default
4. **Prioritize clarifications**: scope > security/privacy > user experience > technical details
5. **Think like a tester**: Every vague requirement should fail the "testable and unambiguous" checklist item
6. **Common areas needing clarification** (only if no reasonable default exists):
   - Feature scope and boundaries (include/exclude specific use cases)
   - User types and permissions (if multiple conflicting interpretations possible)
   - Security/compliance requirements (when legally/financially significant)

**Examples of reasonable defaults** (don't ask about these):

- Data retention: Industry-standard practices for the domain
- Performance targets: Standard web/mobile app expectations unless specified
- Error handling: User-friendly messages with appropriate fallbacks
- Authentication method: Standard session-based or OAuth2 for web apps
- Integration patterns: RESTful APIs unless specified otherwise

### Success Criteria Guidelines

Success criteria must be:

1. **Measurable**: Include specific metrics (time, percentage, count, rate)
2. **Technology-agnostic**: No mention of frameworks, languages, databases, or tools
3. **User-focused**: Describe outcomes from user/business perspective, not system internals
4. **Verifiable**: Can be tested/validated without knowing implementation details

**Good examples**:

- "Users can complete checkout in under 3 minutes"
- "System supports 10,000 concurrent users"
- "95% of searches return results in under 1 second"
- "Task completion rate improves by 40%"

**Bad examples** (implementation-focused):

- "API response time is under 200ms" (too technical, use "Users see results instantly")
- "Database can handle 1000 TPS" (implementation detail, use user-facing metric)
- "React components render efficiently" (framework-specific)
- "Redis cache hit rate above 80%" (technology-specific)
