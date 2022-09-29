/** @odoo-module **/

import { registry } from "@web/core/registry";

const userMenuRegistry = registry.category("user_menuitems");

document.addEventListener('DOMContentLoaded', function () {
  userMenuRegistry.remove("documentation");
  userMenuRegistry.remove("separator");
  userMenuRegistry.remove("odoo_account");
  userMenuRegistry.remove("support");
});
