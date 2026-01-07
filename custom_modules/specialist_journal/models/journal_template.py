from odoo import models, fields


class SpecialistJournalTemplate(models.Model):
    _name = "specialist.journal.template"
    _description = "Journal Entry Template"

    name = fields.Char(string="Template Name", required=True)
    text = fields.Text(string="Template Text", required=True)
