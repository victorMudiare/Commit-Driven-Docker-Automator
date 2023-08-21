import json
import subprocess

def get_latest_commit_hash():
    try:
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def build_docker_image(commit_hash):
    try:
        subprocess.run(['docker', 'build', '-t', f'your-image-name:{commit_hash}', '.'], check=True)
        print("Docker image built successfully.")
    except subprocess.CalledProcessError:
        print("Error building Docker image.")

def load_last_commit_from_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get('last_commit_hash')
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_last_commit_to_json(filename, commit_hash):
    data = {'last_commit_hash': commit_hash}
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
    except IOError:
        print("Error saving commit hash to JSON.")

def main():
    commit_data_file = 'last_commit.json'
    
    previous_commit_hash = load_last_commit_from_json(commit_data_file)
    latest_commit_hash = get_latest_commit_hash()
    
    if latest_commit_hash:
        if latest_commit_hash != previous_commit_hash:
            print("New commit detected. Building Docker image...")
            build_docker_image(latest_commit_hash)
            save_last_commit_to_json(commit_data_file, latest_commit_hash)
        else:
            print("No new commits since the last build.")
    else:
        print("Error getting latest commit hash.")

if _name_ == "_main_":
    main()