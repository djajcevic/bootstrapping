import os
import shutil

def replace_java_packages_with_dirs(root_dir):
    """
    Recursively replace Java package names (e.g., a.b.c) with directory trees (a/b/c).
    Ignore directories starting with a dot (e.g., .git, .idea).
    """
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            # Ignore directories starting with "."
            if dirname.startswith('.'):
                continue

            old_dir = os.path.join(dirpath, dirname)

            # Check if directory name contains dots (Java package format)
            if '.' in dirname:
                # Replace dots with os-specific directory separator
                new_dir = os.path.join(dirpath, dirname.replace('.', os.sep))

                # Ensure the new directory structure exists
                os.makedirs(new_dir, exist_ok=True)

                # Move all contents from the old directory to the new one
                for item in os.listdir(old_dir):
                    old_item_path = os.path.join(old_dir, item)
                    new_item_path = os.path.join(new_dir, item)

                    # Move file or directory to new path
                    shutil.move(old_item_path, new_item_path)

                # Remove the old directory after moving its contents
                os.rmdir(old_dir)


def main():
    # Set the root directory of the generated project
    root_package = os.getcwd()  # This will be the directory where the Cookiecutter project is generated
    replace_java_packages_with_dirs(root_package)

if __name__ == "__main__":
    main()
