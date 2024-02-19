from django.contrib import admin
from . models import Loan , Applicant
from import_export.admin import ImportExportModelAdmin
# from .resources import LoanResource

admin.site.register( Loan , ImportExportModelAdmin)

admin.site.register( Applicant , ImportExportModelAdmin)