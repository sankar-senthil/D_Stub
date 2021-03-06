# Generated by Django 3.2.7 on 2021-10-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paystub',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Employee_Name', models.CharField(max_length=264)),
                ('Employee_Address', models.CharField(max_length=264)),
                ('Company_Name', models.CharField(max_length=264)),
                ('Company_Address', models.CharField(max_length=264)),
                ('SSN', models.CharField(max_length=264)),
                ('Reporting_Period', models.CharField(max_length=264)),
                ('Pay_Date', models.CharField(max_length=264)),
                ('A8090', models.CharField(max_length=264)),
                ('Income', models.CharField(max_length=264)),
                ('Rate', models.CharField(max_length=264)),
                ('Hours', models.CharField(max_length=264)),
                ('Current_Pay', models.CharField(max_length=264)),
                ('Fica_Medicare_Total', models.CharField(max_length=264)),
                ('Fica_Medicare_YTD', models.CharField(max_length=264)),
                ('Fica_Social_Security_Total', models.CharField(max_length=264)),
                ('Fica_Social_Security_YTD', models.CharField(max_length=264)),
                ('Federal_tax_Total', models.CharField(max_length=264)),
                ('Federal_tax_YTD', models.CharField(max_length=264)),
                ('State_Tax_Total', models.CharField(max_length=264)),
                ('State_Tax_YTD', models.CharField(max_length=264)),
                ('YTD_Gross', models.CharField(max_length=264)),
                ('YTD_Deductions', models.CharField(max_length=264)),
                ('YTD_Net_Pay', models.CharField(max_length=264)),
                ('Total', models.CharField(max_length=264)),
                ('Deductions', models.CharField(max_length=264)),
                ('Netpay', models.CharField(max_length=264)),
            ],
        ),
    ]
