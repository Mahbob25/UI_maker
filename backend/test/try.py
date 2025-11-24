import shutil
def copy_base_template(destination: str):
    shutil.copytree("backend\\workflow\\angular_base_template", destination, dirs_exist_ok=True)

copy_base_template("generated_output")