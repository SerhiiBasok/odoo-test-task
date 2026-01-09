{
    "name": "Specialist Journal",
    "version": "1.0.0",
    "author": "Serhii Dev",
    "category": "Custom",
    "summary": "Journal of specialist notes per client",
    "depends": ["base"],
    "application": True,
    "data": [
        "security/ir.model.access.csv",
        "security/journal_rules.xml",
        "views/journal_entry_views.xml",
        "views/journal_template_views.xml",
        "views/res_partner_views.xml",
    ],
}
