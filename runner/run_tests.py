import pytest
import os
from utils.azure_vault import AzureKeyVaultClient

def get_browserstack_credentials():
    """
    Fetches BrowserStack credentials securely from Azure Key Vault.
    """
    vault_client = AzureKeyVaultClient()
    bs_user = vault_client.get_secret("browserstack-username")
    bs_key = vault_client.get_secret("browserstack-access-key")

    if not bs_user or not bs_key:
        raise ValueError("BrowserStack credentials missing in Azure Key Vault!")

    return bs_user, bs_key

def run_pytest():
    """
    Executes pytest tests with BrowserStack integration and generates Allure reports.
    """
    test_dir = os.path.join(os.path.dirname(__file__), "../tests")
    
    # Fetch BrowserStack credentials from Azure Key Vault
    bs_user, bs_key = get_browserstack_credentials()

    # Set environment variables for BrowserStack
    os.environ["BROWSERSTACK_USERNAME"] = bs_user
    os.environ["BROWSERSTACK_ACCESS_KEY"] = bs_key

    # Run pytest with BrowserStack configuration
    pytest.main([
        test_dir,
        "--alluredir=reports/allure-results",
        "--maxfail=3",
        "--reruns", "2",
        "-q",
        "--browserstack"
    ])

if __name__ == "__main__":
    run_pytest()
