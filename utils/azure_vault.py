from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

class AzureKeyVaultClient:
    """
    Handles fetching secrets securely from Azure Key Vault.
    """

    def __init__(self):
        """
        Initializes the connection to Azure Key Vault.
        Requires the AZURE_KEY_VAULT_URL environment variable to be set.
        """
        self.vault_url = os.getenv("AZURE_KEY_VAULT_URL")
        if not self.vault_url:
            raise ValueError("AZURE_KEY_VAULT_URL environment variable is not set.")
        
        self.credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=self.vault_url, credential=self.credential)

    def get_secret(self, secret_name: str) -> str:
        """
        Retrieves a secret value from Azure Key Vault.
        """
        retrieved_secret = self.client.get_secret(secret_name)
        return retrieved_secret.value
