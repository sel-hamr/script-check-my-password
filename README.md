# Password Leak Checker

## Description

This script checks if a password has been leaked using the "Have I Been Pwned" API. It hashes the password using SHA-1 and checks the first 5 characters of the hash against the API to see if the password has been compromised.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/yourrepository.git
   ```
2. Navigate to the project directory:
   ```sh
   cd yourrepository
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Arguments

You can provide one or more passwords as command-line arguments:

```sh
python checkmypass.py <password1> <password2> ...

# Example

python checkmypass.py password123 qwerty
```

This will check if the passwords `password123` and `qwerty` have been leaked.

## Error Handling

If an error occurs during the API request, the script will raise a `RuntimeError` with the status code of the response.
