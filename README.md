# genpark-lsm-tree-sstable-compaction-skill

> Log-Structured Merge-tree (LSM Tree) storage engine with in-memory MemTable, SSTables, and compaction.

Part of the **GenPark AI Agent Skills Matrix**. Production-ready, zero external dependencies, native Python 3.9+ standard library.

## Architecture

```mermaid
flowchart TD
    A[Database Transaction / Query] --> B[Storage Engine / B+ Tree / LSM]
    B --> C[WAL Logging & MVCC Isolation]
    C --> D[Cost-Optimized Plan / Execution]
    D --> E[MCP Protocol Endpoint]
```

## Features
- **Zero Third-Party Dependencies**: Pure Python standard library (`bisect`, `collections`).
- **Database Engine Internals**: B+ Tree indexing, ARIES WAL recovery, LSM tree compaction, and MVCC snapshot isolation.
- **Native MCP Protocol Support**: Integrated JSON-RPC 2.0 stdio server ready for Claude Desktop, Cursor, and Windsurf.

## Installation

```bash
pip install genpark-lsm-tree-sstable-compaction-skill
```

Or clone directly:

```bash
git clone https://github.com/alphaparkinc/genpark-lsm-tree-sstable-compaction-skill.git
cd genpark-lsm-tree-sstable-compaction-skill
python example_usage.py
```

## Quick Start

```python
from client import *
# Refer to example_usage.py for end-to-end execution
```

## Model Context Protocol (MCP) Setup

Add to your `claude_desktop_config.json` or `cursor.json`:

```json
{
  "mcpServers": {
    "genpark-lsm-tree-sstable-compaction-skill": {
      "command": "python",
      "args": ["-m", "genpark-lsm-tree-sstable-compaction-skill.mcp_server"]
    }
  }
}
```

## License
MIT License. Copyright (c) 2026 AlphaPark Inc. & Alpha-Park.
