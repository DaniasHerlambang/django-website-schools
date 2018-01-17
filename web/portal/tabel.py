#!/usr/bin/env python
# coding: utf-8
from datetime import date
import django

if django.VERSION >= (1, 10):
    from django.urls import reverse_lazy
else:
    from django.core.urlresolvers import reverse_lazy

from table.columns import Column
from table.columns.calendarcolumn import CalendarColumn
from table.columns.sequencecolumn import SequenceColumn
from table.columns.imagecolumn import ImageColumn
from table.columns.linkcolumn import LinkColumn, Link, ImageLink
from table.columns.checkboxcolumn import CheckboxColumn
from table import Table
from table.utils import A

from portal.models import data_guru

class TabelData(Table):
    id_guru_tab = Column(field='id_guru', header='#')
    nama_guru_tab = LinkColumn(header='NAMA', links=[
        Link( args=(A('id_guru'),), text=A('nama_guru'))])
    kelamin_guru_tab = Column(field='kelamin_guru', header='KELAMIN')
    pelajaran_guru_tab = Column(field='pelajaran_guru', header='PELAJARAN')


    # logo = ImageColumn(field='logo.url', header='Logo Image', image_title='logo')

    class Meta:
        model = data_guru
