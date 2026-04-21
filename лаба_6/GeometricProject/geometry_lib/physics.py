def get_mass(volume, material):
    densities = {
        "Сталь": 7850, 
        "Дерево": 600,
        "Алюминий": 2700,
        "Медь": 8920,
        "Бетон": 2400,
        "Пластик": 950
    }
    return volume * densities.get(material, 1000)