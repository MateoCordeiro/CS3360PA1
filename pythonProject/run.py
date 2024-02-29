import subprocess

if __name__ == "__main__":
    # Run the first file
    print("Running the first file:")
    subprocess.run(["python", "Problem1.py"])

    # break
    print("\n====================")

    # Run the second file
    print("\nRunning the second file:")
    subprocess.run(["python", "Problem2.py"])
