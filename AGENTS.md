# Iron Age Project

This is a markdown-based knowledge management system that integrates Obsidian for documentation and knowledge organization with OpenCode for development tasks.

## Project Overview

- **Type**: Knowledge management system
- **Primary Tools**: Obsidian, OpenCode, Git
- **Structure**: Markdown files in organized folder hierarchy
- **Goal**: Seamless integration between documentation and development

## Directory Structure

```
iron-age/
├── docs/                   # Obsidian vault (main documentation)
│   ├── .obsidian/         # Obsidian configuration
│   ├── 00 - Inbox/        # Quick capture and ideas
│   ├── 01 - Projects/     # Active project documentation
│   ├── 02 - Areas/        # Ongoing responsibilities
│   ├── 03 - Resources/    # Reference materials
│   ├── 04 - Archive/      # Completed projects
│   └── 99 - Attachments/  # Media and files
├── src/                   # Source code (if needed)
├── scripts/               # Automation scripts
├── tests/                 # Test files
├── config/                # Configuration files
└── AGENTS.md              # This file - OpenCode configuration
```

## Key Features

### Obsidian Integration
- Wiki links between notes: `[[Note Name]]`
- File linking to code: `[[src/filename.js]]`
- Graph view for visualizing connections
- Daily notes and templates
- Tags and metadata for organization

### OpenCode Integration
- Can read and write markdown files in the vault
- Generate documentation directly into appropriate folders
- Cross-reference between code and documentation
- Automate repetitive documentation tasks

### Development Workflow
1. **Planning**: Use Obsidian for project planning and architecture
2. **Implementation**: Use OpenCode for coding and file management
3. **Documentation**: Generate and update docs in Obsidian
4. **Version Control**: Git tracks both code and documentation changes

## Conventions

### File Naming
- Use descriptive names with spaces
- Capitalize important words
- Include dates for time-sensitive content

### Linking
- Use `[[Wiki Link]]` for internal notes
- Use `[[path/to/file.js]]` for code references
- Add context to links: `[[Note Name|Description]]`

### Documentation Structure
- Start with overview/purpose
- Include usage examples
- Link to related resources
- Keep documentation up-to-date with code

## Common Commands

### OpenCode Tasks
```bash
# Generate documentation
"Create API documentation in docs/01 - Projects/API Reference.md"

# Update project structure
"Update the README.md to reflect the new folder structure"

# Cross-reference documentation
"Add links to [[Authentication Flow]] in the login component docs"
```

### Git Workflow
```bash
# Add all changes
git add .

# Commit with descriptive message
git commit -m "Add user authentication documentation"

# Push changes
git push origin main
```

## Tools and Scripts

### OpenCode Configuration
- This file serves as the primary configuration
- OpenCode will understand the project structure from this documentation
- Can be updated to reflect new patterns or conventions

### Obsidian Settings
- Vault located in `docs/` folder
- Minimal theme for clean interface
- Core plugins enabled for productivity
- Custom workspace for development workflow

## Best Practices

1. **Keep documentation current**: Update docs when code changes
2. **Use descriptive links**: Make links self-explanatory
3. **Organize by context**: Place docs in appropriate folders
4. **Cross-reference everything**: Link related concepts
5. **Commit regularly**: Track both code and documentation changes

## Getting Started

1. Open `docs/` folder in Obsidian
2. Run `opencode` and use `/init` to initialize
3. Start creating notes and documentation
4. Use OpenCode for any development tasks
5. Commit changes regularly

## Related Resources

- [[Project Setup]] - Initial setup instructions
- [[OpenCode Integration]] - OpenCode-specific workflows
- [[Documentation Standards]] - Formatting and organization guidelines