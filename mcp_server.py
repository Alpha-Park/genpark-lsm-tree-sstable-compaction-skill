import sys
import json
from client import LSMTreeEngine

lsm = LSMTreeEngine(memtable_threshold=3)

def handle_rpc(line):
    global lsm
    try:
        req = json.loads(line)
    except Exception:
        return
    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        res = {
            "protocolVersion": "2024-11-05",
            "serverInfo": {"name": "genpark-lsm-tree-sstable-compaction-skill", "version": "1.0.0"},
            "capabilities": {"tools": {}}
        }
    elif method == "tools/list":
        res = {
            "tools": [
                {
                    "name": "put_key",
                    "description": "Write key-value to LSM Tree MemTable, triggering SSTable flush when threshold reached",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "key": {"type": "string"},
                            "value": {"type": "string"}
                        },
                        "required": ["key", "value"]
                    }
                },
                {
                    "name": "get_key",
                    "description": "Read key value from MemTable or SSTable hierarchy",
                    "inputSchema": {
                        "type": "object",
                        "properties": {"key": {"type": "string"}},
                        "required": ["key"]
                    }
                },
                {
                    "name": "run_compaction",
                    "description": "Merge and compact all flushed SSTables into a single sorted level",
                    "inputSchema": {"type": "object", "properties": {}}
                }
            ]
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "put_key":
            lsm.put(args.get("key"), args.get("value"))
            res = {"content": [{"type": "text", "text": json.dumps({"status": "written", "memtable_size": len(lsm.memtable), "sstables_count": len(lsm.sstables)})}]}
        elif tool_name == "get_key":
            val = lsm.get(args.get("key"))
            res = {"content": [{"type": "text", "text": json.dumps({"key": args.get("key"), "value": val})}]}
        elif tool_name == "run_compaction":
            num_keys = lsm.compact()
            res = {"content": [{"type": "text", "text": json.dumps({"compacted_keys": num_keys, "sstables_count": len(lsm.sstables)})}]}
        else:
            res = {"isError": True, "content": [{"type": "text", "text": f"Unknown tool {tool_name}"}]}
    else:
        res = {"error": {"code": -32601, "message": "Method not found"}}

    resp = {"jsonrpc": "2.0", "id": req_id, "result": res.get("result", res)}
    sys.stdout.write(json.dumps(resp) + "\n")
    sys.stdout.flush()

def main():
    for line in sys.stdin:
        if line.strip():
            handle_rpc(line.strip())

if __name__ == "__main__":
    main()
