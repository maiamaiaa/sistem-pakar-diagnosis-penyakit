# Aturan dan rekomendasi
rules = [
    {"if": ["demam", "batuk", "sakit_tenggorokan"], "then": "flu"},
    {"if": ["flu", "sakit_kepala"], "then": "influenza"},
    {"if": ["demam", "nyeri_sendi"], "then": "demam_berdarah"},
    {"if": ["flu"], "then": "istirahat_dan_minum_obat"},
    {"if": ["demam_berdarah"], "then": "periksa_ke_dokter"},
    {"if": ["sakit_kepala", "mual"], "then": "migren"},
    {"if": ["demam", "ruam"], "then": "campak"},
    {"if": ["batuk", "sesak_napas"], "then": "asma"},
    {"if": ["nyeri_perut", "mual"], "then": "gastroenteritis"},
    {"if": ["demam", "nyeri_tulang"], "then": "dengue"},
]

rekomendasi = {
    "flu": "Istirahat dan minum obat.",
    "influenza": "Minum obat flu dan istirahat total.",
    "demam_berdarah": "Segera periksa ke dokter.",
    "istirahat_dan_minum_obat": "Istirahat di rumah dan perbanyak cairan.",
    "periksa_ke_dokter": "Konsultasikan ke dokter untuk pemeriksaan lebih lanjut.",
    "migren": "Minum obat pereda nyeri dan istirahat di ruangan gelap.",
    "campak": "Segera periksa ke dokter untuk penanganan lebih lanjut.",
    "asma": "Gunakan inhaler dan hindari pemicu.",
    "gastroenteritis": "Minum banyak cairan dan istirahat.",
    "dengue": "Segera periksa ke dokter untuk penanganan lebih lanjut."
}

# Daftar semua gejala yang diketahui sistem
daftar_gejala = {
    "demam", "batuk", "sakit_tenggorokan", "sakit_kepala", "nyeri_sendi",
    "mual", "ruam", "sesak_napas", "nyeri_perut", "nyeri_tulang"
}

facts = set()

# Fungsi backward chaining yang juga mengumpulkan fakta
def backward_chaining(goal, rules, facts, visited=None):
    if visited is None:
        visited = set()
    if goal in facts:
        return True
    if goal in visited:
        return False
    visited.add(goal)
    for rule in rules:
        if rule["then"] == goal:
            if all(backward_chaining(premis, rules, facts, visited) for premis in rule["if"]):
                facts.add(goal)
                return True
    return False

print("Silakan jawab pertanyaan berikut dengan 'y' atau 'n':")
for gejala in daftar_gejala:
    jawaban = input(f"Apakah Anda mengalami {gejala.replace('_',' ')}? (y/n): ").lower()
    if jawaban == 'y':
        facts.add(gejala)

diagnosis_list = [
    "flu", "influenza", "demam_berdarah", "istirahat_dan_minum_obat", "periksa_ke_dokter",
    "migren", "campak", "asma", "gastroenteritis", "dengue"
]

# Cari penyakit yang cocok dan ukur seberapa cocok (jumlah gejala konkret yang cocok)
diagnosis_results = []

for penyakit in diagnosis_list:
    temp_facts = facts.copy()  
    if backward_chaining(penyakit, rules, temp_facts):
        def count_basic_symptoms(goal, rules, counted=None):
            if counted is None:
                counted = set()
            for rule in rules:
                if rule["then"] == goal:
                    cnt = 0
                    for premis in rule["if"]:
                        if premis in daftar_gejala:
                            counted.add(premis)
                        else:
                            count_basic_symptoms(premis, rules, counted)
                    return len(counted)
            if goal in daftar_gejala:
                return 1
            return 0

        score = count_basic_symptoms(penyakit, rules)
        diagnosis_results.append((penyakit, score))

if diagnosis_results:
    max_score = max(score for _, score in diagnosis_results)
    best_diagnoses = [d for d, s in diagnosis_results if s == max_score]

    print("\n Hasil Diagnosis Terperinci:")
    for penyakit in best_diagnoses:
        print(f"- Kemungkinan Terbesar: {penyakit.replace('_',' ').capitalize()}")
        if penyakit in rekomendasi:
            print(f"  ➤ Saran: {rekomendasi[penyakit]}")
else:
    print("\nTidak ditemukan penyakit berdasarkan gejala yang Anda masukkan.")

