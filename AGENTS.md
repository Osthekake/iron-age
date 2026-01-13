# Iron Age Project

This is a markdown-based knowledge management system that integrates Obsidian for documentation and knowledge organization with OpenCode for development tasks.

## Project Overview

- **Type**: Knowledge management system
- **Primary Tools**: Obsidian, OpenCode, Git
- **Structure**: Markdown files in organized folder hierarchy
- **Goal**:  Worldbuilding the world of Ferros

## Directory Structure

```
iron-age/
├── docs/                  # Obsidian vault
│   ├── .obsidian/         # Obsidian configuration
│   ├── factions/          # Factions of the world
│   ├── locations/         # Notable locations in the world
├── Theme.md/              # Foundational themes
└── AGENTS.md              # OpenCode configuration
```
## Getting Started

1. Open `docs/` folder in Obsidian
2. Run `opencode` and use `/init` to initialize
3. Start creating notes and documentation
4. Use OpenCode for any development tasks
5. Commit changes regularly

## Theme
Make sure you read the [Theme](docs/Theme.md) document before generating any text.

## Linking Guidelines

### Mandatory Linking Rules
**CRITICAL**: All mentions of locations and cultures must use functional links to ensure proper knowledge connectivity:

- **Location References**: Always use `[Region Name](link)` format for all geographical locations
- **Culture References**: Always use `[Culture Name](link)` format for factions, peoples, and groups
- **Document Cross-References**: Link between related documents using `[Document Name](FILE_NOT_FOUND: Document Name)` format

### Examples
- Correct: "The [Cerwin elves](docs/factions/Cerwin%20elves.md) trade with the [Hiren](docs/factions/Hiren.md) clans in the [Spine Peaks](docs/locations/regions/Spine%20Peaks.md))"
- Incorrect: "The Cerwin elves trade with the Hiren clans in the Spine Peaks"
- Correct: "Travelers pass through the [Whisperwood](docs/locations/regions/Whisperwood.md) forests near the shores of [Mosswater](docs/locations/regions/Mosswater.md)"
- Incorrect: "Travelers pass through the Whisperwood forests near the shores of Mosswater"

### Implementation
- When creating new content, immediately identify and link all location/culture mentions
- When editing existing content, convert plain text mentions to proper links
- Use search functionality to find all instances of unlinked names
- Maintain consistency across all documentation

This ensures the knowledge base remains fully navigable and interconnected.
