# OpenCode Integration

How to use OpenCode with this project and Obsidian vault.

## Configuration

OpenCode is configured via `AGENTS.md` in the project root.

## Usage Patterns

### 1. Documentation Generation
Ask OpenCode to create documentation directly in the vault:

```
Create API documentation for the user service in docs/01 - Projects/User API.md
```

### 2. Code Documentation
Generate code documentation that links to Obsidian:

```javascript
/**
 * User authentication service
 * See [[Authentication Flow]] for implementation details
 */
```

### 3. Cross-referencing
Link between code and documentation:

- In code: `// See [[Error Handling]] for details`
- In Obsidian: `[[src/services/auth.js]]`

## Workflows

### Development Workflow
1. Plan in Obsidian
2. Implement with OpenCode
3. Document results back to Obsidian

### Documentation Workflow
1. Use OpenCode to generate initial docs
2. Edit and enhance in Obsidian
3. Link related concepts with wiki links

## Tips

- Use `@` in OpenCode to reference files
- Keep documentation in sync with code changes
- Use Obsidian's graph view to see connections
- Commit both code and docs together