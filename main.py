import json
import xml.etree.ElementTree as ET

"""Класс для обработки исключения"""
class InvalidYearError(Exception):
    pass

"""Cоздание абстрактного класса здравоохранение"""
class Healthcare():
    """Свойства класса здравоохранение"""
    def __init__(self, name, year, gender):
        self.name = name
        self.gender = gender
        """Обработка исключения"""
        if not isinstance(year, int):
            raise InvalidYearError("Year must be an integer.")
        self.year = year

    def to_dict(self):
        try:
            return {
                'name': self.name,
                'year': self.year,
                'gender': self.gender
            }
        except InvalidYearError as e:
            print(e)

"""Наследуемый класс доктор"""
class Doctor(Healthcare):
    def __init__(self, name, year, gender, speciality):
        super().__init__(name, year, gender)
        self.speciality = speciality

    def to_dict(self):
        doctor_dict = super().to_dict()
        doctor_dict.update(
            {
                'speciality': self.speciality
            }
        )
        return doctor_dict

"""Наследуемый класс пациент"""
class Patient(Healthcare):
    def __init__(self, name, year, gender, diagnosis):
        super().__init__(name, year, gender)
        self.diagnosis = diagnosis

    def to_dict(self):
        patient_dict = super().to_dict()
        patient_dict.update(
            {
                'diagnosis': self.diagnosis
            }
        )
        return patient_dict
"""Создание объектов"""
doctor_1 = Doctor("Иванов И.И", 1986, "муж", "Кардиолог")
doctor_2 = Doctor("Иванова И.И", 1992, "жен", "Медсестра")
patient_1 = Patient("Ирина", 1954, "жен", "Воспаления миокарда")
patient_2 = Patient("Сергей", 1948, "муж", "Инфаркт")
"""Преобразование объектов в словари"""
dict_Healthcare = {
    "doctor": [doctor_1.to_dict(), doctor_2.to_dict()],
    "patient": [patient_1.to_dict(), patient_2.to_dict()]
}
"""Запись данных в формате JSON"""
with open('out.json', 'w') as json_file:
    json.dump(dict_Healthcare, json_file, indent=4)

try:
    """чтение файла input.json"""
    with open('input.json', 'r', encoding='utf-8') as input_file:
        for line in input_file:
            print(line)
except FileNotFoundError:
    print("File not found")

"""Создаем XML-структуру"""
root = ET.Element("doctor")
for doctor in [doctor_1, doctor_2]:
    doctor_element = ET.SubElement(root, "doctor")
    for key, value in doctor.to_dict().items():
        ET.SubElement(doctor_element, key).text = str(value)

for patient in [patient_1, patient_2]:
    patient_element = ET.SubElement(root, "patient")
    for key, value in patient.to_dict().items():
        ET.SubElement(patient_element, key).text = str(value)

"""Сохраняем данные в формате XML"""
tree = ET.ElementTree(root)
tree.write('data.xml')
with open('data_from_json.json', 'r') as json_file:
    loaded_data = json.load(json_file)
with open('data_to_json.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)