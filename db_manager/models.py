from sqlalchemy import Table, Column, Integer, String, Date, MetaData


metadata = MetaData()


patients_table = Table(
    "patients",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("surname", String),
    Column("name", String),
)


# class Patient(models.Model):
#     surname = models.CharField()
#     name = models.CharField()
#     patronymic = models.CharField()
#     birthday = models.DateField()
#     gender = models.CharField()
#     settlement = models.CharField()
#     address = models.CharField()
#     phone = models.CharField()


# class Consultation(models.Model):
#     patient = models.ForeignKey(
#         Patient,
#         on_delete=models.CASCADE,
#     )