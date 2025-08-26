def read_and_write_file(input_file, output_file):
    try:
        with open(input_file, "r") as infile:
            content = infile.read()
        modified_content = content.upper()

        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
read_and_write_file("input.txt", "output.txt")
