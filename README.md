# Community-AVS-Playbooks

- [Community-AVS-Playbooks](#community-avs-playbooks)
  - [Supported AVSs](#supported-avss)
  - [TODO](#todo)
  - [How to handle secrets](#how-to-handle-secrets)
    - [Encrypting a new Ansible file with variables](#encrypting-a-new-ansible-file-with-variables)
    - [Editing an existing Ansible encrypted file](#editing-an-existing-ansible-encrypted-file)
    - [Encrypting Caddy basic auth password](#encrypting-caddy-basic-auth-password)
  - [Suggested variables to encrypt](#suggested-variables-to-encrypt)
    - [Shared variables among all AVSs](#shared-variables-among-all-avss)

Ansible playbooks for Eigenlayer AVSs maintained by Nethermind.

This repo is WIP and will be updated with more playbooks and documentation, especially for more AVSs.

## Supported AVSs

- EigenDA (Holesky and Mainnet)

## TODO

- [ ] [EigenDA] Make caddy reverse proxy optional.
- [ ] Set instructions on inventory management.
- [ ] Add Contribution Guidelines and Code of Conduct.

## How to handle secrets

We use [Ansible Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html) to encrypt sensitive data.

### Encrypting a new Ansible file with variables

To create a new encrypted Ansible vault, use the following command:

```bash
    ansible-vault create secret.yml
```

You will be prompted to enter a password for the vault.

In the editor that opens, add your secret content. For example:

```yaml
api_key: your_api_key_here
```

Save and exit the editor. Your secret.yml file is now encrypted.

### Editing an existing Ansible encrypted file

To edit an existing encrypted Ansible vault, use the following command:

```bash
    ansible-vault edit secret.yml
```

You will be prompted to enter the password for the vault. The file will open in an editor, where you can make your changes. Save and exit the editor to re-encrypt the file.

### Encrypting Caddy basic auth password

Create a password or passphrase first and add it to a file called `caddy_password.txt`. Then run the following command to see the hashed password in the terminal:

```bash
PASSWORD=$(< caddy_password.txt) && docker run --rm caddy caddy hash-password --plaintext "$PASSWORD" 
```

You should use this hash for the `monitoring_encoded_password` variable in the `inventory/group_vars/group/*.yml` file.

## Suggested variables to encrypt

### Shared variables among all AVSs

We strongly recommend you create a new encrypted file for the following variables for the proper inventory group (e.g., `inventory/group_vars/holesky/operator_1/secret.yml`):

```yaml
node_ecdsa_key_password: your_password_here
node_bls_key_password: your_password_here
```

These would be the passwords for the `operator_1` keys.