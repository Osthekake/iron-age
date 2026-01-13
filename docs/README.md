# Iron Age Project

A markdown-based knowledge management system using Obsidian and OpenCode integration.

## Project Structure

```
iron-age/
├── docs/                   # Obsidian vault
│   ├── .obsidian/         # Obsidian configuration
│   ├── 00 - Inbox/        # Quick notes and ideas
│   ├── 01 - Projects/     # Project documentation
│   ├── 02 - Areas/        # Areas of responsibility
│   ├── 03 - Resources/    # Reference materials
│   ├── 04 - Archive/      # Completed/archived content
│   └── 99 - Attachments/  # Media and files
├── src/                   # Source code
├── scripts/               # Utility scripts
├── tests/                 # Test files
├── config/                # Configuration files
└── AGENTS.md              # OpenCode configuration
```

## Tools Integration

### Obsidian
- **Vault Location**: `docs/` folder
- **Purpose**: Knowledge management, documentation, planning
- **Key Features**: Wiki links, graph view, daily notes

### OpenCode
- **Purpose**: Code generation, file management, automation
- **Configuration**: See `AGENTS.md`
- **Integration**: Can read/write markdown files in the vault

## Workflow

1. **Planning**: Use Obsidian for project planning and documentation
2. **Development**: Use OpenCode for coding tasks
3. **Documentation**: Generate docs directly into Obsidian vault
4. **Version Control**: Git tracks both code and documentation

## Getting Started

1. Open `docs/` folder in Obsidian
2. Use OpenCode for development tasks
3. Link between code and documentation using wiki links

## Related Notes

- [[Project Setup]] - Detailed setup instructions
- [[OpenCode Integration]] - OpenCode-specific workflows
- [[Documentation Standards]] - How to structure documentation