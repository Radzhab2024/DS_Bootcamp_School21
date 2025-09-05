import os
import subprocess
import sys


#проверка наличия окружения
def in_virtenv(expected_env):
    env_name = os.environ.get('VIRTUAL_ENV')
    if not env_name or expected_env not in env_name:
        raise EnvironmentError("This script must be run in the correct virtual environment!")


#установка библиотек
def install_requirements(req_file):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', req_file])


#получение списка устновленных библиотек
def installed_packages_list():
    result_list = subprocess.run(
        [sys.executable, '-m', 'pip', 'freeze'], capture_output=True, text=True
    )
    return result_list.stdout


#сохранение списка библиотек
def packages_list_save(output_file, packages_list):
    with open(output_file, 'w') as file:
        file.write(packages_list)


#архивация окружения
def archive_of_env(path_to_env, archive_name):
    import shutil
    shutil.make_archive(archive_name, 'zip', path_to_env)


if __name__ == '__main__':
    try:
        expected_env_name = 'morfinwi'
        in_virtenv(expected_env_name)

        requirements_file = 'requirements.txt'
        install_requirements(requirements_file)

        installed_packages = installed_packages_list()
        packages_list_save("requirements.txt", installed_packages)

        env_path = os.environ["VIRTUAL_ENV"]
        archive_of_env(env_path, "morfinwi_env")

        print("Libraries installed and environment archived successfully.")

    except EnvironmentError as e:
        print(f"Error: {e}")
