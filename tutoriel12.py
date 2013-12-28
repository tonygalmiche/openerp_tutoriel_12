# -*- coding: utf-8 -*-

from osv import osv
from osv import fields


class tutoriel12(osv.osv):
  # Cette option permet de préciser que l'on souhaite créer une vue et non pas une table dans Postgres
  _auto = False

  # Nom et description de la vue
  _name = "tutoriel12"
  _description = "Tutoriel 12"

  # Champs de la vue (Mettre readonly sur tous les champs). 
  # -> Il est possible de mettre en place des relations avec d'autres tables comme dans cet exemple
  _columns = {
    'date_facture': fields.date('Date Facture', readonly=True),
    'facture_id':fields.many2one('account.invoice', 'Facture', readonly=True, relate=True),
    'partner_id':fields.many2one('res.partner', 'Partenaire', readonly=True, relate=True)
  }


  # Cette méthode permet de créer la vue à partir des données des autres tables de Postgres
  def init(self, cr):
    cr.execute("""
        create or replace view tutoriel12 as (
            select
                a.id as id,
                a.date_invoice as date_facture,
                a.id as facture_id,
                a.partner_id as partner_id
            from
                account_invoice a)""")


  # Ordre de tri 
  _order = "date_facture desc"

tutoriel12()


