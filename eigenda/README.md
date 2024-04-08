# EigenDA

This project reflects all the operations an AVS Operator should do according to the [Eigenlayer Operator Guide](https://docs.eigenlayer.xyz/eigenlayer/operator-guides/operator-installation) except keys management.

## Supported operations (playbooks)

- Install Golang (to build the Eigenlayer CLI from source).
- Install Eigenlayer CLI.
- Register an Operator according to `group_vars`.
- Check an Operator's registration status.

## Requirements

To use this project, you need first to provide the AVS nodes. Once you have the nodes ready and the proper SSH keys installed, you can use this project to execute the playbooks.

To start, you can run the `Install Eigenlayer CLI` playbook to install the Eigenlayer CLI on your local machine. Then, you can create the Operator keys, which we recommend doing manually, and stick to the Key Management guidelines in the Eigenlayer documentation. Once you make the keys and get the Operator address, you can update the `group_vars` files with the Operator's information.
