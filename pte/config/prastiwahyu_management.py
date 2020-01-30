from __future__ import unicode_literals
from frappe import _


def get_data():
	return [
        {	
        "label": _("Management Surat"),
		"items":[
				{
					"type": "doctype",
					"label": "Surat Corporate",
					"name": "Management Surat Corporate",
					"description": _("Imput masukan barang Beacukai."),
				},
				{
					"type": "doctype",
					"label": "Surat Sales",
					"name": "Management Surat Sales",
					"description": _("Imput masukan barang Beacukai."),
				},
				{
					"type": "doctype",
					"label": "Management Surat SKD",
					"name": "Management Surat Pengangkatan",
					"description": _("Imput masukan barang Beacukai."),
				},
				{
					"type": "doctype",
					"label": "Surat Kontrak Percobaan",
					"name": "Management Surat PKWTT",
					"description": _("Imput masukan barang Beacukai."),
				},
				{
					"type": "doctype",
					"label": "Surat Kontrak",
					"name": "Management Kontrak Karyawan",
					"description": _("Imput masukan barang Beacukai."),
				},
				{
					"type": "doctype",
					"label": "Surat SK Mutasi",
					"name": "Management Surat Mutasi",
					"description": _("Imput masukan barang Beacukai."),
				},

				]
		},
				{
        "label": _("Laporan"),
        "items": 
            [
				{
					"type": "report",
					"name": "Laporan Pertanggungjawaban Barang Jadi",
					"description": _("Applications for leave."),
					"doctype": "Laporan",
					"is_query_report": True,


				},
				{
					"type": "report",
					"label": "Laporan Posisi Barang WIP",
					"name": "Laporan Posisi Barang",
					"description": _("Applications for leave."),
					"doctype": "Laporan",
					"is_query_report": True,

				},
				{
					"type": "report",
					"name": "Laporan Pertanggungjawaban Mutasi Bahan Baku dan Bahan Penolong",
					"description": _("Applications for leave."),
					"doctype": "Laporan",
					"is_query_report": True,

				},
				{
					"type": "report",
					"name": "Laporan Pertanggungjawaban Barang Reject dan Scrap",
					"description": _("Applications for leave."),
					"doctype": "Laporan",
					"is_query_report": True,

				},
				{
					"type": "report",
					"name": "Laporan Stock Opname",
					"description": _("Applications for leave."),
					"doctype": "Stock Opname",
					"is_query_report": True,

				},
				{
					"type": "report",
					"name": "Laporan Pertanggungjawaban Mutasi Mesin dan Peralatan Kantor",
					"description": _("Applications for leave."),
					"doctype": "Mutasi Mesin dan Peralatan Kantor",
					"is_query_report": True,

				},

		
			]
        },
		{
			"label": _("Transaksi Lainnya"),
			"items":
			[ 
				{
					"type": "report",
					"label": "Riwayat Pengguna",
					"name": "Riwayat Pengguna",
					"is_query_report": True,

				},
				{
					"type": "doctype",
					"label": "Stock Opname",
					"name": "Stock Opname",
					"description": _("Monthly salary statement."),
				},
				{
					"type": "doctype",
					"label": "Mutasi Mesin dan Peralatan Kantor",
					"name": "Mutasi Mesin dan Peralatan Kantor",
					"description": _("Monthly salary statement."),
				},

				
			]
		}
	]

