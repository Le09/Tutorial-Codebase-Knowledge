import subprocess

# get folder commit hash
def get_commit_hash(folder_path):
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=folder_path, capture_output=True, text=True)
    return result.stdout.strip()

# get folder upstream url
def get_upstream_url(folder_path):
    result = subprocess.run(['git', 'config', '--get', 'remote.origin.url'], cwd=folder_path, capture_output=True, text=True)
    return result.stdout.strip()

def get_branch_name(folder_path):
    result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], cwd=folder_path, capture_output=True, text=True)
    return result.stdout.strip()

def get_tag_name(folder_path):
    result = subprocess.run(['git', 'describe', '--tags'], cwd=folder_path, capture_output=True, text=True)
    return result.stdout.strip()
