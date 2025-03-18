import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Child:
    def __init__(self, father, mother):
        # Memilih alel dari ayah dan ibu
        self.father_alel = random.choice(father.blood_type)
        self.mother_alel = random.choice(mother.blood_type)
        self.child_blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        # Menggabungkan alel dari ayah dan ibu untuk menentukan golongan darah
        if self.father_alel == 'A' and self.mother_alel == 'A':
            return 'A'
        elif self.father_alel == 'A' and self.mother_alel == 'B':
            return random.choice(['A', 'AB'])
        elif self.father_alel == 'A' and self.mother_alel == 'O':
            return 'A'
        elif self.father_alel == 'B' and self.mother_alel == 'A':
            return random.choice(['A', 'AB'])
        elif self.father_alel == 'B' and self.mother_alel == 'B':
            return 'B'
        elif self.father_alel == 'B' and self.mother_alel == 'O':
            return 'B'
        elif self.father_alel == 'O' and self.mother_alel == 'A':
            return 'A'
        elif self.father_alel == 'O' and self.mother_alel == 'B':
            return 'B'
        elif self.father_alel == 'O' and self.mother_alel == 'O':
            return 'O'
        elif self.father_alel == 'AB' or self.mother_alel == 'AB':
            return random.choice(['A', 'B', 'AB'])

    def __str__(self):
        return f"Golongan darah anak: {self.child_blood_type}"

if __name__ == "__main__":
    # Input golongan darah ayah
    father_blood_type = input("Masukkan golongan darah ayah (A, B, AB, O): ").strip().upper()
    father = Father(father_blood_type)

    # Input golongan darah ibu
    mother_blood_type = input("Masukkan golongan darah ibu (A, B, AB, O): ").strip().upper()
    mother = Mother(mother_blood_type)

    # Membuat objek Child
    child = Child(father, mother)

    # Menampilkan golongan darah anak
    print(child)