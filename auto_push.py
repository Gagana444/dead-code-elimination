import subprocess
import time
import os

file_path = "test_sample.py"

print("🚀 Auto Push Watcher Started...")

# safer check
if not os.path.exists(file_path):
    print("❌ File not found:", file_path)
    exit()

last_modified = os.path.getmtime(file_path)

while True:
    try:
        current_modified = os.path.getmtime(file_path)

        if current_modified != last_modified:
            print("📦 File changed → Auto pushing to GitHub...")

            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Auto update from analyzer"], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)

            print("✅ Pushed successfully!")

            last_modified = current_modified

    except subprocess.CalledProcessError as e:
        print("❌ Git error:", e)

    except Exception as e:
        print("❌ Error:", e)

    time.sleep(3)