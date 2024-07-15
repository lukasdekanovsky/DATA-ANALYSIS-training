import random
import pandas as pd

# Úloha 2
# Data o několika stovkách klientů obsahují dva sloupce: pohlaví a věk. Máme hypotézu, že podíl žen mezi klienty se statisticky významně mění s věkem.
#       a) Navrhněte způsob, jak graficky znázornit data tak, abychom si udělali dobrou a korektní představu, zda může hypotéza platit.
#       b) Navrhněte vhodnou statistickou metodu, která by hypotézu na datech ověřila. Můžete uvést i více metod.

def generate_dataset():
    dataset = []
    female_ratio = 0.4  # Starting with 40% females
    exponential_factor = 1.001  # Adjust this to control the rate of increase

    for i in range(800):
        age = random.randint(18, 100)
        if random.random() < female_ratio:
            gender = 'F'
        else:
            gender = 'M'
        dataset.append((age, gender))
        female_ratio *= exponential_factor
        female_ratio = min(female_ratio, 0.9)  # Ensure the ratio does not exceed 90%

    data = pd.DataFrame(dataset, columns=["age", "gender"])
    print(data["gender"].value_counts())
    data.to_csv("data.csv", index=False)

def main():
    generate_dataset()

if name == "__main__":
    main()