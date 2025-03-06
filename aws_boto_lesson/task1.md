# **Setting up Python Virtal Environment and Dependancies**

1. In a Gitbash, Sh, or Bash shell (Unix, Linux or OSX):

   Enable the Python Environment
   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

   To install AWS CLI:
   ```bash
   pip install awscli
   ```

   Then, configure it:
   ```bash
   aws configure
   ```

   You will need to input your **Access Key ID**, **Secret Access Key**, **Default Region Name**, and **Default Output Format**.
   
2. **Example File**: Run the example file.

   Run example file:
   ```bash
   python code/open_web.py
   ```

   Deactivate and delete environment:
   ```bash
   deactivate
   rm -rf venv
   ```
   
   
