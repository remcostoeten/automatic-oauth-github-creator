import os
import json
import logging
from datetime import datetime
from pathlib import Path
from cryptography.fernet import Fernet
from typing import List, Dict, Optional

logger = logging.getLogger("AuditLogger")

class AuditLogger:
    """
    Handles secure, encrypted logging of generated OAuth credentials.
    Uses Fernet (symmetric encryption) with a locally stored key.
    """
    
    def __init__(self, base_dir: Path = None):
        if base_dir is None:
            # Default to ~/.oauth-automator
            self.base_dir = Path.home() / ".oauth-automator"
        else:
            self.base_dir = base_dir
            
        self.key_file = self.base_dir / ".key"
        self.github_dir = self.base_dir / "github"
        self.log_file = self.github_dir / "history.enc"
        
        self.key = None
        self.fernet = None
        
        self._initialize_storage()
        
    def _initialize_storage(self):
        """Ensure directories and keys exist."""
        try:
            # Create directories with restricted permissions
            if not self.base_dir.exists():
                self.base_dir.mkdir(parents=True, mode=0o700)
            if not self.github_dir.exists():
                self.github_dir.mkdir(parents=True, mode=0o700)
                
            # Load or generate key
            if self.key_file.exists():
                self.key = self.key_file.read_bytes()
            else:
                self.key = Fernet.generate_key()
                # Write key with 600 permissions
                self.key_file.write_bytes(self.key)
                self.key_file.chmod(0o600)
                
            self.fernet = Fernet(self.key)
            
        except Exception as e:
            logger.error(f"Failed to initialize secure logging storage: {e}")
            raise

    def log_credential(self, app_name: str, client_id: str, client_secret: str, 
                      homepage: str, env_type: str = "PROD"):
        """
        Encrypt and append a credential entry to the log.
        """
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "app_name": app_name,
            "client_id": client_id,
            "client_secret": client_secret,
            "homepage": homepage,
            "env_type": env_type
        }
        
        try:
            # Read existing entries
            history = self.read_log()
            history.append(entry)
            
            # Encrypt entire blob
            json_blob = json.dumps({"entries": history}, indent=2).encode()
            encrypted_blob = self.fernet.encrypt(json_blob)
            
            # Write back
            self.log_file.write_bytes(encrypted_blob)
            logger.info(f"🔒 App logged to secure history: {app_name}")
            
        except Exception as e:
            logger.error(f"Failed to write to secure log: {e}")

    def read_log(self) -> List[Dict]:
        """
        Decrypt and return the list of logged credentials.
        """
        if not self.log_file.exists():
            return []
            
        try:
            encrypted_data = self.log_file.read_bytes()
            if not encrypted_data:
                return []
                
            decrypted_data = self.fernet.decrypt(encrypted_data)
            data = json.loads(decrypted_data)
            return data.get("entries", [])
            
        except Exception as e:
            logger.error(f"Failed to read secure log: {e}")
            return []
