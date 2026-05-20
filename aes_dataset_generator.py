from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import pandas as pd
import os


def generate_aes_dataset(total_samples=5000):

    os.makedirs("dataset", exist_ok=True)

    dataset = []

    print("Generating AES encryption dataset...\n")

    for sample in range(total_samples):

        plaintext = get_random_bytes(16)

        secret_key = get_random_bytes(16)

        cipher = AES.new(secret_key, AES.MODE_ECB)

        ciphertext = cipher.encrypt(plaintext)

        dataset.append({
            "plaintext": plaintext.hex(),
            "key": secret_key.hex(),
            "ciphertext": ciphertext.hex()
        })

        if (sample + 1) % 500 == 0:
            print(f"{sample + 1} samples generated")

    dataframe = pd.DataFrame(dataset)

    output_path = "dataset/aes_dataset.csv"

    dataframe.to_csv(output_path, index=False)

    print("\nAES dataset generation completed successfully")
    print(f"Dataset saved at: {output_path}")


if __name__ == "__main__":
    generate_aes_dataset()