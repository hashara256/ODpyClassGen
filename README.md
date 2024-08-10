# ODpyClassGen

Generate Python classes from OData metadata with **ODpyClassGen**, a tool designed for seamless interaction with OData-compliant services, particularly within the Microsoft ecosystem. This Python tool enables easy creation, reading, updating, deleting, and searching of data entities, leveraging user-based authentication via MSAL. Ideal for developers, **ODpyClassGen** automates the process of working with OData APIs by generating Pythonic, ready-to-use classes.

## Features

- **Dynamic Class Generation**: Automatically generates Python classes for each OData entity based on your service's OData metadata.
- **CRUD Operations**: Provides methods to create, update, delete, and retrieve records from your service instance.
- **Search Functionality**: Allows for flexible querying of entities using multiple property values.

## Prerequisites

- **Python 3.6+**: Make sure you have Python installed.
- **Microsoft Azure AD Application**: You need to register an application in Azure AD to obtain the `client_id` and `tenant_id`.
- **OData-Compliant Service**: A valid service URL that exposes an OData API (e.g., Dynamics 365 Finance & Operations, Dynamics 365 Sales, etc.).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ODpyClassGen.git
   cd ODpyClassGen
   ```

2. **Install Required Python Packages**:
   ```bash
   pip install msal requests
   ```

3. **Set Up Your Environment**:
   - Replace placeholders in the script (`client_id`, `tenant_id`, and `service_instance`) with your actual Azure AD and service instance details.

## Usage

1. **Configure the Script**:
   - Update the configuration variables at the top of the script:
     ```python
     client_id = 'your-client-id'  # Replace with your Azure AD Application (client) ID
     tenant_id = 'your-tenant-id'  # Replace with your Azure AD Tenant ID
     service_instance = 'https://your-service-instance-url'  # Replace with your OData service URL
     ```

2. **Run the Script**:
   - Execute the script to authenticate, retrieve metadata, and generate classes:
     ```bash
     python ODpyClassGen.py
     ```

3. **Example Usage**:
   - After running the script, you can use the generated classes for CRUD operations and searches:
     ```python
     # Assuming a Customer class was generated
     customer = Customer()
     customer.CustomerID = 'CUST001'
     customer.CustomerName = 'Example Customer'
     
     # Create a new customer
     status_code, response = customer.create(access_token)
     print(status_code, response)
     
     # Search for customers
     status_code, data = Customer.search(access_token, CustomerID='CUST001')
     print(status_code, data)
     ```

## Supported Services

This script is designed to work with any OData-compliant service, particularly those using Azure AD for authentication. While originally developed with Dynamics 365 Finance & Operations in mind, it can be adapted for use with other Microsoft services such as:

- **Dynamics 365 Finance & Operations**
- **Dynamics 365 Sales**
- **Dynamics 365 Customer Service**
- **Other OData-Compliant Services**: Any service that exposes an OData API and uses Azure AD for authentication.

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**. You are free to use, modify, and distribute this software under the terms of the GPL-3.0 license. However, any derivative works must also be distributed under the same license, ensuring that the source code remains open and available to the community. For more details, see the [LICENSE](LICENSE) file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Acknowledgements

- **Microsoft Authentication Library (MSAL)**: For managing authentication flows.
- **Microsoft Dynamics 365**: For providing the OData services.

## Troubleshooting

- **Authentication Issues**: Ensure that your Azure AD application has the correct permissions and that you have provided the correct `client_id`, `tenant_id`, and `redirect_uri`.
- **OData Errors**: Check that your service instance is accessible and that the OData service is enabled.

## Contact

For questions or support, please open an issue on the GitHub repository or contact the project maintainer at your-email@example.com.
