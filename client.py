"""Log-Structured Merge-Tree (LSM Tree) & SSTable Compaction Engine
100% Python Standard Library.
"""

class LSMTreeEngine:
    """In-memory MemTable with immutable SSTable flush and compaction."""
    def __init__(self, memtable_threshold=3):
        self.memtable_threshold = memtable_threshold
        self.memtable = {}
        self.sstables = []

    def put(self, key, value):
        self.memtable[key] = value
        if len(self.memtable) >= self.memtable_threshold:
            sorted_sstable = dict(sorted(self.memtable.items()))
            self.sstables.append(sorted_sstable)
            self.memtable = {}

    def get(self, key):
        if key in self.memtable:
            return self.memtable[key]
        for sst in reversed(self.sstables):
            if key in sst:
                return sst[key]
        return None

    def compact(self):
        merged = {}
        for sst in self.sstables:
            merged.update(sst)
        self.sstables = [dict(sorted(merged.items()))]
        return len(self.sstables[0])
