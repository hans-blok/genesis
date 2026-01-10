#!/usr/bin/env python3
"""
Workspace Initialisatie Script

Maakt een nieuwe document-repository workspace aan met:
- Folderstructuur volgens workspace-standaard
- Governance documenten van Genesis
- Agent moeder en rolbeschrijver
- Beleid.md gegenereerd uit context
- Git repository initialisatie

Gebruik:
    python scripts/init-workspace.py --name "mijn-workspace" --description "Korte omschrijving"
    python scripts/init-workspace.py --name "kerstmenu" --context "temp/kerstmenu-context.md"
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path
from datetime import date


def print_header(text):
    """Print een header met emoji en lijnen"""
    print(f"\n🚀 {text}")
    print("━" * 60)


def print_step(text):
    """Print een stap met checkmark"""
    print(f"✅ {text}")


def print_error(text):
    """Print een error met cross"""
    print(f"❌ ERROR: {text}", file=sys.stderr)


def print_warning(text):
    """Print een waarschuwing"""
    print(f"⚠️  WAARSCHUWING: {text}")


def validate_name(name):
    """Valideer workspace naam volgens conventies"""
    if not name:
        return False, "Naam mag niet leeg zijn"
    
    if not name.islower():
        return False, "Naam moet lowercase zijn"
    
    if " " in name:
        return False, "Gebruik hyphens i.p.v. spaties"
    
    if not all(c.isalnum() or c == "-" for c in name):
        return False, "Alleen letters, cijfers en hyphens toegestaan"
    
    return True, ""


def workspace_exists(name, parent_dir):
    """Controleer of workspace al bestaat"""
    workspace_path = Path(parent_dir) / name
    return workspace_path.exists()


def get_genesis_root():
    """Vind de Genesis root directory"""
    script_dir = Path(__file__).parent
    genesis_root = script_dir.parent
    return genesis_root


def create_folders(workspace_path):
    """Maak folderstructuur aan volgens workspace-standaard"""
    folders = [
        "docs",
        "governance/rolbeschrijvingen",
        "templates",
        "scripts",
        ".github/prompts",
        "temp"
    ]
    
    for folder in folders:
        folder_path = workspace_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
    
    return folders


def copy_governance_documents(genesis_root, workspace_path):
    """Kopieer governance documenten van Genesis"""
    governance_files = [
        "governance/gedragscode.md",
        "governance/workspace-standaard.md",
        "governance/agent-standaard.md"
    ]
    
    for file in governance_files:
        src = genesis_root / file
        dst = workspace_path / file
        
        if src.exists():
            shutil.copy2(src, dst)
        else:
            print_warning(f"Governance bestand niet gevonden: {file}")
    
    return governance_files


def extract_section(content, header):
    """Extract een sectie uit markdown content"""
    lines = content.split("\n")
    in_section = False
    section_lines = []
    
    for line in lines:
        if line.startswith("### ") and header.lower() in line.lower():
            in_section = True
            continue
        elif line.startswith("### ") and in_section:
            break
        elif in_section and line.strip():
            section_lines.append(line)
    
    return "\n".join(section_lines).strip()


def generate_beleid(workspace_name, description, context_content):
    """Genereer beleid.md uit context"""
    
    # Extract secties uit context
    scope_wel = extract_section(context_content, "Wat valt binnen")
    scope_niet = extract_section(context_content, "Wat valt NIET binnen")
    
    # Basis template
    beleid = f"""# Beleid: {workspace_name.capitalize()} Workspace

**Versie**: 1.0  
**Datum**: {date.today().strftime('%d %B %Y')}

---

## Context

{description}

## Scope

### WEL binnen deze workspace

{scope_wel if scope_wel else "- [TODO: Definieer wat binnen scope valt]"}

### NIET binnen deze workspace

{scope_niet if scope_niet else "- [TODO: Definieer wat buiten scope valt]"}

## Agents

### Moeder ({workspace_name}.moeder)
**Rol**: Git/GitHub expert en workspace ordening  
**Verantwoordelijk voor**: Repository structuur, Git workflows, markdown formatting, naamgevingsconventies

**Zie**: `governance/rolbeschrijvingen/moeder.md`

### Rolbeschrijver ({workspace_name}.rolbeschrijver)
**Rol**: Agent documentatie specialist  
**Verantwoordelijk voor**: Rolbeschrijvingen maken voor nieuwe agents volgens agent-standaard

**Zie**: `governance/rolbeschrijvingen/rolbeschrijver.md`

## Kwaliteitsnormen

Conform governance documenten:
- **Gedragscode**: B1 taalniveau, fatsoenlijke omgangsvormen, testbare normen
- **Workspace-standaard**: Folderstructuur, naamgeving, markdown formatting
- **Agent-standaard**: 3-component model (rolbeschrijving, prompt, runner)

### Specifieke normen voor deze workspace

- [ ] Documenten in B1 Nederlands
- [ ] Bestandsnamen lowercase met hyphens
- [ ] Markdown formatting volgens standaard
- [ ] Scope wordt gerespecteerd (WEL/NIET)
- [ ] Nieuwe agents conform agent-standaard

---

**Let op**: Dit beleid is gegenereerd bij workspace initialisatie.  
Pas aan indien scope of agents wijzigen.
"""
    
    return beleid


def copy_agent(agent_name, genesis_root, workspace_path, workspace_name):
    """Kopieer agent componenten en pas aan voor workspace"""
    
    # 1. Rolbeschrijving
    rolbeschrijving_src = genesis_root / f"governance/rolbeschrijvingen/{agent_name}.md"
    rolbeschrijving_dst = workspace_path / f"governance/rolbeschrijvingen/{agent_name}.md"
    
    if rolbeschrijving_src.exists():
        content = rolbeschrijving_src.read_text(encoding="utf-8")
        # Vervang genesis. met workspace.
        content = content.replace(f"genesis.{agent_name}", f"{workspace_name}.{agent_name}")
        rolbeschrijving_dst.write_text(content, encoding="utf-8")
    
    # 2. Prompt
    prompt_src = genesis_root / f".github/prompts/{agent_name}.prompt.md"
    prompt_dst = workspace_path / f".github/prompts/{agent_name}.prompt.md"
    
    if prompt_src.exists():
        content = prompt_src.read_text(encoding="utf-8")
        content = content.replace(f"genesis.{agent_name}", f"{workspace_name}.{agent_name}")
        prompt_dst.write_text(content, encoding="utf-8")
    
    # 3. Runner (optioneel, kan nog niet bestaan)
    runner_src = genesis_root / f"scripts/{agent_name}.py"
    runner_dst = workspace_path / f"scripts/{agent_name}.py"
    
    if runner_src.exists():
        shutil.copy2(runner_src, runner_dst)


def copy_create_agent_script(genesis_root, workspace_path):
    """Kopieer create-agent.py script"""
    src = genesis_root / "scripts/create-agent.py"
    dst = workspace_path / "scripts/create-agent.py"
    
    if src.exists():
        shutil.copy2(src, dst)
        return True
    else:
        print_warning("create-agent.py niet gevonden in Genesis")
        return False


def generate_readme(workspace_name, description, workspace_path):
    """Genereer README.md voor workspace"""
    
    readme = f"""# {workspace_name.capitalize()}

{description}

## Structuur

```
{workspace_name}/
├── docs/                    # Documentatie
├── governance/              # Governance documenten
│   ├── gedragscode.md
│   ├── workspace-standaard.md
│   ├── agent-standaard.md
│   ├── beleid.md           # Workspace-specifiek beleid
│   └── rolbeschrijvingen/  # Agent rolbeschrijvingen
├── templates/               # Templates
├── scripts/                 # Scripts en runners
├── .github/
│   └── prompts/            # Agent prompts
└── temp/                    # Tijdelijke context (niet in git)
```

## Agents

### Moeder ({workspace_name}.moeder)
Git en GitHub expert + workspace ordening

**Gebruik**:
```
@github /moeder Richt workspace in volgens standaard
@github /moeder Valideer markdown formatting
```

### Rolbeschrijver ({workspace_name}.rolbeschrijver)
Specialist in agent documentatie

**Gebruik**:
```
@github /rolbeschrijver agent-naam=mijn-agent doel="..." domein="..."
```

## Nieuwe Agent Toevoegen

```bash
# 1. Maak rolbeschrijving met rolbeschrijver agent
@github /rolbeschrijver agent-naam=mijn-agent doel="Korte omschrijving" domein="kennisgebied"

# 2. Genereer agent skeletons (prompt + runner)
python scripts/create-agent.py mijn-agent

# 3. Vul prompt contract in
# Edit: .github/prompts/mijn-agent.prompt.md

# 4. Test agent
@github /mijn-agent [opdracht]
```

## Governance

Deze workspace volgt de governance standaarden uit Genesis:
- **Gedragscode**: B1 Nederlands, fatsoenlijk, testbaar
- **Workspace-standaard**: Folders, naamgeving, markdown
- **Agent-standaard**: 3 componenten (rolbeschrijving, prompt, runner)

Zie `governance/beleid.md` voor workspace-specifiek beleid en scope.

---

**Versie**: 1.0  
**Aangemaakt**: {date.today().strftime('%d %B %Y')}  
**Geïnitialiseerd met**: Genesis init-workspace.py
"""
    
    readme_path = workspace_path / "README.md"
    readme_path.write_text(readme, encoding="utf-8")


def generate_gitignore(workspace_path):
    """Genereer .gitignore voor workspace"""
    
    gitignore = """# Conform workspace-standaard.md

# Tijdelijke context folder
/temp/

# Editor bestanden
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# OS bestanden
.DS_Store
Thumbs.db
desktop.ini

# Python
__pycache__/
*.py[cod]
*$py.class
.pytest_cache/
*.egg-info/
dist/
build/

# Notities en drafts
*.draft.md
*.wip.md
"""
    
    gitignore_path = workspace_path / ".gitignore"
    gitignore_path.write_text(gitignore, encoding="utf-8")


def git_init(workspace_path, workspace_name):
    """Initialiseer Git repository"""
    try:
        # Git init
        subprocess.run(["git", "init"], cwd=workspace_path, check=True, 
                      capture_output=True, text=True)
        
        # Git add
        subprocess.run(["git", "add", "."], cwd=workspace_path, check=True,
                      capture_output=True, text=True)
        
        # Git commit
        commit_msg = f"Initial commit: {workspace_name} workspace structure"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=workspace_path, 
                      check=True, capture_output=True, text=True)
        
        return True
    except subprocess.CalledProcessError as e:
        print_warning(f"Git initialisatie gefaald: {e}")
        return False


def print_success_message(workspace_name, workspace_path):
    """Print success bericht met volgende stappen"""
    print()
    print("━" * 60)
    print(f"✅ Workspace '{workspace_name}' succesvol aangemaakt!")
    print("━" * 60)
    print()
    print(f"📁 Locatie: {workspace_path}")
    print(f"🔧 Agents: moeder, rolbeschrijver")
    print(f"📄 Beleid: governance/beleid.md")
    print()
    print("Volgende stappen:")
    print(f"1. cd {workspace_path}")
    print("2. Controleer en pas governance/beleid.md aan indien nodig")
    print("3. Start met: @github /moeder Richt workspace in")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Initialiseer een nieuwe document-repository workspace",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Voorbeelden:
  python scripts/init-workspace.py --name "kerstmenu" --description "Kerstmenu planning"
  python scripts/init-workspace.py --name "api-docs" --context "temp/api-context.md"
  python scripts/init-workspace.py --name "project-x" --description "..." --parent "../workspaces"
        """
    )
    
    parser.add_argument("--name", required=True, 
                       help="Workspace naam (lowercase, hyphens)")
    parser.add_argument("--description", 
                       help="Korte omschrijving van workspace doel")
    parser.add_argument("--context", 
                       help="Pad naar context.md bestand (voor beleid generatie)")
    parser.add_argument("--parent", default=".", 
                       help="Parent directory voor workspace (default: huidige dir)")
    
    args = parser.parse_args()
    
    # Validatie
    valid, error_msg = validate_name(args.name)
    if not valid:
        print_error(f"Ongeldige workspace naam: {error_msg}")
        return 1
    
    # Genesis root vinden
    genesis_root = get_genesis_root()
    if not (genesis_root / "governance/gedragscode.md").exists():
        print_error("Genesis root niet gevonden. Run dit script vanuit Genesis repository.")
        return 1
    
    # Parent directory
    parent_dir = Path(args.parent).resolve()
    if not parent_dir.exists():
        print_error(f"Parent directory bestaat niet: {parent_dir}")
        return 1
    
    # Check of workspace al bestaat
    if workspace_exists(args.name, parent_dir):
        print_error(f"Workspace '{args.name}' bestaat al in {parent_dir}")
        return 1
    
    # Description
    description = args.description or f"Document repository workspace: {args.name}"
    
    # Context laden (optioneel)
    context_content = None
    if args.context:
        context_path = genesis_root / args.context
        if not context_path.exists():
            print_warning(f"Context bestand niet gevonden: {args.context}")
        else:
            context_content = context_path.read_text(encoding="utf-8")
    
    # Start initialisatie
    workspace_path = parent_dir / args.name
    print_header(f"Workspace Initialisatie: {args.name}")
    
    # 1. Folders aanmaken
    create_folders(workspace_path)
    print_step("Folderstructuur aangemaakt")
    
    # 2. Governance documenten kopiëren
    copy_governance_documents(genesis_root, workspace_path)
    print_step("Governance documenten gekopieerd")
    
    # 3. Beleid genereren
    if context_content:
        beleid_content = generate_beleid(args.name, description, context_content)
    else:
        # Basis beleid zonder context
        beleid_content = generate_beleid(args.name, description, "")
    
    beleid_path = workspace_path / "governance/beleid.md"
    beleid_path.write_text(beleid_content, encoding="utf-8")
    print_step("Beleid.md gegenereerd")
    
    # 4. Agent moeder installeren
    copy_agent("moeder", genesis_root, workspace_path, args.name)
    print_step("Agent moeder geïnstalleerd")
    
    # 5. Agent rolbeschrijver installeren
    copy_agent("rolbeschrijver", genesis_root, workspace_path, args.name)
    print_step("Agent rolbeschrijver geïnstalleerd")
    
    # 6. Create-agent script kopiëren
    if copy_create_agent_script(genesis_root, workspace_path):
        print_step("Create-agent script gekopieerd")
    
    # 7. README genereren
    generate_readme(args.name, description, workspace_path)
    print_step("README.md gegenereerd")
    
    # 8. .gitignore genereren
    generate_gitignore(workspace_path)
    print_step(".gitignore aangemaakt")
    
    # 9. Git initialiseren
    if git_init(workspace_path, args.name):
        print_step("Git repository geïnitialiseerd")
    
    # Success!
    print_success_message(args.name, workspace_path)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
