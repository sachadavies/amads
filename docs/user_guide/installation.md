# Installation

## Prerequisites

- Python 3.8 or higher
- Git
- Access to the private repository:
  - The repository is hosted at https://github.com/music-computing/toolkit
  - You will need to request access from the repository administrators
  - For secure authentication, we recommend using SSH keys:
    1. Generate an SSH key pair if you don't have one already - see [GitHub's guide on generating SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
    2. Add your public key to your GitHub account - follow [GitHub's instructions for adding SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
    3. Once set up, clone using the SSH URL: `git clone git@github.com:music-computing/toolkit.git`

## Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/music-computing/toolkit.git
   cd toolkit
   ```

2. Create and activate a virtual environment:

   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the package in editable mode:

   ```bash
   pip install -e .
   ```

Your installation is now complete! The package is installed in editable mode, which means any changes you make to the source code will be reflected immediately without needing to reinstall.
