import gzip

def compress_file(source_file, destination_file):
    try:
        with open(source_file, 'rb') as source_stream:
            with gzip.open(destination_file, 'wb') as destination_stream:
                destination_stream.writelines(source_stream)
        print(f"File {source_file} compressed to {destination_file} successfully")
    except Exception as e:
        print(f"Error compressing file: {e}")

if __name__ == "__main__":
    source_file = "input.txt"
    destination_file = "compressed_output.gz"

    compress_file(source_file, destination_file)
