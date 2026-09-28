from client import LSMTreeEngine

def main():
    lsm = LSMTreeEngine(memtable_threshold=3)
    lsm.put("user_1", "Alice")
    lsm.put("user_2", "Bob")
    lsm.put("user_3", "Charlie")
    lsm.put("user_1", "Alice_Updated")
    print("LSM Tree & SSTable Verification:")
    print(f"Get user_1: {lsm.get('user_1')}")
    print(f"Active SSTables Count before compaction: {len(lsm.sstables)}")
    lsm.compact()
    print(f"Active SSTables Count after compaction: {len(lsm.sstables)}")

if __name__ == "__main__":
    main()
