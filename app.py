import os

def main():
    print("Running app.py from Jenkins")

    workspace = os.getcwd()
    print(f"Jenkins workspace: {workspace}")

    # Example: list files pulled from GitHub
    files = os.listdir(workspace)
    print("Files in repo:")
    for f in files:
        print(f"- {f}")

if __name__ == "__main__":
    main()
