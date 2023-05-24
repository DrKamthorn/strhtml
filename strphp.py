import streamlit as st
import subprocess

# Display Streamlit UI elements
st.title('PHP Integration with Streamlit')

# PHP script execution
php_script = """
<?php
 echo "Kamthorn";
?>
"""

# Execute PHP script using subprocess
result = subprocess.run(['php', '-r', php_script], capture_output=True, text=True)

# Display PHP script output
st.write('PHP Output:')
st.code(result.stdout)