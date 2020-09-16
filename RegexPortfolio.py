import os
import json
import sublime
import sublime_plugin


REGEX_PREFIX_ = "(?m)^(?!(^\s*$))([ \\t#'\/\*]*(\.+)?)"
_REGEX_SUFFIX = "(?:\R*(?>( *[ \\t#'\/\*]*)[ \\t]+)(?![\*:]).*)*"
_REGEX = {
	"keywords": "REGEX_PREFIX_( ?:?(keyword)s?::?.*)_REGEX_SUFFIX",
	"synopsis": "REGEX_PREFIX_( ?:?(synopsis|description|desc)s?::?.*)_REGEX_SUFFIX",
	"changelog": "REGEX_PREFIX_( ?:?(changelog)s?::?.*)_REGEX_SUFFIX",
	"todo": "REGEX_PREFIX_( ?:?(todo)s?::?.*)_REGEX_SUFFIX",
	"note": "REGEX_PREFIX_( ?:?(note)s?::?.*)_REGEX_SUFFIX",
	"warning": "REGEX_PREFIX_( ?:?(warning)s?::?.*)_REGEX_SUFFIX",
	"all_flag": "REGEX_PREFIX_( ?:?(keyword|synopsis|description|desc|changelog|todo|note|warning)s?::?.*)_REGEX_SUFFIX",
}

SETTINGS_FILE = 'RegexPortfolio.sublime-settings'
USER_REGEX_PORTFOLIO_KEY = "user_regex_portfolio"
custom_settings = None

CONTEXT_SUBLIME_MENU = "Context.sublime-menu"
CONTEXT_JSON_MAIN_LEVEL = 0
CONTEXT_JSON_USER_LEVEL = 5


def cache_path():
	return os.path.join(sublime.cache_path(), __package__)


def packages_path():
	return os.path.join(sublime.packages_path(), __package__)


def build_user_context_menu_file():
	sublime_context_menu = os.path.join(packages_path(), CONTEXT_SUBLIME_MENU)

	with open(sublime_context_menu, "r") as json_in_file:
		context_menu = json.load(json_in_file)

	user_regex_def = regex_portfolio_settings()
	user_regex_def = check_regex_dict_keys(user_regex_def)
	user_regex_def = gather_user_regex(user_regex_def)
		
	user_menu = context_menu[CONTEXT_JSON_MAIN_LEVEL]["children"][CONTEXT_JSON_USER_LEVEL]["children"]
	user_menu_settings = user_menu[0:1]

	_user_menu = user_menu_settings
	for u in user_regex_def:
		_user_menu.append(build_user_menu(u))

	context_menu[CONTEXT_JSON_MAIN_LEVEL]["children"][CONTEXT_JSON_USER_LEVEL]["children"] = _user_menu

	with open(sublime_context_menu, 'w') as json_out_file:
		json.dump(context_menu, json_out_file)

	# sublime_plugin.reload_plugin(__package__)


def regex_portfolio_settings():
	view = sublime.active_window().active_view()

	if view.settings().has(USER_REGEX_PORTFOLIO_KEY):
		return view.settings().get(USER_REGEX_PORTFOLIO_KEY)

	global custom_settings
	if custom_settings is None:
		custom_settings = sublime.load_settings(SETTINGS_FILE)

	return custom_settings.get(USER_REGEX_PORTFOLIO_KEY)


def check_regex_dict_keys(regex_dictionaries):
	check = []
	for i, reg in enumerate(regex_dictionaries, start=1):
		for key in reg.keys():
			if key not in ["name", "description", "regex"]:
				is_good_dict = False
				break
			else:
				is_good_dict = True

		if is_good_dict:
			check += [{"is_good_dict": True, "regex": reg}]
		else:
			check += [{"is_good_dict": False, "regex": key}]

	return check


def has_undefined_dict_keys(checked_regex_dictionaries):
	for i, check in enumerate(checked_regex_dictionaries, start=1):
		if check["is_good_dict"] == False:
			sublime.error_message("Unknown key '{key}' defined in dictionary #{i}".format(key=check["regex"], i=i))


def gather_user_regex(checked_regex_dictionaries):
	user_regex = []
	for i, check in enumerate(checked_regex_dictionaries, start=1):
		if check["is_good_dict"]:
			user_regex.append(check["regex"])

	return user_regex


def build_user_menu(user_regex_dictionaries):
	_ = {}
	if len(user_regex_dictionaries["description"]) > 31:
		desc = " (" + user_regex_dictionaries["description"][0:31] + "...)"
	else:
		desc = " (" + user_regex_dictionaries["description"] + ")"

	_["caption"] = user_regex_dictionaries["name"] + desc
	_["command"] = "load_regex"
	_["args"] = {
		"regex_pattern": user_regex_dictionaries["regex"],
		"user_regex": True
	}

	return _


class RegexPortfolioListener(sublime_plugin.EventListener):
	def on_activated(self, view):
		user_regex_def = regex_portfolio_settings()
		check_user_regex = check_regex_dict_keys(user_regex_def)
		has_undefined_dict_keys(check_user_regex)
		build_user_context_menu_file()


class FindPanel(sublime_plugin.WindowCommand):
	def show_panel(self, regex_pattern, user_regex=False):
		window = self.window
		window.run_command("hide_panel")

		options = {
			"panel": "find_in_files",
			"regex": True,
			"case_sensitive": False,
			"show_context": True,
		}

		if int(sublime.version()) < 2134:
			options["location"] = options["where"]
			del options["where"]

		window.run_command("show_panel", options)
		window.run_command("insert", {"characters": ""})

		if user_regex:
			window.run_command("insert", {"characters": regex_pattern})
		else:
			window.run_command("insert", {
				"characters": _REGEX[regex_pattern] \
					.replace("REGEX_PREFIX_", REGEX_PREFIX_)
					.replace("_REGEX_SUFFIX", _REGEX_SUFFIX)
				}
			)


class LoadRegex(FindPanel):
	def run(self, regex_pattern, user_regex=False):
		self.show_panel(regex_pattern, user_regex)


def plugin_loaded():
	pass
