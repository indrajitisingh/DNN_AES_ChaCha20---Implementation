from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import pandas as pd
import os


def generate_chacha_dataset(total_samples=5000):

    os.makedirs("dataset", exist_ok=True)

    dataset = []

    print("Generating ChaCha20 encryption dataset...\n")

    for sample in range(total_samples):

        plaintext = get_random_bytes(32)

        secret_key = get_random_bytes(32)

        cipher = ChaCha20.new(key=secret_key)

        ciphertext = cipher.encrypt(plaintext)

        dataset.append({
            "plaintext": plaintext.hex(),
            "key": secret_key.hex(),
            "nonce": cipher.nonce.hex(),
            "ciphertext": ciphertext.hex()
        })

        if (sample + 1) % 500 == 0:
            print(f"{sample + 1} samples generated")

    dataframe = pd.DataFrame(dataset)

    output_path = "dataset/chacha_dataset.csv"

    dataframe.to_csv(output_path, index=False)

    print("\nChaCha20 dataset generation completed successfully")
    print(f"Dataset saved at: {output_path}")


if __name__ == "__main__":
    generate_chacha_dataset()