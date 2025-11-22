import os
import subprocess
import click
working_dir = os.getcwd()

def execute_chatter_box():

    click.secho("Initializing Chatterbox Extended!", fg="green", bold=True)
    bat_path = os.path.join(working_dir, "bat", "install_chatterbox.bat")
    # install all required dependencies
    subprocess.call([bat_path])
    # chatterboxVenv should exist now.
    # run its specific venv that has all the required packages
    venv = os.path.join(working_dir, "chatterboxVenv", "Scripts", "python.exe")
    subprocess.run([venv, "Chatter.py"], cwd="Chatterbox-TTS-Extended")


def init_maya():
    text = get_command_input("Enter text you want to generate:", str)
    prompt = get_command_input("Enter prompt of what the person should sound like", str)
    click.secho("Initializing FastMaya!", fg="green", bold=True)
    bat_path = os.path.join(working_dir, "bat", "install_fastmaya.bat")
    # install all required dependencies
    subprocess.call([bat_path])
    venv = os.path.join(working_dir, "fastmayaVenv", "Scripts", "python.exe")
    subprocess.call([venv, "fast_maya.py", text, prompt])


def get_command_input(text, required_type=str):
    click.secho(text, fg="green", bold=True)
    return click.prompt("Input", type=required_type)

def init_neutts():
    text = get_command_input("Enter text you want to generate:", str)
    path = get_command_input("Enter path of reference audio", str)

    click.secho("Initializing NeuTTS!", fg="green", bold=True)
    bat_path = os.path.join(working_dir, "bat", "install_fastneutts.bat")
    # install all required dependencies
    subprocess.call([bat_path])
    venv = os.path.join(working_dir, "fastneuttsVenv", "Scripts", "python.exe")
    subprocess.call([
        venv, "-m", "pip", "install",
        "torch==2.8.0+cu129",
        "torchvision==0.23.0+cu129",
        "torchaudio==2.8.0",
        "--index-url", "https://download.pytorch.org/whl/cu129"
    ])
    subprocess.call([venv, "fast_neutts.py", text, path])

@click.command()
def menu():
    click.secho("TTSHub", fg="green", bold=True)
    click.secho("1) Chatterbox Extended", fg="blue")
    click.secho("2) FastMaya")
    click.secho("3) FastNeuTTS")
    click.secho("4) Exit", fg="red")
    choice = click.prompt("Enter your choice", type = int)
    if choice == 1:
        execute_chatter_box()
    elif choice == 2:
        init_maya()
    elif choice == 3:
        init_neutts()
    elif choice == 4:
        return







if __name__ == "__main__":#
    menu()




