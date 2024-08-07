import subprocess
import sys
import io

import subprocess


def execute_and_compare(python_file, input_file, output_file, delimiter="\n"):
    # Read the input file content
    with open(input_file, "r") as f:
        input_data = f.read().split(delimiter)

    # Read the expected output file content
    with open(output_file, "r") as f:
        expected_output_data = f.read().split(delimiter)

    # Ensure the number of test cases matches
    if len(input_data) != len(expected_output_data):
        print("Number of test cases in input and output files do not match.")
        return

    all_tests_passed = True

    for i, (input_case, expected_output) in enumerate(
        zip(input_data, expected_output_data)
    ):
        # Execute the python file for each test case
        process = subprocess.Popen(
            ["python", python_file],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        output, error = process.communicate(input=input_case)

        if error:
            print(f"Error during execution of test case {i+1}: {error}")
            all_tests_passed = False
            continue

        # Compare the actual output with the expected output
        if output.strip() == expected_output.strip():
            print(f"Test case {i+1} passed")
        else:
            print(f"Test case {i+1} failed")
            print("Expected Output:")
            print(expected_output)
            print("Actual Output:")
            print(output)
            all_tests_passed = False

    if all_tests_passed:
        print("All test cases passed.")
    else:
        print("Some test cases failed.")


# Example usage
execute_and_compare("script.py", "input.txt", "output.txt")


if __name__ == "__main__":
    execute_and_compare(sys.argv[1], sys.argv[2], sys.argv[3])
