# main.py
import sys
from network.server import start_server

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <node_id>")
        sys.exit(1)

    node_id = sys.argv[1]
    db_file = f"data_{node_id}.db"
    port = 8000 + int(node_id)  # Optional: vary port per node

    start_server(db_file=db_file, id=node_id, port=port)