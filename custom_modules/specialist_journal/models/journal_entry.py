from odoo import models, fields, api
from datetime import datetime


class SpecialistJournalEntry(models.Model):
    _name = "specialist.journal.entry"
    _description = "Note of specialist journal"
    _order = "date desc"

    date = fields.Datetime(string="Date", default=lambda self: fields.Datetime.now())
    user_id = fields.Many2one(
        "res.users", string="Specialist", default=lambda self: self.env.user
    )
    partner_id = fields.Many2one("res.partner", string="Customer", required=True)
    note = fields.Text(string="Text")
    template_ids = fields.Many2many("specialist.journal.template", string="Design")

    @api.onchange("template_ids")
    def _onchange_template_ids(self):
        if self.template_ids:
            self.note = "\n".join(t.content for t in self.template_ids)
