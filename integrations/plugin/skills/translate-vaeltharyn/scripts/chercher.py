from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from vaeltharyn.search import main
if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
if __name__=='__main__':main()
