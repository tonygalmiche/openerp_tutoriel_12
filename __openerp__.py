# -*- coding: utf-8 -*-

{
  "name" : "InfoSaône - Module OpenERP Tutoriel 12",
  "version" : "0.1",
  "author" : "InfoSaône",
  "category" : "InfoSaône/Tutoriel",


  'description': """
InfoSaône / Module OpenERP Tutoriel 12 
===================================================

Le but de ce module est de montrer comment créer une vue dans Postgres permettant par exemple d'afficher les données de plusieurs tables ou de trier une liste différement.

Ce module installe le module `account_voucher` pour créer une liste des factures personnalisées.

""",

  'maintainer': 'InfoSaône',
  'website': 'http://www.infosaone.com',
  "depends" : ["base","account_voucher"],  # Liste des dépendances (autres modules nececessaire au fonctionnement de celui-ci)
  "init_xml" : [],              # Liste des fichiers XML à installer uniquement lors de l'installation du module
  "demo_xml" : [],              # Liste des fichiers XML à installer pour charger les données de démonstration
  "update_xml" : ["tutoriel12.xml"],            # Liste des fichiers XML à installer lors d'une mise à jour du module (ou lord de l'installation)
  "installable": True,          # Si False, ce module sera visible mais non installable (intéret ?)
  "active": False               # Si True, ce module sera installé automatiquement dés la création de la base de données d'OpenERP
}





