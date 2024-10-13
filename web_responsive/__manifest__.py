# Copyright 2016-2017 LasLabs Inc.
# Copyright 2017-2018 Tecnativa - Jairo Llopis
# Copyright 2018-2019 Tecnativa - Alexandre Díaz
# Copyright 2021 ITerra - Sergey Shebanin
# Copyright 2023 Onestein - Anjeel Haria
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Web Responsive",
    "summary": "Responsive web client, community-supported",
    "version": "16.0.1.3.1",
    "category": "Website",
    "website": "https://github.com/OCA/web",
    "author": "LasLabs, Tecnativa, ITerra, Onestein, "
    "Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "installable": True,
    "depends": ["web", "mail"],
    "development_status": "Production/Stable",
    "maintainers": ["Tardo", "SplashS"],
    "excludes": ["web_enterprise"],
    "assets": {
        "web.assets_backend": [
            "/web_responsive/static/src/components/ui_context.esm.js",
            "/web_responsive/static/src/components/apps_menu/apps_menu.scss",
            "/web_responsive/static/src/components/apps_menu/apps_menu.esm.js",
            "/web_responsive/static/src/components/hotkey/hotkey.scss",
            "/web_responsive/static/src/components/apps_menu/apps_menu.xml",
            "/web_responsive/static/src/components/hotkey/hotkey.xml",
        ],
    },
    "sequence": 1,
}
