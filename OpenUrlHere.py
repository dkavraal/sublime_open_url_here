import sublime, sublime_plugin
from tempfile import NamedTemporaryFile
from uuid import uuid1
try:
	from urllib import urlretrieve
except:
	from urllib.request import urlretrieve

class OpenUrlHereCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		def getTempFile():
			return NamedTemporaryFile(delete=False).name

		def on_done(s_url):
			try:
				temp_file_name = getTempFile()
				urlretrieve(s_url, temp_file_name)
				new_view = self.view.window().open_file(temp_file_name)
			except:
				sublime.error_message('Couldnot open URL.')

		self.view.window().show_input_panel("Enter the URL to open in Sublime:", "", on_done, None, None)
