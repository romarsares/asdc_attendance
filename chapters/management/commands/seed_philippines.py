from django.core.management.base import BaseCommand
from chapters.models import Region, Province, Municipality, Barangay


DATA = {
    "code": "XII",
    "name": "SOCCSKSARGEN",
    "provinces": [
        {
            "name": "South Cotabato",
            "municipalities": [
                {
                    "name": "General Santos City",
                    "barangays": [
                        "Apopong", "Baluan", "Batomelong", "Buayan", "Bula",
                        "Calumpang", "City Heights", "Conel", "Dadiangas East",
                        "Dadiangas North", "Dadiangas South", "Dadiangas West",
                        "Fatima", "Katangawan", "Lagao", "Labangal", "Ligaya",
                        "Mabuhay", "Olympog", "San Isidro", "San Jose",
                        "Sinawal", "Tambler", "Tinagacan", "Upper Labay",
                    ],
                },
                {
                    "name": "Koronadal City",
                    "barangays": [
                        "Assumption", "Avanceña", "Caloocan", "Carpenter Hill",
                        "Concepcion", "Esperanza", "General Paulino Santos",
                        "Mabini", "Mambucal", "Morales", "Namnama", "New Pangasinan",
                        "Paraiso", "Rotonda", "San Isidro", "San Jose",
                        "Santa Cruz", "Santo Niño", "Saravia", "Zone I",
                        "Zone II", "Zone III", "Zone IV",
                    ],
                },
            ],
        },
        {
            "name": "Sarangani",
            "municipalities": [
                {
                    "name": "Alabel",
                    "barangays": [
                        "Alegria", "Bagacay", "Baluntay", "Datal Anggas",
                        "Domolok", "Kawas", "Ladol", "Maribulan", "Pag-Asa",
                        "Paraiso", "Poblacion", "Public Market Area", "Salakit",
                        "Suli", "Talahik", "Tokawal",
                    ],
                },
                {
                    "name": "Malapatan",
                    "barangays": [
                        "Baliton", "Batotuling", "Batulaki", "Big Margus",
                        "Daan Suyan", "Kalaong", "Kapatan", "Little Margus",
                        "Lun Masla", "Lun Padidu", "Maguling", "Malungon Gamay",
                        "Poblacion", "Sapu Masla", "Sapu Padidu", "Tuyan",
                    ],
                },
            ],
        },
        {
            "name": "Sultan Kudarat",
            "municipalities": [
                {
                    "name": "Isulan",
                    "barangays": [
                        "Bambad", "Bual", "Dansuli", "Impao", "Kalawag I",
                        "Kalawag II", "Kalawag III", "Kenram", "Kolambog",
                        "Lagandang", "Laguilayan", "Mapantig", "New Pangasinan",
                        "Paddaya", "Poblacion", "Sampao", "Tayugo",
                    ],
                },
                {
                    "name": "Tacurong City",
                    "barangays": [
                        "Baras", "Buenaflor", "Calean", "Carmelo", "Griño",
                        "Kakar", "Lancheta", "Lapu", "Lower Katungal",
                        "New Isabela", "New Lagao", "New Passi", "Poblacion",
                        "Rajah Nuda", "San Antonio", "San Emmanuel", "San Pablo",
                        "Santa Cruz", "Santa Maria", "Santo Niño", "Upper Katungal",
                    ],
                },
            ],
        },
        {
            "name": "North Cotabato",
            "municipalities": [
                {
                    "name": "Kidapawan City",
                    "barangays": [
                        "Amas", "Amazion", "Balabag", "Binoligan", "Birada",
                        "Gayola", "Ginatilan", "Indangan", "Ilomavis", "Lanao",
                        "Linangkob", "Luvimin", "Macabolig", "Malinan",
                        "Manongol", "Marbel", "Mateo", "Meochao", "Mua-an",
                        "New Bohol", "Nuangan", "Onica", "Paco", "Perez",
                        "Poblacion", "Puas", "Salvacion", "San Isidro",
                        "San Roque", "Santo Niño", "Sikitan", "Singao",
                        "Sudapin", "Sumbao",
                    ],
                },
            ],
        },
    ],
}


class Command(BaseCommand):
    help = "Seed Region XII sample data"

    def handle(self, *args, **kwargs):
        region, _ = Region.objects.get_or_create(
            code=DATA["code"], defaults={"name": DATA["name"]}
        )

        for prov_data in DATA["provinces"]:
            province, _ = Province.objects.get_or_create(
                name=prov_data["name"], region=region
            )

            for mun_data in prov_data["municipalities"]:
                municipality, _ = Municipality.objects.get_or_create(
                    name=mun_data["name"], province=province
                )

                barangays = [
                    Barangay(name=b, municipality=municipality)
                    for b in mun_data["barangays"]
                    if not Barangay.objects.filter(name=b, municipality=municipality).exists()
                ]
                Barangay.objects.bulk_create(barangays)

        self.stdout.write(self.style.SUCCESS("Region XII sample data seeded."))
