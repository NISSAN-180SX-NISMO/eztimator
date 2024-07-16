import os

# List of target paths to add to PYTHONPATH
target_paths = [
    # 'C:/Users/user/__handlers__/pract/modules/implementations/cpp_bytes_parser_adapter/zparser_lib_cpp/zparser.cp310-win_amd64.pyd',
    # 'C:/Users/user/__handlers__/pract/modules/implementations/cpp_bytes_parser_adapter/zparser_lib_cpp/',  # work
    'C:/Users/User/Desktop/python/zoyda/modules/implementations/cpp_bytes_parser_adapter/zparser_lib_cpp/'  # home
]

# Construct the Python path including all project paths
python_paths = [os.path.abspath(path) for path in target_paths]

# Join all paths with os.pathsep to form the final PYTHONPATH
new_python_path = os.pathsep.join(python_paths)

# Check if PYTHONPATH is already set
if 'PYTHONPATH' in os.environ:
    # Append the new paths to the existing PYTHONPATH
    os.environ['PYTHONPATH'] = new_python_path + os.pathsep + os.environ['PYTHONPATH']
else:
    # Set PYTHONPATH to the new paths
    os.environ['PYTHONPATH'] = new_python_path

# Optionally print the updated PYTHONPATH
print(f"PYTHONPATH set to: {os.environ['PYTHONPATH']}")
