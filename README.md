# ODpyClassGen
Gerenate Python classes from OData metadata. Besides standard get, patch, delete, put, it also has support for search

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
   git clone https://github.com/yourusername/oclassgenerator.git
   cd oclassgenerator
