# Claude Code Instructions for nbdev Projects

## Project Overview
This project uses **nbdev** - a literate programming system that creates Python packages directly from Jupyter notebooks. All development should follow nbdev conventions to maintain consistency between code, documentation, and tests.

## Core nbdev Principles
- **Literate Programming**: Code, documentation, examples, and tests live together in notebooks
- **Single Source of Truth**: Notebooks are the primary source - Python modules are generated from them
- **Interactive Development**: Use live preview and notebook execution for immediate feedback
- **Professional Output**: Automatically generate PyPI packages, conda packages, and documentation websites

## Required nbdev Directives

### Essential Cell Directives
Always include these special comments at the top of code cells:

- `#| default_exp module_name` - **First cell of each notebook** - specifies which Python module this notebook exports to
- `#| export` - Mark cells to include in the exported Python module and documentation
- `#| hide` - Exclude cells from both exported module and documentation (for setup/utilities)
- `#| eval: false` - Include code in docs but don't execute it
- `#| echo: false` - Execute code but don't show it in docs

### Frontmatter Structure
Every notebook should start with markdown frontmatter:
```markdown
# Module Name
> Brief description of what this module does

Some detailed explanation of the module's purpose and how it fits into the larger project.
```

## Code Development Standards

### Function/Class Documentation
Every exported function and class must include:
1. **Descriptive docstring** explaining purpose, parameters, and return values
2. **Type hints** where appropriate
3. **At least 2-3 usage examples** showing typical and edge cases
4. **Tests** using assert statements or fastcore.test functions

Example format:
```python
#| export
def process_data(data: list, threshold: float = 0.5) -> dict:
    """Process input data and return filtered results.
    
    Args:
        data: List of values to process
        threshold: Minimum value to include (default: 0.5)
    
    Returns:
        Dictionary with processed results
    """
    # Implementation here
    return result

# Examples and tests immediately follow
sample_data = [0.1, 0.6, 0.8, 0.3]
result = process_data(sample_data, 0.4)
assert len(result) > 0
assert all(v >= 0.4 for v in result['values'])
```

### Notebook Organization
1. **Start with overview** - Explain what the notebook accomplishes
2. **Import dependencies** - Keep imports at the top, mark with `#| hide` if setup-only
3. **Build complexity gradually** - Start with simple functions, build to complex ones
4. **Include comprehensive examples** - Show real-world usage scenarios
5. **End with export cell** - Include `#| hide` cell with `from nbdev import nbdev_export; nbdev_export()`

### Linking and References
- Use backticks around function/class names for automatic hyperlinking: `process_data`
- Reference other notebooks and functions liberally
- Use `show_doc()` for detailed method documentation when needed

## Development Workflow Commands

### Essential Commands to Remember
- `nbdev_preview` - Start live documentation preview (run this first)
- `nbdev_prepare` - **Run before every commit** (exports, tests, cleans, updates README)
- `nbdev_export` - Export notebooks to Python modules
- `nbdev_test` - Run all notebook tests
- `nbdev_clean` - Remove notebook metadata for git-friendly commits

### Setup Commands (for new environments)
- `nbdev_install_hooks` - Install git hooks for automatic notebook cleaning
- `pip install -e '.[dev]'` - Install package in development mode

## File Structure and Naming
- All notebooks go in `nbs/` directory
- Use descriptive names: `00_core.ipynb`, `01_data_processing.ipynb`, `02_visualization.ipynb`
- Number prefixes help show reading order (but creation order can differ)
- `index.ipynb` becomes the main documentation page and README

## Testing Philosophy
- **Every example is a test** - All code cells with output serve as tests
- **Use explicit assertions** - Include `assert` statements for critical behavior
- **Test edge cases** - Include examples that might break
- **Use fastcore.test** for better error messages: `from fastcore.test import test_eq`

## Dependencies and Configuration
- Add requirements to `settings.ini` in the `requirements` section
- Use space-separated format: `requirements = pandas numpy>=1.20 matplotlib`
- For development-only deps: `dev_requirements = pytest black`

## Common Patterns

### Autoreload Setup (for development notebooks)
```python
#| hide
%load_ext autoreload
%autoreload 2
```

### Class Documentation
```python
#| export
class DataProcessor:
    "Process and analyze data with configurable parameters"
    
    def __init__(self, config: dict):
        "Initialize processor with configuration"
        self.config = config
    
    def process(self, data):
        "Main processing method"
        # Implementation
```

### Error Handling Examples
Always include examples of both success and failure cases:
```python
# Success case
result = process_data([1, 2, 3])
assert result is not None

# Edge case
empty_result = process_data([])
assert empty_result == {}

# Error case (if applicable)
try:
    invalid_result = process_data("not a list")
    assert False, "Should have raised TypeError"
except TypeError:
    pass  # Expected behavior
```

## Documentation Quality
- **Write for your future self** - Assume you'll forget the implementation details
- **Explain the "why" not just the "what"** - Include rationale for design decisions
- **Use rich output** - Include plots, tables, and visual examples when helpful
- **Cross-reference liberally** - Link related functions and concepts

## Git Workflow
1. Always run `nbdev_prepare` before committing
2. Check `git status` to see what files were generated/modified
3. Commit with descriptive messages that mention both features and notebooks changed
4. Let GitHub Actions handle testing and documentation deployment

## Troubleshooting
- If exports seem wrong, check `#| default_exp` directive
- If tests fail, run individual notebook cells to isolate issues
- If docs look wrong, check frontmatter and directive placement
- Use `nbdev_preview` to see documentation changes immediately

## Reference Links
- [nbdev Documentation](https://nbdev.fast.ai/)
- [nbdev Tutorial](https://nbdev.fast.ai/tutorials/tutorial.html)
- [Quarto Documentation](https://quarto.org/) (for advanced formatting)
- [fastcore.test](https://fastcore.fast.ai/test.html) (for testing utilities)

Remember: The goal is to create code that is not just functional, but also thoroughly documented, tested, and understandable. Every notebook should tell a story about what it does and why it matters to the larger project.