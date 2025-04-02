from src.integrator import LegacySystemIntegrator
from src.ai_processor import AIProcessor
from src.workflow_manager import WorkflowManager

def main():
    config = {
        'legacy_system_url': 'http://sistema-legado.com',
        'db': {
            'host': 'localhost',
            'database': 'automation_db',
            'user': 'admin',
            'password': 'securepassword'
        }
    }
    
    print("Sistema de automação inicializado!")
    
if __name__ == "__main__":
    main()